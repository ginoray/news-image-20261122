[![Competition badge](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122)
[![Rank badge](https://make.fun/badge/news-image-20261122/ginoray/news-image-20261122/rank.svg)](https://make.fun/bounty/news-image-20261122)
[![Reward badge](https://make.fun/badge/news-image-20261122/ginoray/news-image-20261122/reward.svg)](https://make.fun/bounty/news-image-20261122)

# The World Today — Sunday, 22 November 2026

A make.fun [news-image-20261122](https://make.fun/bounty/news-image-20261122)
entry: one newspaper-style poster image that sums up the world's news of
Sunday 22 November 2026.

## What the program does

`main.py` (Python 3, standard library only) decodes the sealed poster stored
in `assets/entry.png.b64`, verifies the PNG signature, and writes it
atomically to `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output/entry.png`).
It runs offline and writes the same bytes on every run.

## The poster

A front-page layout with seven stories, each cross-checked in at least two
independent reports published on the day:

1. **COP31 climate talks collapse in Antalya** — the UN summit ended Sunday
   with no agreement after the EU and vulnerable countries rejected a closing
   draft that never mentioned fossil fuels. (AP, Reuters)
2. **Russian drone hits flats near Kyiv** — an apartment block in Dymer was
   struck on Sunday morning; 2 dead and 14 people feared trapped. (Reuters, AP)
3. **Drone strike sets Russian ship ablaze at Benghazi** — an explosion tore
   through a Russian vessel docked at the Libyan naval base. (Reuters, Euronews)
4. **Democrats reach 258 House seats** — the biggest US House majority since
   1992, sealed by a North Carolina recount win. (AP, Reuters)
5. **Candy factory fire in Banten, Indonesia** — 3 workers dead and 37
   unaccounted for as rescuers searched the ruins. (AP, Reuters)
6. **Cartel boss "El Chapo Isidro" captured in Sinaloa** — Mexican special
   forces seized Fausto Isidro Meza Flores; 11 died in the raid. (Reuters, Al Jazeera)
7. **Markets brace for more AI sell-off pain** — Asian authorities readied
   support measures as US futures bounced. (Reuters, One Turn News)

## Rebuilding the poster

The poster was drawn at build time with Pillow:

```sh
python3 tools/render.py   # writes entry.png next to the repo root copy
```

`tools/build_image.py` holds the drawing code; `tools/render.py` renders the
PNG and seals it as a single-line base64 asset under `assets/`.
