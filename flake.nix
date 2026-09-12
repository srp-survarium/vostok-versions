{
  description = "Survarium cross-version sources + toolchain: archive.org installers innoextracted to survarium.{exe,pdb}, plus the delink/diff tools on a devShell";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";

    rust-overlay = {
      url = "github:oxalica/rust-overlay";
      inputs.nixpkgs.follows = "nixpkgs";
    };

    # The delink/diff toolchain, fetched from its public source repos (non-flake
    # checkouts used directly as derivation sources).
    vostok-delinker-src = {
      url = "github:srp-survarium/vostok-delinker";
      flake = false;
    };
    vostok-pdb-parser-src = {
      url = "github:srp-survarium/vostok-pdb-parser";
      flake = false;
    };
  };

  outputs = { self, nixpkgs, rust-overlay, vostok-delinker-src, vostok-pdb-parser-src }:
    let
      systems = [ "x86_64-linux" ];
      forAll = nixpkgs.lib.genAttrs systems;

      # Single source of truth, shared with scripts/*.py (which read it as JSON).
      versions = builtins.fromJSON (builtins.readFile ./catalog/versions.json);

      # Post-0.23 builds that are NOT in the delink registry (no PDB), but whose
      # survarium.exe can still be lifted from a game-tree dump on archive.org.
      # Each carries an `exe_url` (an archive.org `view_archive.php` member URL
      # that streams just the exe) + `exe_sha256`, so the flake fetches ~13 MB
      # instead of the multi-GB installer. Shared with scripts/deps_report.py.
      extraBuilds = builtins.fromJSON (builtins.readFile ./catalog/extra_builds.json);

      # All builds we can produce a survarium.exe for, keyed by bare version token
      # ("v0.26g0-build2777" -> "0.26g0") for the `nix build .#"0.26g0"` UX.
      allExeBuilds = versions ++ extraBuilds;
      tokenOf = label:
        builtins.head (nixpkgs.lib.splitString "-" (nixpkgs.lib.removePrefix "v" label));

      pkgsFor = system: import nixpkgs {
        inherit system;
        overlays = [ rust-overlay.overlays.default ];
      };
    in
    {
      packages = forAll (system:
        let
          pkgs = pkgsFor system;

          # Nightly Rust, matching what the delinker/pdb-parser were developed
          # against (they use nightly-only features).
          rust = pkgs.rust-bin.nightly.latest.default.override {
            extensions = [ "rust-src" ];
          };
          nightly-rustPlatform = pkgs.makeRustPlatform { cargo = rust; rustc = rust; };

          # ---------------------------------------------------------------------
          # vostok-delinker - splits an EXE into per-unit COFF .obj files for
          # objdiff, using the PDB for symbol names + function boundaries.
          #
          # cargoHash: update by running `nix build .#vostok-delinker` after
          # `nix flake update vostok-delinker-src` - Nix reports the new hash.
          # ---------------------------------------------------------------------
          vostok-delinker = nightly-rustPlatform.buildRustPackage {
            pname = "vostok-delinker";
            version = "0.1.0";
            src = vostok-delinker-src;
            cargoHash = "sha256-ry3TH1fz7Aj/JdbmlgQFFn29m8E7EQHyGaVXnZTEcXo=";
          };

          # ---------------------------------------------------------------------
          # vostok-pdb-parser - PDB tooling; provides the `pdb_parser` binary that
          # emits readable C++ structure stubs from a build's survarium.pdb.
          #
          # cargoHash: update by running `nix build .#vostok-pdb-parser` after
          # `nix flake update vostok-pdb-parser-src` - Nix reports the new hash.
          # ---------------------------------------------------------------------
          vostok-pdb-parser = nightly-rustPlatform.buildRustPackage {
            pname = "vostok-pdb-parser";
            version = "0.1.0";
            src = vostok-pdb-parser-src;
            cargoHash = "sha256-XUF9ca0D1k5NhR6tZth2/yactZ1NyWc8W9voWNRXcDI=";
          };

          # ---------------------------------------------------------------------
          # objdiff-cli - upstream's prebuilt Linux binary (not in nixpkgs). It is
          # a foreign ELF for a normal FHS distro, so autoPatchelfHook rewrites its
          # interpreter + RPATH into the store. It dlopen's nothing, so the C++
          # runtime alone is enough (no LD_LIBRARY_PATH wrapper needed).
          # ---------------------------------------------------------------------
          objdiffVersion = "3.7.1";
          objdiff-cli = pkgs.stdenv.mkDerivation {
            pname = "objdiff-cli";
            version = objdiffVersion;
            src = pkgs.fetchurl {
              url = "https://github.com/encounter/objdiff/releases/download/v${objdiffVersion}/objdiff-cli-linux-x86_64";
              hash = "sha256-QNhW2gHgpnbA8zr1NOVi8JjNUORey2Tzs0ZBjHsmSuY=";
            };
            dontUnpack = true; # a bare binary; nothing to unpack
            nativeBuildInputs = [ pkgs.autoPatchelfHook ];
            buildInputs = [ pkgs.stdenv.cc.cc.lib ]; # libstdc++ / libgcc_s
            installPhase = "install -Dm755 $src $out/bin/objdiff-cli";
          };

          # ---------------------------------------------------------------------
          # One `version-<label>` package per registry entry: fetch the installer
          # from archive.org and innoextract it to a dir holding survarium.{exe,pdb}
          # (largest non-uninstaller survarium.exe, sibling files copied alongside).
          # ---------------------------------------------------------------------
          # Two packaging formats seen on archive.org: InnoSetup .exe installers
          # (2013 builds) and plain .7z trees (2014 builds, "survarium_full_*").
          extract = v:
            let
              installer = pkgs.fetchurl {
                name = builtins.baseNameOf v.url;
                url = v.url;
                sha256 = v.sha256;
              };
              is7z = pkgs.lib.hasSuffix ".7z" v.url;
              unpack =
                if is7z
                then ''7z x -y -oextract "${installer}" >/dev/null''
                else ''innoextract -d extract "${installer}"'';
              # A build flagged symbols=false (e.g. a stripped retail-style drop)
              # is allowed through without a PDB; the delink step just won't apply.
              requirePdb = (v.symbols or true);
            in
            pkgs.runCommand "survarium-${v.label}" {
              nativeBuildInputs = [ pkgs.innoextract pkgs.p7zip ];
            } ''
              mkdir extract
              ${unpack}
              surv_exe=$(find extract -iname survarium.exe ! -path "*uninstall*" \
                -printf "%s %p\n" | sort -rn | head -1 | awk '{print $2}')
              if [ -z "$surv_exe" ]; then
                echo "ERROR: survarium.exe not found in ${v.label}"; exit 1
              fi
              dir=$(dirname "$surv_exe")
              if [ ! -e "''${surv_exe%.exe}.pdb" ] && ! ls "$dir"/*.pdb >/dev/null 2>&1; then
                ${if requirePdb
                  then ''echo "ERROR: no .pdb beside survarium.exe in ${v.label} (symbol-less build)"; exit 1''
                  else ''echo "WARNING: ${v.label} has no .pdb (symbols=false); extracting exe only"''}
              fi
              mkdir -p "$out"
              cp -r "$dir"/. "$out"/
            '';

          # Dots in a label would split the `nix build .#attr` CLI path, so the
          # package attribute uses an underscore-sanitized label (scripts/common.py
          # applies the same transform). The human label keeps its dots.
          versionPkgs = builtins.listToAttrs (map (v: {
            name = "version-${builtins.replaceStrings [ "." ] [ "_" ] v.label}";
            value = extract v;
          }) versions);

          # ---------------------------------------------------------------------
          # Exe-only packages, addressed by bare version token:
          #     nix build .#"0.26g0"      -> result/0.26g0.exe
          #     nix build .#all           -> result/ with every <token>.exe
          # A build with an `exe_url` (post-0.23 game-tree dump) fetches just the
          # exe; a registry build reuses its full innoextract (cached) and copies
          # the exe out. Each package is a dir holding one `<token>.exe` so they
          # merge cleanly into `all`.
          # ---------------------------------------------------------------------
          exeDir = v:
            let
              token = tokenOf v.label;
              exeFile =
                if v ? exe_url
                then pkgs.fetchurl {
                  name = "survarium-${token}.exe";
                  url = v.exe_url;
                  hash = v.exe_sha256;
                }
                else "${extract v}/survarium.exe";
            in
            pkgs.runCommand "survarium-exe-${token}" { } ''
              mkdir -p "$out"
              cp "${exeFile}" "$out/${token}.exe"
            '';

          exePkgs = builtins.listToAttrs
            (map (v: { name = tokenOf v.label; value = exeDir v; }) allExeBuilds);

          allExes = pkgs.symlinkJoin {
            name = "survarium-all-exes";
            paths = map exeDir allExeBuilds;
          };
        in
        versionPkgs // exePkgs // {
          inherit vostok-delinker vostok-pdb-parser objdiff-cli;
          all = allExes;
        }
      );

      # `nix develop` puts the whole delink/diff toolchain on PATH, so the scripts
      # run with no *_BIN env vars set. innoextract + p7zip cover both archive
      # formats; python3/ruff/ripgrep/jq are the script + inspection tooling.
      devShells = forAll (system:
        let
          pkgs = pkgsFor system;
          p = self.packages.${system};

          # `nix develop .#"0.26g0"` -> a shell with $SURV_EXE pointing at that
          # build's survarium.exe (fetched/extracted on entry).
          exeShells = builtins.listToAttrs (map (v:
            let token = tokenOf v.label; in {
              name = token;
              value = pkgs.mkShell {
                name = "survarium-${token}";
                shellHook = ''
                  export SURV_EXE="${p.${token}}/${token}.exe"
                  echo "survarium ${token} exe -> $SURV_EXE"
                '';
              };
            }) allExeBuilds);

          # `nix develop .#all` -> $SURV_EXES is a dir with every <token>.exe.
          allShell = pkgs.mkShell {
            name = "survarium-all-exes";
            shellHook = ''
              export SURV_EXES="${p.all}"
              echo "all survarium exes in: $SURV_EXES"
              ls "$SURV_EXES"
            '';
          };
        in
        exeShells // {
          all = allShell;
          default = pkgs.mkShell {
            name = "vostok-versions";
            packages = [
              p.vostok-delinker
              p.vostok-pdb-parser
              p.objdiff-cli
              pkgs.innoextract
              pkgs.p7zip
              pkgs.binutils       # `strings` for deps_report.py / package_builds.sh
              pkgs.python3
              pkgs.ruff
              pkgs.ripgrep
              pkgs.jq
            ];
          };
        }
      );
    };
}
