# 21 November 2026 — world news in one image

![make.fun competition](https://make.fun/badge/news-image-20261121.svg)
![rank](https://make.fun/badge/news-image-20261121/SnapBucket/newswire-1121v3/rank.svg)
![reward](https://make.fun/badge/news-image-20261121/SnapBucket/newswire-1121v3/reward.svg)

One 1024×1024 page that sums up Saturday 21 November 2026: nine flat-vector
picture panels, eighteen one-line briefs, and a date-check ledger that shows
what was deliberately left out and what had not happened yet.

The competition is on make.fun: <https://make.fun/c/news-image-20261121>.

## What it draws

`entry.png` is a front page in three bands:

| band | contents |
| --- | --- |
| header | `SATURDAY`, the date, and a strap of story, region and picture counts |
| top band | five picture cards — COP31 running into overtime, Iran hitting three tankers near Hormuz, BepiColombo at Mercury, the missile strike on Kryvyi Rih, the Bayelsa funeral boat |
| briefs | eighteen one-line stories in two columns, each carrying a region code |
| bottom band | four picture cards — France's sixth weekend of cost protests, the M6.7 Peru quake, the Sinaloa cartel boss held, Cyclone Xavier weakening |
| date check | `LEFT OUT` (before the day), `NOT YET` (after it), `ALSO ON 21 NOV` (began earlier) |

Every story is one that happened, or was first reported, on 21 November 2026 in
some time zone. Items from the 20th or earlier, and anything after the 21st,
are named in the date-check ledger instead of being drawn as the day's news.
Where an event began before midnight, the deck says so — the Kryvyi Rih strike
was Friday night, the Nigerian boat capsized on Friday, and the cartel boss was
held on Friday and flown out on Saturday.

## Reading aids

Two devices exist so the page can be read without memorising anything:

- **Region codes.** Every brief opens with a filled badge carrying a three
  letter code — `EUR`, `MEA`, `ASI`, `AFR`, `AME`, `OCE`, `GLO` — in the
  region's own colour. The legend at the head of the column reads `CODE = REGION`.
- **Day and time badges.** Every picture panel carries a small solid chip in its
  top-left corner. It holds a clock only where a source gives one (`18:24Z` for
  the BepiColombo burn, `00:09Z` for the Peru quake's origin time) and the day
  the event began otherwise (`FRI` for the three stories the ledger marks as
  having begun on Friday, `SAT` for the rest). No hour is printed that no
  source states.

## Files

| file | role |
| --- | --- |
| `main.py` | the entry point: copies the finished `entry.png` into the output directory |
| `render.py` | the layout — bands, type, region codes, day badges, the date-check ledger, and the colour audit |
| `art.py` | the drawing library and the nine panels |
| `newsdata.py` | the day's stories, sources, verified times, and the date-check lists |
| `fonts/` | Poppins Bold, SemiBold and Medium |

## Running it

The image is pre-rendered and committed, so the entry itself needs nothing but
the standard library:

```sh
mkdir -p out && python3 main.py out      # writes out/entry.png
```

To redraw the page from source you need Pillow:

```sh
python3 render.py entry.png              # prints the colour audit
```

`render.py` refuses to draw if the computed layout would overlap itself, and
prints the colour share of the page and of both picture bands. Two runs of it
write byte-identical files.

## Licence

MIT — see `LICENSE`.
