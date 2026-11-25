# Working on pathwayanalytics.com

Instructions for anyone changing this website: people, Claude, Gemini, Copilot and other AI assistants. Read this before changing a page, a style or a graphic.

## How the site works

- This is a Docsify site. Each page is a Markdown file; `index.html` is the template for every page.
- **The `main` branch is the live website.** Anything merged into `main` goes live. Work on a branch and open a pull request. Only merge when the site owner has approved it.
- After changing pages, run `node infra/gen-pages.mjs` (needs `marked@18`) and `./infra/gen-search-paths.sh`. The "Generate pages" workflow also runs them on `main`.

## Design system: v1.0, frozen

All styling follows the **Website Design System v1.0**: [`style-guide/README.md`](style-guide/README.md). It is frozen. New pages and case studies use it as it stands; they do not restyle the site.

- Colours, fonts, spacing and widths come from the design tokens in `assets/css/custom.css`, section 1. Use the `--pa-*` variables. Do not write new colour values into rules, add near-duplicate colours, or add another stylesheet.
- A change to the design system itself goes in its own pull request, never inside a content change. Change the tokens, the guide and the gallery together.
- Technical notes: [`style-guide/_implementation.md`](style-guide/_implementation.md).

## Graphics

- Every website graphic is drawn by `infra/graphics/pwa_graphics.py`, using the shared rules in `infra/graphics/pwa_style.py`.
- Each case study has its own set in `infra/graphics/sets/`, so case studies can be drawn independently. Start a new set by copying `sets/tariff.py`.
- Each graphic has a desktop version (720 wide) and a phone version (360 wide).
- Text is Arial and colours come from the house palette only. Steps are solid dots; one gold dot marks the highlight. No rings, glows or gradients, and timelines are straight.
- Put each graphic in the page as a pair of images with class `cs-fig cs-fig-wide` and `cs-fig cs-fig-narrow`, and add it to `style-guide/vector-gallery.html` under its family.
- Check both versions at full size and at 390px, in light and dark mode.

## Publishing a case study

Each case study is its own branch and pull request, independent of the others.

1. Create `case-studies/<slug>.md`. Model it on `case-studies/sexual-health-tariff.md`:
   - a meta block (description, image, image_alt)
   - the `cs-*` page elements: `cs-rule`, `cs-tags`, `cs-project`, `cs-standfirst`, `cs-stats`, `cs-overview`, `cs-contents`, `cs-related`, and `figure-caption` for captions
2. Order of content:
   - the problem
   - Pathway Analytics' role
   - the approach
   - the work delivered
   - the impact or wider relevance
   - sources
3. Draw its graphics in `infra/graphics/sets/<slug>.py`. Run `python3 infra/graphics/pwa_graphics.py <slug>`.
4. Add a 1200 × 627 PNG sharing image to `assets/images/og/`.
5. Add the case study to the list in `case-studies/README.md`.
6. Regenerate pages and search, check desktop and phone in light and dark, then open the pull request.

## Writing

- British English, plain and evidence-led. No em dashes. Few uses of "we". No consultancy clichés or AI-style repetition. No full stops in headings.
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
