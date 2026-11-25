# Design system: implementation notes

Technical notes for whoever edits the site. Not a website page: the page generator and the search builder both skip files whose names start with an underscore. It is still public on GitHub, like everything in this repository.

The rules are in [README.md](README.md). This file covers where they live, how to add graphics, and what is still to change.

## Where everything lives

| What | Where | Public web page? |
| --- | --- | --- |
| Design system guide | `style-guide/README.md` | Yes, `/style-guide/`, in the sitemap and search, not in the menu |
| Design tokens | `assets/css/custom.css`, section 1: the `:root` block and the `html[data-theme="dark"]` block | No: the stylesheet |
| Vector gallery | `style-guide/vector-gallery.html` | Reachable at `/style-guide/vector-gallery.html`; not in the menu, search or sitemap; `noindex` |
| These notes | `style-guide/_implementation.md` | No |
| Graphics script | `infra/graphics/pwa_graphics.py` | No |
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

Values that changed: primary from the old blue `#1F4788` to navy; links from bright blue `#2563EB` to navy, underlined in running text; dark mode primary from bright blue to `#E8EEF8`; dark panel `#172033`; body text `#1F2933`; secondary text `#5F6B7A`; dividers `#E3E6EA`; corners from 6px and 8px to 4px.

## Graphics

All website graphics come from one script, so they share the same rules.

1. Add or edit a function in `infra/graphics/pwa_graphics.py`, using its helpers and colour constants only. Draw a desktop version (720 wide) and a phone version (360 wide).
2. Run `python3 infra/graphics/pwa_graphics.py` from the repository root. It writes the SVG files.
3. Check both versions at full size for overlapping or clipped labels, and the phone version at 390px.
4. Put the graphic on the page as a pair of images:
   ```html
   <img class="cs-fig cs-fig-wide" src="/assets/images/case-studies/NAME.svg" alt="What it shows">
   <img class="cs-fig cs-fig-narrow" src="/assets/images/case-studies/NAME-mobile.svg" alt="What it shows">
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

## Still to do

The work is in five steps:

1. This pull request: the guide, the tokens, the gallery, and the tariff case study figures redrawn to v1.0.
2. Apply the tokens across the site. The stylesheet still has about 110 colour values written out in full rather than as tokens. The main ones:
   - Home page signature graphic (`.pg-*`): its own colours, a gold ring around the patient, and Playfair inside the graphic. It is drawn in the page, so it follows dark mode; decide whether it keeps that or moves to the figure panel.
   - Venn graphic (`.venn-*`): still uses the old blue `#1F4788` and other golds (`#D9A441`, `#9A6F1F`, `#E8BE6E`, `#ECCA8A`).
   - Dark mode link colours on the home page (`.ex-link`, `.rc-cta`): `#9DC4FB` instead of `#9DB8DD`.
   - Case study classes (`.cs-*`): navy and gold written out in full.
   - Page titles (H1) still use Inter; v1.0 says Playfair Display for major titles.
   - The square mark `pa-mark.svg` and the SVG wordmarks still use `#1F4788`.
   - Form fields in the calculators: check their edges use `--pa-border-control`.
3. Redraw the next case study's graphics with the same script, and add them to the gallery.
4. Check the home page, navigation, case studies, articles, Tariff Grouper pages, Health Economics Toolkit and calculators on desktop and phone, light and dark.
5. List anything left as an exception, and why.

The previous style guide (Roboto, the old blue palette, examples of callouts, navigation cards and code blocks) is in the git history: `git show 84e9618:style-guide/README.md`.
