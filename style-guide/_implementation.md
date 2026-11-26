# Design system: implementation notes

Technical notes for whoever edits the site. Not a website page: the page generator and the search builder both skip files whose names start with an underscore. It is still public on GitHub, like everything in this repository.

The rules are in [README.md](README.md). This file covers where they live, how to add graphics, and what is still to change.

## Where everything lives

| What | Where | Public web page? |
| --- | --- | --- |
| Design system guide | `style-guide/README.md` | Yes, `/style-guide/`, in the sitemap and search, not in the menu |
| Illustrated reference (v1.2) | `style-guide/PWA_Website_Design_Guide_v1.2.pdf` | No: a file on GitHub, linked from the guide |
| Version 1.0 guide, kept for the record | `style-guide/_v1.0.md` | No |
| Design tokens | `assets/css/custom.css`, section 1: the `:root` block and the `html[data-theme="dark"]` block | No: the stylesheet |
| Vector gallery | `style-guide/vector-gallery.html` | Reachable at `/style-guide/vector-gallery.html`; not in the menu, search or sitemap; `noindex` |
| These notes | `style-guide/_implementation.md` | No |
| Graphics | `infra/graphics/`: `pwa_graphics.py` draws them, `pwa_style.py` holds the shared rules, `sets/` has one file per case study | No |
| Instructions for people and AI assistants working on the site | `AGENTS.md` (and `CLAUDE.md`, which points to it) at the repository root | No: excluded from pages and search |
| Case study figures | `assets/images/case-studies/` | Shown on case study pages |
| Reusable graphics that are not case study figures | `assets/images/dictionary/` | No |
| Logo | `assets/images/brand/` | Used across the site |

Do not add a separate `styles/` folder. The site loads only `assets/css/custom.css`, and adding another stylesheet means editing `index.html`, the template for every page.

## Tokens

The tokens keep the variable names the stylesheet already used (`--pa-*`), so existing rules pick up the new values without being rewritten. New tokens:

- Brand: `--pa-navy`, `--pa-teal`, `--pa-gold`, and text versions `--pa-navy-text`, `--pa-teal-text`, `--pa-gold-text`, which change in dark mode.
- Interface: `--pa-on-primary` (text on primary buttons), `--pa-focus` (focus ring), `--pa-border-control` (form field edges).
- Figures: `--pa-figure-panel`, `--pa-figure-pad`. Images with class `cs-fig` or `pa-figure` get a white panel in dark mode.
- Charts: `--pa-cat-1` to `--pa-cat-6`, `--pa-seq-1` to `--pa-seq-5`.
- Type: `--font-display` (Playfair Display), `--font-graphic` (Arial).
- v1.2 editorial layout: `--pa-prose-size` (17px), `--pa-prose-line` (1.6), `--pa-measure` (578px, about 68 characters), `--pa-editorial-width` (800px).
- v1.2 figure type: `--pa-fig-heading` (15px), `--pa-fig-text` (14px), `--pa-source-size` (13px), `--pa-fig-label-min` (13px, for reference).
- v1.2 numbering: `--pa-numeral`, the gold text colour, for step numerals, dates and the index years.

Values that changed: primary from the old blue `#1F4788` to navy; links from bright blue `#2563EB` to navy, underlined in running text; dark mode primary from bright blue to `#E8EEF8`; dark panel `#172033`; body text `#1F2933`; secondary text `#5F6B7A`; dividers `#E3E6EA`; corners from 6px and 8px to 4px.

## Version 1.2: editorial pages and figures

The v1.2 styles are in `assets/css/custom.css`, section 17. Nothing in v1.0 was removed; a few values changed (listed below).

