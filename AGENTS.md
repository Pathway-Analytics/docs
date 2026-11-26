# Working on pathwayanalytics.com

Instructions for anyone changing this website: people, Claude, Gemini, Copilot and other AI assistants. Read this before changing a page, a style or a graphic.

## How the site works

- This is a Docsify site. Each page is a Markdown file; `index.html` is the template for every page.
- **The `main` branch is the live website.** Anything merged into `main` goes live. Work on a branch and open a pull request. Only merge when the site owner has approved it.
- After changing pages, run `node infra/gen-pages.mjs` (needs `marked@18`) and `./infra/gen-search-paths.sh`. The "Generate pages" workflow also runs them on `main`.

## Design system: v1.2, frozen

All styling follows the **Website Design System v1.2**: [`style-guide/README.md`](style-guide/README.md), illustrated in [`style-guide/PWA_Website_Design_Guide_v1.2.pdf`](style-guide/PWA_Website_Design_Guide_v1.2.pdf). It is frozen. New pages and case studies use it as it stands; they do not restyle the site. Version 1.0 is kept for the record in `style-guide/_v1.0.md`; follow v1.2.

- This is a refinement, not a rebrand. Keep the logo, the brand colours, Playfair Display and Inter, the navigation, the site structure and approved content. The PDF uses a substitute serif for production reasons only; the site's serif is Playfair Display.
- Colours, fonts, spacing and widths come from the design tokens in `assets/css/custom.css`, section 1. Use the `--pa-*` variables. Do not write new colour values into rules, add near-duplicate colours, or add another stylesheet.
- A change to the design system itself goes in its own pull request, never inside a content change. Change the tokens, the guide and the gallery together.
- Technical notes: [`style-guide/_implementation.md`](style-guide/_implementation.md).

### Editorial pages and functional tools

- **Editorial pages** (case studies and the case study index; insight articles when next revised) use the editorial layout: 17px prose, about 68 characters a line, figures to 800px. `index.html` adds `body.page-editorial` on `/case-studies/` pages.
- **Functional pages** (Tariff Grouper guidance, Health Economics Toolkit, calculators) keep their interface styles. Panels, inputs, controls and product buttons are allowed there.
- **Home page:** keep its architecture. The Tariff Grouper and Health Economics Toolkit stay the primary actions in the hero.

### Figures

- Every figure is a `<figure class="pa-figure">`: a short heading (`pa-figure-title`), the drawing or HTML, then `<figcaption>` with `<span class="pa-fig-num">Figure n.</span>`, the caption, and `<span class="pa-source">Source: ...</span>`. Number figures in page order. No blank lines inside the block.
- Sizes as shown on screen: figure heading 15px, caption 14px, source note 13px (never below 12px), labels inside graphics 13px minimum. Figure text is smaller than the prose.
- The preferred reference for processes, methods and chronologies is the editorial sequence, `ol.pa-steps` (dated: `pa-dated`): Playfair numerals in dark gold, semibold step titles, regular text, fine rules, no box. It is shown in the guide and the gallery.
- State units, period, denominator, comparator and source where they apply, and whether figures are illustrative, modelled or observed. Every source must be published or cleared; "Pathway Analytics schematic" for a diagram of a method.

### What to avoid on editorial pages and in figures

Gradients, shadows, pill badges, icons in circles, filled numeral squares, alternating colours, decorative arrows, repeated three-card grids, generic centred hero and button pairs, stock photography, heavy frames, rounded corners, emoji, slogans and unsupported claims. Functional controls are exempt.

## Graphics

- Every website graphic is drawn by `infra/graphics/pwa_graphics.py`, using the shared rules in `infra/graphics/pwa_style.py`.
- Each case study has its own set in `infra/graphics/sets/`, so case studies can be drawn independently. Start a new set by copying `sets/tariff.py`, which is drawn to v1.2 (`DESIGN_SYSTEM = '1.2'`).
- Each graphic has a desktop version (720 wide) and a phone version (360 wide). Reflow the phone version; never shrink the desktop drawing onto a phone.
- Text is Arial and colours come from the house palette only. Keep text inside a graphic to labels; titles, explanations and sources go in the page. Steps are solid dots; one gold dot marks the highlight. No rings, glows or gradients, and timelines are straight.
- Labels: at least 12 units in a desktop drawing and 13 in a phone drawing (13px on screen). The v1.2 sets enforce this; check for clipped or overlapping labels after drawing.
- Put each graphic in a `pa-figure` as a pair of images with class `cs-fig cs-fig-wide` and `cs-fig cs-fig-narrow`, and add it to `style-guide/vector-gallery.html` under its family.

## Before any visual change goes live

1. Read the guide, the tokens and the gallery, and measure actual rendered sizes in a browser.
2. Build working previews: desktop (1280px) and phone (390px), light and dark mode. Compare designs at identical rendered sizes, widths and zoom.
3. Merge only after the site owner approves the previews.
4. Do not change approved copy, data, links, attribution or method in a design change.

## Publishing a case study

Each case study is its own branch and pull request, independent of the others.

1. Create `case-studies/<slug>.md`. Model it on `case-studies/sexual-health-tariff.md`:
   - a meta block (description, image, image_alt)
   - the `cs-*` page elements: `cs-rule`, `cs-tags`, `cs-project`, `cs-standfirst`, `cs-stats`, `cs-overview`, `cs-contents`, `cs-related`
   - figures as `pa-figure` blocks with numbered captions and source notes
2. Order of content:
   - the problem
   - Pathway Analytics' role
   - the approach
   - the work delivered
   - the impact or wider relevance
   - sources
3. Draw its graphics in `infra/graphics/sets/<slug>.py` with `DESIGN_SYSTEM = '1.2'`. Run `python3 infra/graphics/pwa_graphics.py <slug>`.
4. Add a 1200 × 627 PNG sharing image to `assets/images/og/`.
5. Add the case study to the index in `case-studies/README.md`: an `ol.pa-index` entry with its years, disciplines, title, one line and a verified finding where there is one.
6. Regenerate pages and search, check desktop and phone in light and dark, then open the pull request.

## Writing

- British English, plain and evidence-led. No em dashes. Few uses of "we". No consultancy clichés or AI-style repetition. No full stops in headings. Always "Pathway Analytics" on the site, not "PWA".
- Separate what Pathway Analytics did from what the wider programme achieved. Claim only what the sources show, and cite them.
- Name clients and individuals only with permission.
- A graphic and its page must say the same thing.

## This repository is public

Everything here, on every branch, can be read by anyone on GitHub, including files kept off the website.

- Never commit client material, unpublished drafts or findings, artwork that has not been approved, internal evaluation palettes, private analysis, or the Word, PowerPoint and Excel house styles. Keep drafts outside the repository until they are cleared.
- Pages and files are not the same thing. A Markdown file becomes a public page unless:
  - its name starts with `_`, or
  - it is listed in `EXCLUDE` in both `infra/gen-pages.mjs` and `infra/gen-search-paths.sh`.
- This file and `CLAUDE.md` are excluded that way.
