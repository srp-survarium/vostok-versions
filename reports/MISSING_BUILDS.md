# Missing builds — coverage vs. the canonical version list (≤ 0.23h)

Which numbered Survarium / Vostok Engine versions exist up to **0.23h**, and which
we have ingested. Scope is capped at 0.23h per project remit; later versions
(0.24a … 0.30a) are out of scope.

**Bottom line: we hold 9 of the 63 numbered versions the wiki records through
0.23h. 54 are missing.** Almost the entire **0.12 → 0.19 era (Aug 2013 – Feb 2014)
is absent** — and that era is the part archive.org never had (see
[`docs/finding-builds.md`](../docs/finding-builds.md)).

## Source & method

The canonical list is the wiki's **Updates** category, pulled via the MediaWiki API
(the rendered category/article pages 403 the fetcher; the API does not):

    https://survarium.fandom.com/api.php?action=query&list=categorymembers&cmtitle=Category:Updates&cmlimit=500&format=json

Each version's release date was read from its page infobox `date` field, pulled in
batches via `action=query&prop=revisions&rvprop=content` (multiple titles per call).

### Naming: wiki labels = our labels

The wiki writes the 0.1.x line with the middle dot dropped, but the tokens are
otherwise identical to ours:

| wiki page | our label | note |
|---|---|---|
| `0.100b` | `v0.100b` | build 802 |
| `0.11a`  | `v0.1.1a` | i.e. 0.1.1a, build 816 |
| `0.11e`  | `v0.1.1e` | build 884 |
| `0.20e`  | `v0.20e`  | identical token, build 1916 |
| `0.21d`  | `v0.21d`  | build 2010 |
| `0.23h`  | `v0.23h`  | build 2285 |

So from 0.20 onward the wiki and our labels are byte-for-byte the same.

## What we have (9)

All nine came from one archive.org uploader (`labx8net@gmail.com`); all are
internal builds that shipped `survarium.exe` + `survarium.pdb` except the last.

| version | build | date | PDB |
|---|---|---|---|
| v0.100b | 802  | 2013-05-09 | ✓ |
| v0.1.1a | 816  | 2013-05-14 | ✓ |
| v0.1.1b | 826  | 2013-05-14 | ✓ |
| v0.1.1c | 870  | 2013-05-24 | ✓ |
| v0.1.1e | 884  | 2013-05-28 | ✓ |
| v0.20e  | 1916 | 2014-03-20 | ✓ |
| v0.20f  | 1923 | 2014-04-01 | ✓ |
| v0.21d  | 2010 | 2014-04-24 | ✓ |
| v0.23h  | 2285 | 2014-07-17 | ✗ (stripped — out of the function-level diff) |

## What we are missing (54)

`·` = we have it · `✗` = missing · `—` = no wiki page (likely never a distinct
public release). The `span` column is the series' first→last release date.

| series | a | b | c | d | e | f | g | h | span |
|---|---|---|---|---|---|---|---|---|---|
| **0.1** (bare `0.1` page) | — | | | | | | | | 13 May 2013 (public alpha) |
| **0.100b** | · | | | | | | | | 9 May 2013 |
| **0.1.1 (`0.11x`)** | · | · | · | ✗ | · | | | | 14 May – 30 May 2013 |
| **0.12 (`0.12x`)** | ✗ | — | — | ✗ | ✗ | ✗ | ✗ | | 14 Aug – 22 Aug 2013 |
| **0.13 (`0.13x`)** | ✗ | ✗ | ✗ | ✗ | | | | | 11 Sep – 19 Sep 2013 |
| **0.14 (`0.14x`)** | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | 25 Sep – 9 Oct 2013 |
| **0.15 (`0.15x`)** | ✗ | ✗ | ✗ | | | | | | 23 Oct – 25 Oct 2013 |
| **0.16 (`0.16x`)** | ✗ | ✗ | | | | | | | 4 Nov – 6 Nov 2013 |
| **0.17 (`0.17x`)** | ✗ | | | | | | | | 25 Nov 2013 |
| **0.18 (`0.18x`)** | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | | 20 Dec 2013 – 23 Jan 2014 |
| **0.19 (`0.19x`)** | ✗ | ✗ | ✗ | | | | | | 5 Feb – 7 Feb 2014 |
| **0.20 (`0.20x`)** | ✗ | ✗ | ✗ | ✗ | · | · | | | 17 Mar – 1 Apr 2014 |
| **0.21 (`0.21x`)** | ✗ | ✗ | ✗ | · | | | | | 22 Apr – 24 Apr 2014 |
| **0.22 (`0.22x`)** | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | | 30 May – 6 Jun 2014 |
| **0.23 (`0.23x`)** | ✗ | ✗ | ✗ | — | ✗ | — | ✗ | · | 17 Jun – 17 Jul 2014 |

### The 54 missing versions, with release dates