| Class | What it is |
| --- | --- |
| `body.page-editorial` | Added by the article layout plugin in `index.html` to every `/case-studies/` page, including the index. Sets 17px prose, the 68-character measure and the 800px column |
| `figure.pa-figure` | A figure: fine rules above and below, heading, drawing, caption |
| `.pa-figure-title` | The figure heading, Inter 600. Add `pa-serif` for the understated Playfair title of an editorial sequence |
| `figcaption`, `.pa-fig-num`, `.pa-source` | The caption, its "Figure n." and the source note, all inside `figcaption` (a `figcaption` must be the first or last child of its figure) |
| `ol.pa-steps` | The editorial sequence: counter numerals in the margin. `pa-dated` with `.pa-step-date` puts a date there instead |
| `ol.pa-index` | The case study index: `.pa-index-meta` holding `.pa-index-years` and `.pa-index-tags` (one span per discipline, no separators: the CSS adds them on phones), `h2.pa-index-title`, `.pa-index-text`, `.pa-index-finding` |
| `.home-latest` | A dated case study lead under the home page product buttons |

Existing styles changed in v1.2:

- `.figure-caption` is left-aligned at 14px in the secondary text colour (was centred at 0.82em).
- The home page client band, product buttons and resource links use 4px or square corners (were 12px, 6px and 10px); the resource links are columns under a fine rule, not bordered cards.
- The home page "Five questions" numerals use the editorial treatment: Playfair Display 400, old-style figures, dark gold (were bold teal).
- In dark mode, a figure's white canvas grows outwards by its 16px padding, so the drawing keeps its width.

To bring a case study up to v1.2:

1. Wrap each graphic, its caption and its source in a `<figure class="pa-figure">`, with a short heading, numbered in page order. Keep each figure block free of blank lines.
2. Replace a process or chronology drawn as text in an SVG with an `ol.pa-steps` sequence, keeping the same wording.
3. Add `DESIGN_SYSTEM = '1.2'` to the page's graphics set, redraw it, and run the label check: no label clipped or overlapping, none below the floors.
4. Check the page at 1280px and 390px, light and dark, and at 200% zoom.

## Graphics

All website graphics are drawn from the same rules, in `infra/graphics/pwa_style.py`: colours, font and shapes. Each case study has its own set in `infra/graphics/sets/` (`tariff.py`, `signature.py`), so case studies can be drawn and published independently.

1. For a new case study, copy `sets/tariff.py` to `sets/<slug>.py`. Use the helpers and colour constants only, and draw a desktop version (720 wide) and a phone version (360 wide) of each graphic.
2. Run `python3 infra/graphics/pwa_graphics.py <slug>` from the repository root. It writes that set's SVG files. With no name, it draws every set.
   A set with `DESIGN_SYSTEM = '1.2'` is drawn with the v1.2 label floors: no font size below 12 units in a desktop drawing or 13 units in a phone drawing, so every label is at least 13px on screen. Sets without it are drawn to v1.0 sizes, unchanged, until they are brought up to v1.2.
3. Check both versions at full size for overlapping or clipped labels, and the phone version at 390px.
4. Put the graphic on the page as a pair of images inside a figure:
   ```html
   <figure class="pa-figure">
   <p class="pa-figure-title">Heading</p>
   <img class="cs-fig cs-fig-wide" src="/assets/images/case-studies/NAME.svg" alt="What it shows">
   <img class="cs-fig cs-fig-narrow" src="/assets/images/case-studies/NAME-mobile.svg" alt="What it shows">
   <figcaption><span class="pa-fig-num">Figure 1.</span> Caption. <span class="pa-source">Source: ...</span></figcaption>
   </figure>
   ```
5. Add an `<article>` for it in the gallery, in its family.

Before any graphic goes into this repository, check its facts and wording against the published page, and that the work it describes is cleared for publication.

### Changes made to the reconstructed gallery for v1.0

The seven graphics in the reconstructed `pathway_analytics_vectors.html` were redrawn with the script:

- Playfair Display and Inter replaced by Arial; slate greys (`#475569`, `#CBD5E1`, `#E2E8F0`, `#F1F5F9`, `#F8FAFC`) replaced by the house neutrals.
- Gold rings and halos replaced by a single solid gold dot; the patient hub is a plain circle.
- The timeline's rising curve replaced by a straight line.
- "Redrawn from…" notes removed from the graphics and the case study captions.
- Wording brought into line with the published case study and home page. Three phrases that the published pages do not support were left out: "Integrated tariff and service specification", "Co-designed across clinical and finance leads", and "No identifiers" (the case study says no *direct* patient identifiers leave the provider).
- The governance graphic is the version on the case study page.
- Every graphic now has a phone version, and a white panel in dark mode.

