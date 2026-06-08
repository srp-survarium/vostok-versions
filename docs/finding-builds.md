# Finding missing Survarium / Vostok Engine builds

How to hunt for dev builds that ship `survarium.exe` **+ `survarium.pdb`** (the only
ones this project can process). Written after the **0.14h** dead end, but the method
generalises to any missing build.

## The 0.14h case (worked example / current target)

A partial `014h.exe` (InnoSetup 5.5, name "Survarium") turned up — a torrent that
never finished, ~27% of pieces zero-filled. Only the first **5,488,640 bytes** of
`survarium.exe` survive; the `.pdb` is 100% lost (solid LZMA stream, first hole at
file offset 2 MiB). So we must **re-source a complete copy**, not repair this one.

What we extracted about the target (use these to recognise/verify a candidate):

| field | value |
|---|---|
| version string | **0.14h** |
| `survarium.exe` PE TimeDateStamp | **0x52556A76 = 2013-10-09 14:38:46 UTC** |
| linker | MSVC 9.0 |
| exe size (from PE section table) | ~10,863,814 bytes |
| recovered prefix | first **5,488,640** bytes, sha256 `b6edffcd5357889de360704e2b3b06ff1c20a8ca84b025095b2d344e4b5ab7e5` |
| est. build number | **~1351** (range ~1286–1420) |
| est. internal id | **~642** |

### Why archive.org is exhausted for this era

Every build in `versions.json` came from one uploader, **`labx8net@gmail.com`**
(collection `prototypesandpress`, creator "Vostok Games"). Their 41 Vostok items jump
straight from:

```
Vostok Engine v0.1 build 884 (internal id 508), May 28 2013
        ↓  ← entire 0.12–0.19 era missing (incl. 0.14h, Oct 2013)
Vostok Engine v0.20e build 1916 (internal id 804), Mar 20 2014
```

A site-wide archive.org search (all uploaders) returns **no 0.11–0.19 build**. So
0.14h was never on archive.org under any obvious tag — it was distributed through a
different channel. Search **off** archive.org.

## 1. Naming conventions to grep/search for

**archive.org item identifier** (snake_case, lowercased month):
```
vostok_engine_v0.1_build_<N>_internal_id_<M>_<month>_<day>_<year>
# e.g. vostok_engine_v0.1_build_884_internal_id_508_may_28_2013
# 0.14h guess: vostok_engine_v0.14_build_1351_internal_id_642_october_9_2013
```

**archive.org item title:**
```
Vostok Engine v<ver> build <N>(internal id <M>), <Mon> <D> <Year>
# e.g. Vostok Engine v0.14h build 1351(internal id 642), Oct 9 2013
```

**Installer filenames seen** (2013 = InnoSetup `.exe`; 2014+ also `.7z`):
```
survarium_setup_v0100b.exe        survarium_alpha_setup_v0.1.1a.exe
survarium_setup_v011b.exe         survarium_alpha_setup_v0.1.1c.exe
survarium_setup_v011e.exe         survarium_full_020e.7z   (2014 .7z tree)
```
So 0.14h candidate filenames to search for:
```
survarium_setup_v014h.exe   survarium_setup_v0.14h.exe   survarium_setup_v014.exe
survarium_alpha_setup_v0.14h.exe   survarium_alpha_setup_v014h.exe
survarium_full_014h.7z      014h.exe   (what the user's torrent named it)
```

**Free-text terms** (EN + RU — these alpha builds circulated on Russian sites):
```
survarium  "vostok engine"  "internal id"  "closed alpha"  "development engine"
survarium 0.14  survarium v0.14  survarium build 13xx
Сурвариум  Восток  "внутренняя сборка"  альфа  "закрытая альфа"  сборка 13xx
```

## 2. Search avenues (with commands)

### a. Other archive.org uploaders / fuzzy identifiers
The advancedsearch + scrape APIs see more than the website UI:
```sh
# anyone who uploaded survarium/vostok, not just labx8net
curl -s 'https://archive.org/advancedsearch.php?q=%28vostok+engine%29+OR+%28survarium%29&fl[]=identifier&fl[]=title&fl[]=uploader&rows=1000&output=json' | jq -r '.response.docs[]|"\(.uploader)\t\(.title)"'

# scrape API (paginated, full corpus) — catch odd identifiers/collections
curl -s 'https://archive.org/services/search/v1/scrape?q=subject:survarium&count=1000' | jq -r '.items[].identifier'

# probe constructed identifiers directly (404 = not there, 200 = jackpot)
for id in vostok_engine_v0.14h vostok_engine_v0.14_build_1351 survarium_v014h; do
  echo -n "$id -> "; curl -s -o /dev/null -w '%{http_code}\n' "https://archive.org/metadata/$id"; done
```

### b. Wayback Machine — original hosting
These builds were distributed via the dev portal and Russian file hosts before being
mirrored. Pull old download links from the CDX index:
```sh
# any archived URL mentioning survarium setup/installer
curl -s 'http://web.archive.org/cdx/search/cdx?url=*survarium*&matchType=domain&fl=original,timestamp&collapse=urlkey&limit=5000' | grep -iE 'setup|install|\.exe|\.7z|build|download'
# the official sites (download pages, dev blog with build links)
curl -s 'http://web.archive.org/cdx/search/cdx?url=survarium.com*&fl=original,timestamp&collapse=urlkey&limit=10000' | grep -iE 'download|setup|\.exe'
curl -s 'http://web.archive.org/cdx/search/cdx?url=vostokgames.com*&fl=original,timestamp&collapse=urlkey'
```
Old Russian file hosts to look for in those results (2013-era):
`depositfiles`, `letitbit`, `turbobit`, `yadi.sk` / `yandex.disk`, `mail.ru` cloud,
`rghost.ru`, `narod.ru`. If a dead link appears, try fetching it *through* Wayback
(`http://web.archive.org/web/2013*/​<url>`).