Dates are the wiki's **public-update** release dates. A couple don't track our
*internal-build* dates exactly: `0.1` is dated 13 May though internal build 802 is
9 May, and `0.11d` (30 May) lands after the internal 0.1.1e build (28 May) — public
patch letters and internal build numbers ran on slightly different clocks.

| version | released | | version | released |
|---|---|---|---|---|
| 0.1    | 2013-05-13 | | 0.18a | 2013-12-20 |
| 0.1.1d | 2013-05-30 | | 0.18b | 2013-12-20 |
| 0.12a  | 2013-08-14 | | 0.18c | 2013-12-24 |
| 0.12d  | 2013-08-20 | | 0.18d | 2013-12-27 |
| 0.12e  | 2013-08-20 | | 0.18e | 2013-12-30 |
| 0.12f  | 2013-08-21 | | 0.18f | 2014-01-20 |
| 0.12g  | 2013-08-22 | | 0.18g | 2014-01-23 |
| 0.13a  | 2013-09-11 | | 0.19a | 2014-02-05 |
| 0.13b  | 2013-09-17 | | 0.19b | 2014-02-06 |
| 0.13c  | 2013-09-19 | | 0.19c | 2014-02-07 |
| 0.13d  | 2013-09-18 | | 0.20a | 2014-03-17 |
| 0.14a  | 2013-09-25 | | 0.20b | 2014-03-17 |
| 0.14b  | 2013-09-26 | | 0.20c | 2014-03-19 |
| 0.14c  | 2013-09-27 | | 0.20d | 2014-03-19 |
| 0.14d  | 2013-09-28 | | 0.21a | 2014-04-22 |
| 0.14e  | 2013-09-29 | | 0.21b | 2014-04-23 |
| 0.14f  | 2013-10-01 | | 0.21c | 2014-04-24 |
| 0.14g  | 2013-10-03 | | 0.22a | 2014-05-30 |
| 0.14h  | 2013-10-09 | | 0.22b | 2014-05-30 |
| 0.15a  | 2013-10-23 | | 0.22c | 2014-05-30 |
| 0.15b  | 2013-10-25 | | 0.22d | 2014-06-03 |
| 0.15c  | 2013-10-25 | | 0.22e | 2014-06-03 |
| 0.16a  | 2013-11-04 | | 0.22f | 2014-06-04 |
| 0.16b  | 2013-11-06 | | 0.22g | 2014-06-06 |
| 0.17a  | 2013-11-25 | | 0.23a | 2014-06-17 |
|        |            | | 0.23b | 2014-06-18 |
|        |            | | 0.23c | 2014-06-24 |
|        |            | | 0.23e | 2014-06-30 |
|        |            | | 0.23g | 2014-07-05 |

Note `0.13d` (18 Sep) predates `0.13c` (19 Sep) on the wiki — letter order isn't
strictly chronological there.

## Gap analysis

- **The 0.12 → 0.19 era is the whole hole (33 of the 54).** Our coverage jumps
  from **0.1.1e (build 884, 28 May 2013)** straight to **0.20e (build 1916, 20 Mar
  2014)** — a 10-month, ~1000-build leap that the cross-version diff has to bridge
  in one step (see `CHANGES_NARRATIVE.md`, "the pivot"). Every version in that span
  is missing, and per `docs/finding-builds.md` **no archive.org uploader has any of
  it** — it has to be sourced off archive.org. **0.14h** is the worked re-sourcing
  target (fingerprint + search guide already written; see the salvage notes).

- **The 0.2x line is nearly within reach.** We have 0.20e/0.20f, 0.21d, 0.23h.
  Missing there are the early points of each series (0.20a–d, 0.21a–c) and most of
  0.22/0.23 — the same labx8net-style internal drops, so archive.org is the first
  place to re-check for these specific tags.

- **Wiki gaps (`—`)** — `0.12b`, `0.12c`, `0.23d`, `0.23f` have **no wiki page**, so
  they were probably never distinct public numbered releases (folded hotfixes /
  internal-only). Don't count them as targets unless evidence surfaces.

- **PDB caveat.** Only internal builds that shipped `survarium.exe` **+
  `survarium.pdb`** can enter the delink pipeline. Our 0.1.x and 0.20–0.21 sources
  all carried a PDB; 0.23h did not. Whether any re-sourced missing build is usable
  depends on it shipping a PDB too — verify per the recipe in
  `docs/finding-builds.md` before ingesting.

## Counts

| | count |
|---|---|
| Numbered versions on the wiki, ≤ 0.23h | 63 |
| Have | 9 |
| Missing | 54 |
| — of which in the 0.12–0.19 gap | 33 |
| Wiki-listless tokens inside the range (`—`, not targets) | 4 |

_Canonical list: Survarium Fandom **Category:Updates** (full set 0.1 … 0.30a;
truncated here at 0.23h). Dates: page infoboxes + our `versions.json`._