## Chart colours: how they were checked

The categorical order was found by testing every order of six candidate colour families, with blue first, and keeping the one with the widest separation between neighbours. Each colour was checked for:

- lightness: OKLCH L between 0.43 and 0.78
- colourfulness: chroma at least 0.10, so it does not read as grey
- colour-blind separation between neighbours: worst ΔE 10.5 (OKLab ×100), under protanopia and deuteranopia simulated with the Machado 2009 model
- separation for normal vision: worst ΔE 18.4
- contrast: at least 3:1 on white

On the pale panel `#F4F6F8`, ochre falls to 2.97:1, so charts sit on white. In scatter plots and maps any two colours can touch; there, only slots 1 and 2 stay distinct enough, which is why the guide limits those charts to two colours. The sequential ramp is one hue, gets steadily darker, and its lightest step is 2.4:1 on white.

## Status: v1.2

Version 1.2 is the frozen standard. Applied so far: the tokens, editorial layout and figure styles; the sexual health tariff case study (figures numbered with captions and sources, the timeline as a dated sequence, graphics redrawn with the label floors); the case study index; the home page refinements.

Still to bring up to v1.2, each when its page is next revised:

- **Sexual assault services case study:** number the figures and add sources; add `DESIGN_SYSTEM = '1.2'` to its set. Two phone graphics need small layout changes first: at the floor, the level names collide in `sas-cost-by-need-mobile` and "12 and under" runs off `sas-needs-over-time-mobile`.
- **Fast-Track Cities London case study:** phone versions of three graphics (`ftc-synthesis`, `ftc-cascade-2030`, `ftc-funding-gaps` use the desktop file on phones, so their labels are about 6px), a graphics set in `infra/graphics/sets/`, gallery entries, numbered figures and sources. Labels in `ftc-funding-gaps` go down to 10 units; the cascade uses filled chevrons.
- **Insight article, What is health economics for?:** the "How split budgets can turn into unequal health" chain is a boxed sequence with arrows; redraw it as an `ol.pa-steps` sequence. Then add `/insights/` articles to the editorial layout.
- **`assets/images/case-studies/tariff-approach.svg`:** a boxed five-step graphic used on no page. Superseded; do not use it as a template.
- **The v1.2 PDF:** its dark-mode specimen on page 7 sets the figure title in light text on the light canvas. The rule is the opposite: text inside the canvas stays dark.

## Status: v1.0 implemented and frozen

Implemented in November 2026 (pull request #5):

- The tokens are applied across the stylesheet. Brand colours that were written out in full now use the tokens, so text follows dark mode.
- The old blue `#1F4788`, the bright link blues and the extra golds and teals are gone from the stylesheet.
- Spaced capitals have been removed from every label style, and page titles use Playfair Display.
- Every page checked passed WCAG AA text contrast at 1280px and 390px, in light and dark mode, with nothing scrolling sideways on a phone: the home page, the tariff case study, this guide, an insight article, the Health Economics Toolkit and the Tariff Grouper pages.

Exceptions kept on purpose:

- **Home page signature graphic (`.pg-*`):** drawn in the page, not as an image file, so it follows dark mode instead of sitting on a white panel. Its gold ring is switched off. The image-file version is `assets/images/dictionary/convergence.svg`.
- **Logo files:** the square mark `pa-mark.svg` and the SVG wordmarks still use `#1F4788`. They are left alone until a faithful vector of the master logo exists.
- **Colours still written out in full:** for example, light text `#E8EEF8` on the navy "work with us" panel, which stays navy in both modes.
- **The `cs-held` style:** draft-only, for marking text waiting for clearance; it never appears on a published page.
- **The interactive calculator:** a separate prototype, not yet on the site. When it is added, its form fields use `--pa-border-control`.

Still to come:

- Graphics for further case studies, drawn as their own sets and added to the gallery.
- Further refinements, made one at a time as new content needs them.

The version 1.0 guide is kept in `style-guide/_v1.0.md`. The guide before that (Roboto, the old blue palette, examples of callouts, navigation cards and code blocks) is in the git history: `git show 84e9618:style-guide/README.md`.
