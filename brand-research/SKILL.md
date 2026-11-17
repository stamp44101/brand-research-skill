---
name: brand-research
description: Competitor brand research ("สืบแบรนด์") — website/platform, traffic, countries, channels, active FB ads, socials, stockists, best-sellers, ownership/origin — delivered as a dense Canva whiteboard (a copy of the team's research board), a PDF, and bullet key takeaways per brand. Use when the user names one or more brands/shops and says สืบ / research / หาข้อมูลแบรนด์, or attaches a research example board.
version: 0.1
---

# Brand research skill — v0.1

> **v0.1:** tested on 1 run (2 Vietnamese fashion brands). See `TESTS.md`.

The bar is **a board as dense as the one the team makes by hand**: many real screenshots per brand, each with a short label. Numbers-only cards are a fallback, never the main content. Facts only, short labels, no strategy advice unless asked. Reply in the user's language (casual Thai by default) with English technical terms.

## 1. Collect (per brand)

Post a one-line progress update every few steps.

| What | How |
|---|---|
| Identify brand + all sites | Web search `"<brand>" official`. Check the IG bio link: brands often have a **separate global site** (e.g. `global.<brand>.com`) |
| Platform, company, socials, pixels | `python -I scripts/probe.py <url> [<global url>]`. The footer often has the company name, registration/tax no. and legal representative |
| Shopify stats (Shopdora-style, free) | `python -I scripts/shopify_stats.py <domain>` → item count, price range/median, store start (oldest product), sold-out %, top-10 best-sellers |
| Traffic, countries, channels, keywords | `similarweb.com/website/<domain>/` in Chrome, read via JS `innerText`. The free quota is small: if "search limit" appears, ask the user for their own Similarweb screenshots. Don't sign up for accounts |
| Active FB ads | Meta Ad Library: search the brand → open its page with "Active" status. Count ads in English vs the local language (diacritics) and note the CTA ("Send message" = sales close in chat) |
| Ownership / origin | Ad Library → page → **About** (Page transparency: managing organisation, admin countries, page creation date, follower counts). National business registry (VN: masothue.com by tax no.). Founder's public profile |
| Socials | IG, TikTok, FB profile screenshots (followers, posts, bio links). **Never solve a captcha.** If one appears, read the numbers behind it and move on |
| Distribution | Search stockists (`"<brand>" collection`), Shopee / Lazada / TikTok Shop. Check each stockist's country (Shopify.country / currency) |

Screenshots: Chrome screenshot saved to disk at full size. Heavy pages can freeze capture: retry once, or use Playwright headless for sites that don't block bots (brand sites and the Ad Library work; Similarweb blocks bots).

**Minimum caps per brand:** homepage(s) · Ad Library results · Similarweb (if quota) · IG · TikTok · best-seller page · each stockist page.

## 2. Board (Canva)

1. Open the board link → **File → Make a copy**. Never edit the original. If the copy's tab drops out of the browser tab group, reopen its URL.
2. Upload: Uploads panel → file input → upload **one file at a time**, so the newest thumbnail is known. Drag the first thumbnail onto empty canvas.
3. Size and place exactly: select → **Position** → Width, Height (Ratio is unlocked, so set both), X, Y.
4. Layout (canvas px, to the right of existing content): per brand a block about 2,600 px wide.
   - Column A: homepage 1200×750, Ad Library 1200×917 below it.
   - Column B: summary text (font 28, left-aligned, width 1380), then the data card (1300 wide).
   - Below both: the other screenshots (or one labelled collage 2580 wide).
5. Text: press `t` → type → Escape → set the font size while the box is selected (not in edit mode). The align button cycles center → right → justify → left.
6. Zoom to Fit, take a screenshot, send it with the copy link.

Template: `templates/data_cards.html` (traffic / countries / channels / store / best-sellers / social). Fill the fields and render the card with Playwright.

## 3. Deliverables

- **PDF:** one 1440×810 page per brand (screenshots + data card) plus a comparison page.
- **Canva copy:** link + overview screenshot.
- **Key takeaways** (when asked): English at a general reading level, **one message per brand**, short bold headings with 2–4 short bullets each: Origin · Market · Sales · Marketing · Distribution · Products · Size. One italic source line at the end. For origin, state only what was found.
- Explain jargon in plain words when writing in Thai (e.g. "organic 100%" = everyone who came from Google searched the name; no Google Ads).

## Known gaps

- Similarweb free quota runs out after a few lookups; the data card replaces the real charts until the user sends screenshots.
- Shopify stats need a Shopify store. Other platforms (Haravan, WooCommerce…) only get `probe.py`.
- TikTok often shows a captcha to automated browsers.

## Appendix: scripts

`scripts/probe.py` and `scripts/shopify_stats.py` are in this folder. Both use only the Python standard library.
