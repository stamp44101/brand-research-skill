# Brand research skill (v0.1)

A Claude skill for competitor brand research ("สืบแบรนด์"). Give it brand names and it collects:
- website and platform, company and owner
- traffic, top countries, traffic sources
- active Facebook ads (how many, which language, which button)
- Instagram / TikTok / Facebook, the shops that stock the brand, best-sellers and prices

It then adds everything to a copy of the team's Canva research board, makes a PDF, and writes bullet key takeaways for each brand.

> **v0.1:** tested on 1 run (2 brands). See `brand-research/TESTS.md`.

## Install
- **Quickest:** add `brand-research/SKILL.md` as a skill in Claude, plus the `scripts` folder.
- **Full:** download this repo (Code → Download ZIP) and install the `brand-research` folder.

## Before you start
1. Install the **Claude in Chrome** extension. Log in to Canva and Instagram in that Chrome.
2. Have Python 3 with Playwright (`pip install playwright` and `playwright install chromium`) for rendering cards and the PDF.
3. Have the link to the research board you want to continue.

## Use
Say: "สืบ [brand 1], [brand 2]" and paste the board link (or attach an example board).

You get:
- a PDF: one page per brand plus a comparison page
- a copy of the Canva board with the new brands added (the original is not touched)
- key takeaways in English, one message per brand

## Files
- `brand-research/SKILL.md`: the skill (source of truth)
- `brand-research/scripts/`:
  - `probe.py`: platform, company/legal info, socials, apps and pixels of a website
  - `shopify_stats.py`: item count, prices, store start date, sold-out share and best-sellers of a Shopify store
- `brand-research/templates/data_cards.html`: data card template (traffic, countries, channels, store, best-sellers, social)
- `brand-research/TESTS.md`: test log
