<!-- meta
description: The Pathway Analytics website design system: colours, type, editorial pages, figures, captions, charts and writing rules for every page.
-->

# Website design system

Version 1.2, November 2026, frozen. One set of rules for every page and graphic on pathwayanalytics.com, for anyone who edits the site: people, AI assistants and developers. The values are set once, in the design tokens at the top of [`assets/css/custom.css`](https://github.com/Pathway-Analytics/docs/blob/main/assets/css/custom.css). Every reusable graphic is in the [vector gallery](/style-guide/vector-gallery.html ':ignore').

Version 1.2 refines version 1.0. It is not a rebrand: the logo, colours, typefaces, navigation, site structure and approved case study content are unchanged. It adds editorial rules for case studies and their figures: reading size and line length, figure type, journal-style captions and source notes, one numbering treatment, and a list of what to avoid. The illustrated reference is the [Website Design Guide v1.2](https://github.com/Pathway-Analytics/docs/blob/main/style-guide/PWA_Website_Design_Guide_v1.2.pdf) (PDF). Version 1.0 is kept for the record in [`style-guide/_v1.0.md`](https://github.com/Pathway-Analytics/docs/blob/main/style-guide/_v1.0.md).

The PDF was made with a substitute serif because Playfair Display was not available to the tool that produced it. The website typeface is Playfair Display.

Version 1.2 is the default for every new page and case study. A change to the design system itself is made in its own pull request, updating the tokens, this guide and the gallery together.

## Principles

Evidence-led. Commercially grounded. Patient-centred. The site should read as an established specialist consultancy with the substance of its strategy, health economics and digital work: not a technology landing page, and not a purely academic publication.

- The work provides the visual interest: original content, figures that explain it, white space and fine dividing lines.
- Editorial pages read like a well-edited report. Functional pages look and work like software. One identity, two treatments: see [Editorial pages and functional tools](#editorial-pages-and-functional-tools).
- Change as little as possible. Use the tokens; do not add near-duplicate colours or one-off styles for a single page.

## Logo

The master logo is the two-colour Pathway Analytics logo: "Pathway" in navy over "ANALYTICS" in spaced teal capitals.

- Use the supplied files in `assets/images/brand/`: `logo-on-light.png` on white, `logo-on-dark.png` in dark mode.
- Keep using the PNG files until a faithful vector version exists; that will replace `wordmark-on-light.svg`.
- Do not redraw, retype, recolour or stretch the logo, or swap in the single-colour wordmark. Keep its clear space and proportions.
- The spaced capitals belong to the logo only.

## Colours

Navy and teal come from the logo; gold is the accent. Each brand colour stands for one discipline.

| Role | Colour | Use |
| --- | --- | --- |
| Strategy | Navy `#14335A` | Headings, main lines, primary buttons |
| Health Economics | Teal `#518386` | Lines and markers |
| Digital Solutions | Gold `#C9A24A` | Lines, markers, the one highlight in a graphic |
| Navy text | `#14335A` | Text on light backgrounds |
| Teal text | `#3F6B6E` | Teal text, and teal fills behind white text |
| Gold text | `#7A5C1A` | Gold text, and editorial numbering and dates. Never set text in `#C9A24A`: it is too light to read |
| Body text | `#1F2933` | Running text |
| Secondary text | `#5F6B7A` | Captions, notes, labels |
| Dividers | `#E3E6EA` | Rules and borders |
| Pale panels | `#F4F6F8` | Panels, table stripes, code |
| Background | `#FFFFFF` | Page and figure canvas |

- Brand colours identify disciplines when they are used to mean a discipline. Analytical colours carry data: see [Charts](#charts).
- Use colour sparingly. Never alternate colours for variety: a change of colour implies a difference in meaning.
- Dark gold is the one colour for editorial numbering and dates. Used that way it identifies no discipline.
- Patient advocacy has no colour of its own: it is shown by the patient at the centre of the signature graphic.

## Dark mode

Dark mode is a dark interface around light figures.

| Role | Dark value |
| --- | --- |
| Page | `#111827` |
| Dark panel | `#172033` |
| Light text | `#E8EEF8` |
| Secondary text | `#CBD5E1` |
| Links and navy text | `#9DB8DD` |
| Teal text | `#8CC2C4` |
| Gold text, numerals and dates | `#E0C07A` |
| Primary buttons | `#E8EEF8` with `#111827` text |
| Focus ring | `#8CC2C4` |

- HTML editorial figures, such as numbered sequences and the case study index, sit on the page background in both modes, in the dark mode text colours.
- Analytical graphics (SVG files) keep their white canvas, with 16px padding, so one file works on the page, in dark mode and in Word and PowerPoint. The canvas grows outwards by its padding, so the drawing and its labels keep their size.
- Text inside the canvas stays dark. Never set light text on the light canvas.
- Headings, captions and source notes sit outside the canvas, in the dark mode text colours.
- Every text colour above meets WCAG AA (4.5:1) on both the page and the dark panel.

## Type

Typography sets the hierarchy. A figure supports the argument, so its text is smaller than the prose around it, without going below the minimums.

| Role | Size as shown | Typeface |
| --- | --- | --- |
| Running text, case studies | 17px, line height 1.6 | Inter 400 |
| Running text, other pages | 16px, line height 1.7 | Inter 400 |
| Page titles and editorial headlines | Existing title sizes | Playfair Display 400, used selectively |
| Section headings | Existing sizes | Inter 600 to 700 |
| Figure heading | 15px | Inter 600 |
| Figure caption and explanation | 14px | Inter 400 |
| Labels inside graphics | 13px minimum, as rendered | Arial, Helvetica, sans-serif |
| Source and provenance notes | 13px (never below 12px) | Inter 400 |
| Step numerals, dates and headline figures | Set by context | Playfair Display 400; old-style figures for numerals and dates |

- On case study pages, running text is about 68 characters a line (578px). Figures may run wider, to 800px.
- Inter in HTML and in graphics drawn in the page. Arial, Helvetica, sans-serif in SVG files, so they render the same in browsers and Office.
- Measure type at the size it is shown. An SVG drawn 720 wide and shown 800 wide makes its 12px labels 13.3px; shown 1,200 wide it would make them 20px, larger than the prose. That is why figures have a maximum width.
- Sentence case for headings, labels and buttons. No full stops in headings. No letter-spaced capitals, apart from the logo.
- One title (H1) per page; H2 for sections, H3 and H4 below them.

## Layout and components

- Spacing comes from the 8px scale in the tokens: 8, 16, 24, 32, 48, 80.
- Corners are small (4px) or square. Dividers are 1px `#E3E6EA`.
- Links in running text are underlined, so they never depend on colour alone.
- Buttons: navy with white text; in dark mode, light with dark text.
- Tags and labels: sentence case, in the discipline's text colour or the secondary text colour. No filled pills.
- Every page works at 390px wide with nothing scrolling sideways, and at 200% browser zoom.

## Editorial pages and functional tools

The site has one visual identity and two treatments.

**Editorial pages** are the case studies and the case study index. Insight articles follow when they are next revised. They use the editorial layout (`page-editorial`): 17px prose at about 68 characters a line, figures to 800px, numbered figures with captions and sources, and the editorial sequence for processes and chronologies. The index is a contents list: years and disciplines in the margin, the title, one line and a verified finding where there is one.

**Functional pages** are the Tariff Grouper guidance, the Health Economics Toolkit and any calculator. They keep their interface styles. Purposeful panels, inputs, controls, tables and primary product actions are allowed: the editorial exclusions below are not a ban on usable software. In a calculator, keep inputs and results clearly separate and label illustrative figures as illustrative.

**The home page** keeps its architecture. The Tariff Grouper and the Health Economics Toolkit stay as the primary actions in the hero. A dated, cleared case study lead may sit beside them, never in place of them.

## Figures

Figures explain the substance of the work; they never decorate. A figure has four parts: a short heading, the drawing, a numbered caption and a source note.

```html
<figure class="pa-figure">
<p class="pa-figure-title">From pathway to price</p>
<img class="cs-fig cs-fig-wide" src="/assets/images/case-studies/NAME.svg" alt="What it shows">
<img class="cs-fig cs-fig-narrow" src="/assets/images/case-studies/NAME-mobile.svg" alt="What it shows">
<figcaption><span class="pa-fig-num">Figure 2.</span> What the reader should take from it. <span class="pa-source">Source: Pathway Analytics schematic.</span></figcaption>
</figure>
```

- Number figures in the order they appear on the page.
- The caption says what the figure shows and anything needed to read it: units, period, denominator, comparator, and whether figures are illustrative, modelled or observed.
- Every figure has a source note: a published source that has been cleared, or "Pathway Analytics schematic" for a diagram of a method or idea.
- Keep the figure block together, with no blank lines inside it, so the page renders it as one piece.

### Reference figure: the editorial sequence

This is the preferred model for processes, methods and chronologies, and the visual reference for future editorial figures. It is built in HTML, so it uses the site's own fonts, reflows on a phone and follows dark mode.

<figure class="pa-figure">
<p class="pa-figure-title pa-serif">The Pathway Analytics approach</p>
<ol class="pa-steps">
<li><p class="pa-step-title">Challenge the assumptions</p><p class="pa-step-text">Establish whether the problem is correctly understood.</p></li>
<li><p class="pa-step-title">Build the evidence</p><p class="pa-step-text">Understand patient needs, clinical pathways, activity and resources.</p></li>
<li><p class="pa-step-title">Understand the economics</p><p class="pa-step-text">Distinguish funding, expenditure, costs and incentives.</p></li>
<li><p class="pa-step-title">Develop practical solutions</p><p class="pa-step-text">Assess strategic options and the operational implications.</p></li>
<li><p class="pa-step-title">Build analytical tools</p><p class="pa-step-text">Translate the methodology into usable decision-support models.</p></li>
</ol>
<figcaption><span class="pa-fig-num">Figure 1.</span> The Pathway Analytics approach to healthcare system design. <span class="pa-source">Source: Pathway Analytics methodology.</span></figcaption>
</figure>

- An understated serif title, not a promotional headline.
- Margin numerals in Playfair Display, dark gold, one treatment for every step. No filled squares, badges or arrows, and no alternating colours.
- Semibold step titles, regular explanatory text, fine rules that start at the text column, modest white space. No enclosing card.
- For a chronology, put the date in the margin instead of the number (`<ol class="pa-steps pa-dated">` with `<span class="pa-step-date">`).

### Graphics (SVG files)

- Every graphic belongs to a family in the [vector gallery](/style-guide/vector-gallery.html ':ignore'): convergence, pathways and processes, cost and funding, matrices, or timelines. New families are added only when a real case study needs one.
- Text in Arial; colours from the brand and neutral lists above, nothing else.
- A desktop version 720 wide and a phone version 360 wide. The page switches between them at 700px. Reflow a phone version; never shrink the desktop drawing to fit a phone.
- Labels at least 13px as rendered: 12 units in a desktop drawing and 13 units in a phone drawing.
- Keep text inside a graphic to labels. Titles, explanations and sources go in the figure heading, caption and source note on the page.
- Steps and points are solid dots. One gold dot marks the point to look at. No rings, halos, glows, shadows, gradients or icons.
- Solid lines are what happens or is paid for; dashed lines are what is not paid for, not counted, or continues.
- Meaning never relies on colour alone: label it, or use line style or position as well.
- Facts and wording match the page the graphic appears on.
- Alt text says what the graphic shows, not what it looks like.

### What each family shows

| Family | Use it for | Rule |
| --- | --- | --- |
| Convergence | Several streams working towards one aim | Do not imply causes the evidence does not support |
| Pathways and processes | Real sequences, dependencies and boundaries | Label arrows only where it helps |
| Cost and funding | Amounts, prices and who pays | A common scale and a zero baseline; keep payment flows separate from patient flows |
| Matrices | Options or components against criteria | Explicit headings and labels; no invented scores or rankings |
| Timelines | Events in order | Mark schematic spacing as schematic, or use proportional intervals when timing matters |

The signature graphic, three disciplines converging on the patient, is for the home page and sharing images. Do not repeat it elsewhere on the site.

### Evidence conventions

- State units, time period, denominator, comparator and source wherever they apply.
- Say whether a result is hypothetical, modelled or observed.
- No unnecessary gridlines, 3D effects or decorative colour. Label directly where there is room.
- Keep the editable source of every graphic in `infra/graphics/`, and its provenance cleared for publication.

## Charts

Charts use analytical colours, kept separate from the brand colours. Analytical colours say which group or how much; brand colours say which discipline.

**Categorical** (services, interventions, groups), always assigned in this order:

| Order | Colour | Value |
| --- | --- | --- |
| 1 | Blue | `#2F6EA8` |
| 2 | Ochre | `#B08A2E` |
| 3 | Teal | `#008C82` |
| 4 | Rust | `#B85A3F` |
| 5 | Plum | `#7B5EA7` |
| 6 | Green | `#5E8F3E` |

- In this order, neighbouring colours stay distinct for people with red-green colour blindness, and every colour reaches 3:1 on white.
- More than six groups: combine the smallest into "Other", or use small multiples. Never invent a seventh colour.
- Scatter plots and maps, where any two colours can sit side by side: use slots 1 and 2 only, with shapes or labels for anything more.

**Sequential** (ordered measures, from low to high): `#8FABCF`, `#6189BB`, `#3E6AA0`, `#25497C`, `#14335A`.

- Keep a group's colour the same in every figure of a case study.
- Label series directly where there is room; add a legend when there are two or more series.
- Horizontal gridlines only, thin and pale. No chart borders. One vertical axis per chart.
- Status colours (green, amber, red) are kept for good, warning and problem, always with a word.

## What we avoid

On editorial pages and in figures:

- Gradients, shadows, pill badges and icons in circles.
- Filled numeral squares, alternating colours and decorative arrows.
- Repeated grids of three cards, generic centred hero and button pairs, and stock photography.
- Heavy frames and rounded corners: use fine rules, space and near-square corners.
- Emoji, slogans in place of evidence, and unsupported impact claims.

These are editorial rules. Functional panels, inputs, controls and the primary product actions are allowed.

## Accessibility

- Text meets WCAG AA: 4.5:1, or 3:1 for large text. Lines, shapes and controls that carry meaning meet 3:1.
- Links are underlined in running text; the keyboard focus ring is always visible.
- Everything can be reached and used by keyboard.
- Every figure has alt text or an HTML equivalent. Captions and sources are legible and traceable.
- Check each new page on a phone (390px) and a desktop (1280px), in light and dark mode, and at 200% zoom. Check print and greyscale where a figure relies on colour.

## Writing

- British English: plain, restrained and evidence-led. No em dashes.
- Case studies follow the same order: the problem, Pathway Analytics' role, the approach, the work delivered, and the impact or wider relevance.
- Separate what Pathway Analytics did from what the wider programme achieved. Claim only what the evidence shows.
- No unsupported impact claims, consultancy clichés or repetitive AI-style phrasing.
- Name clients and individuals only with permission.

## Changing the design

1. Read this guide, the tokens and the gallery first. Check actual rendered sizes in a browser.
2. Build working previews before changing anything live: desktop and phone, light and dark. Compare designs at the same rendered sizes, widths and zoom.
3. Get approval on the previews. Then change the shared tokens and the reusable figure code, never a one-off style.
4. A design change does not change approved copy, data, links, attribution or method.
5. Before merging, check hierarchy, contrast, zoom, wrapping, captions, links, source clearance and that no private material or metadata is included.

## What belongs in this repository

Everything in this repository can be read by anyone on GitHub, including files kept off the website.

- In: this guide and its PDF, the design tokens, editorial conventions and graphics that are approved for publication.
- Never in: client material, unpublished project files or findings, internal evaluation palettes, private analysis, or the Word and PowerPoint house styles.
- This guide is a public page. The vector gallery can be reached by its address but is not in the menu, search or sitemap. Technical notes are in `_implementation.md`, which the site does not publish as a page.

## Versions

| Version | Date | What changed | Status |
| --- | --- | --- | --- |
| 1.2 | November 2026 | Editorial pages, figure type, captions and sources, the editorial sequence, exclusions, the editorial and functional distinction | Current, frozen |
| 1.1 | November 2026 | A boxed visual treatment, proposed and not merged | Superseded |
| 1.0 | November 2026 | Tokens, colours, dark mode, graphics rules, chart colours, vector gallery | Kept in `_v1.0.md` |