### c. Russian trackers & forums (where these builds circulated)
Search these directly (site search or Google `site:`):
```
rutracker.org   nnmclub.to / nnm-club.me   rutor / kinozal   pizdetz / cs.rin.ru
forum.zoneofgames.ru   playground.ru   gamer-info   underground modding boards
```
Google dorks:
```
site:rutracker.org survarium
site:cs.rin.ru survarium pdb
survarium "0.14" (сборка OR build) (внутренняя OR alpha)
intitle:"index of" survarium setup
intitle:"index of" survarium.pdb
inurl:survarium (014 OR v0.14) (exe OR 7z)
```

### d. Recover the dead torrent's infohash, then chase the swarm/DHT
The file came from a torrent — its infohash is the strongest re-find key, and the
swarm/DHT may still hold it even though the original poster left.

> **Recovered infohash (the 0.14h torrent):** `356643b94eba52fee0a8e8b1ea6d88b22a6dd959`
> `magnet:?xt=urn:btih:356643b94eba52fee0a8e8b1ea6d88b22a6dd959`
>
> This is the magnet for the original (incomplete) download. Re-add it and let DHT
> find peers; look the hash up on the indexers below. A complete seeder of the same
> torrent would carry the full `survarium.exe` **+ `survarium.pdb`** — verify any
> result against the §3 fingerprint before trusting it.

```sh
# look in the torrent client's leftovers for the .torrent / resume / fastresume
find ~ -iname '*.torrent' 2>/dev/null | xargs -r grep -ilZ -e survarium -e 014 2>/dev/null
ls -la ~/.config/qBittorrent/ ~/.local/share/qBittorrent/BT_backup/ \
       ~/.config/transmission*/torrents/ ~/.config/deluge/state/ 2>/dev/null
# extract the infohash from a found .torrent
nix-shell -p python3 -p python3Packages.bencodepy --run \
  "python3 -c 'import bencodepy,hashlib,sys; m=bencodepy.bdecode(open(sys.argv[1],\"rb\").read()); print(hashlib.sha1(bencodepy.bencode(m[b\"info\"])).hexdigest())' FILE.torrent"
```
Then look the hash up on DHT/torrent indexers: **BTDigg** (`btdig.com`),
`thetorrent.org`, `idope`, `solidtorrents`, `bt4g`. Re-add the magnet
(`magnet:?xt=urn:btih:<hash>`) and let DHT find peers — a complete seeder may exist
even if the page is gone. Also try **cross-seed**: the same `survarium.exe`/`.pdb`
may live inside a *different* torrent (a bundle/repack) you can pull instead.

### e. People & community
- The archive.org uploader `labx8net@gmail.com` clearly has a private hoard
  (they uploaded 0.1 then 0.20+). Worth a polite ask whether they have 0.12–0.19.
- Survarium modding / X-Ray engine reverse-engineering communities (the same crowd
  that cares about PDBs). Discords/forums around "Vostok Engine", "X-Ray 2.0".

## 3. Verification recipe (confirm a candidate is really 0.14h)

Any found file must match our salvaged fingerprint before trusting it. For an
installer, `innoextract -I app/binaries/win32/survarium.exe` first; then:

```sh
CAND=path/to/found/survarium.exe        # full 10.86 MB exe from the candidate
REF=/tmp/014h/app/binaries/win32/survarium.exe   # our 5,488,640-byte salvage
                                                 # (re-extract from ~/Downloads/014h.exe if /tmp cleared)

# 1) first 5,488,640 bytes must be byte-identical
cmp -n 5488640 "$CAND" "$REF" && echo "PREFIX MATCH ✓" || echo "NOT the same build ✗"

# 2) PE TimeDateStamp must be 0x52556A76 (2013-10-09 14:38:46 UTC)
nix-shell -p python3 --run 'python3 - "$CAND" <<EOF
import struct,sys
d=open(sys.argv[1],"rb").read(0x400); pe=struct.unpack("<I",d[0x3c:0x40])[0]
print("TimeDateStamp:",hex(struct.unpack("<I",d[pe+8:pe+12])[0]),"(want 0x52556a76)")
EOF'

# 3) version string present
strings -el "$CAND" | grep -i '0\.14h'
```
The prefix-match (step 1) is conclusive: 5.49 MB byte-exact cannot collide by chance.
A candidate that passes but ships **no `.pdb`** still can't enter the delink pipeline —
the PDB is mandatory (see README). Confirm both files are present and intact first.

## Once a complete build is in hand

Append its `url` + `sha256` to `versions.json` (hash via `nix-prefetch-url <url>`,
or for a local file compute and add a source path), then:
```sh
python3 scripts/add_version.py v0.14h-build<N>            # delink (needs exe+pdb)
python3 scripts/diff_versions.py v0.1.1e-build884 v0.14h-build<N>
```
This extends the diff chain across the 0.11 → 0.14 gap.
