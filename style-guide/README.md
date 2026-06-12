# Style Guide

This style guide documents the complete design system for the Pathway Analytics documentation site. It serves as a reference for content authors and developers to ensure consistent visual language across all pages.

---

## Colour Palette

The site uses CSS custom properties for all colours, enabling seamless switching between light and dark modes.

### Primary Colours

| Swatch | Name | Hex | CSS Variable | Usage |
|--------|------|-----|--------------|-------|
| ![#1f4788](https://via.placeholder.com/24/1f4788/1f4788) | Primary | `#1f4788` | `--pa-primary` | Brand colour, links, headings, focus indicators |
| ![#0056b3](https://via.placeholder.com/24/0056b3/0056b3) | Primary Hover | `#0056b3` | `--pa-primary-hover` | Link hover states, interactive element hover |

### Accent Colours

| Swatch | Name | Hex | CSS Variable | Usage |
|--------|------|-----|--------------|-------|
| ![#2e86de](https://via.placeholder.com/24/2e86de/2e86de) | Accent 1 | `#2e86de` | `--pa-accent-1` | Blockquote borders, secondary highlights |
| ![#27ae60](https://via.placeholder.com/24/27ae60/27ae60) | Accent 2 | `#27ae60` | `--pa-accent-2` | Success states, positive indicators |

### Text Colours

| Swatch | Name | Hex | CSS Variable | Usage |
|--------|------|-----|--------------|-------|
| ![#333333](https://via.placeholder.com/24/333333/333333) | Text | `#333333` | `--pa-text` | Body text, headings |
| ![#636b75](https://via.placeholder.com/24/636b75/636b75) | Text Muted | `#636b75` | `--pa-text-muted` | Captions, secondary text, edit links |

### Background & Surface Colours

| Swatch | Name | Hex | CSS Variable | Usage |
|--------|------|-----|--------------|-------|
| ![#ffffff](https://via.placeholder.com/24/ffffff/ffffff) | Background | `#ffffff` | `--pa-background` | Page background |
| ![#f8f9fa](https://via.placeholder.com/24/f8f9fa/f8f9fa) | Surface | `#f8f9fa` | `--pa-surface` | Cards, code blocks, sidebar, blockquotes |
| ![#e9ecef](https://via.placeholder.com/24/e9ecef/e9ecef) | Border | `#e9ecef` | `--pa-border` | Dividers, card borders, separators |

### CSS Implementation

```css
:root {
  --pa-primary: #1f4788;
  --pa-primary-hover: #0056b3;
  --pa-accent-1: #2e86de;
  --pa-accent-2: #27ae60;
  --pa-text: #333333;
  --pa-text-muted: #636b75;
  --pa-background: #ffffff;
  --pa-surface: #f8f9fa;
  --pa-border: #e9ecef;
}
```

---

## Typography

### Font Family

The site uses Roboto as the primary typeface with system font fallbacks to ensure text renders immediately if the web font is unavailable.

```css
--font-family: 'Roboto', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
```

The font is loaded from Google Fonts with `font-display: swap` to prevent invisible text during loading.

### Font Weights

| Weight | Value | CSS Variable | Usage |
|--------|-------|--------------|-------|
| Normal | 400 | `--font-weight-normal` | Body text, paragraphs, list items |
| Medium | 500 | `--font-weight-medium` | h3, h4 headings, buttons, labels |
| Bold | 700 | `--font-weight-bold` | h1, h2 headings, card titles, emphasis |

### Heading Sizes

| Level | Size | CSS Variable | Line Height |
|-------|------|--------------|-------------|
| h1 | 2.25em (36px) | `--heading-h1` | 1.2 |
| h2 | 1.625em (26px) | `--heading-h2` | 1.3 |
| h3 | 1.3em (20.8px) | `--heading-h3` | 1.4 |
| h4 | 1.1em (17.6px) | — | 1.4 |

### Body Text

| Property | Value | CSS Variable |
|----------|-------|--------------|
| Font size | 16px | `--font-size-base` |
| Line height | 1.7 | `--line-height` |
| Max width | 80ch | `--content-max-width` |

### CSS Implementation

```css
:root {
  --font-family: 'Roboto', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  --font-size-base: 16px;
  --line-height: 1.7;
  --heading-h1: 2.25em;
  --heading-h2: 1.625em;
  --heading-h3: 1.3em;
  --font-weight-normal: 400;
  --font-weight-medium: 500;
  --font-weight-bold: 700;
}
```

---

## Spacing Scale

All spacing follows an 8px base unit scale. These values are used for margins, padding, and gaps throughout the site.

| Name | Size | CSS Variable | Visual |
|------|------|--------------|--------|
| xs | 8px | `--space-xs` | <span style="display:inline-block;width:8px;height:16px;background:#2e86de;"></span> |
| sm | 16px | `--space-sm` | <span style="display:inline-block;width:16px;height:16px;background:#2e86de;"></span> |
| md | 24px | `--space-md` | <span style="display:inline-block;width:24px;height:16px;background:#2e86de;"></span> |
| lg | 32px | `--space-lg` | <span style="display:inline-block;width:32px;height:16px;background:#2e86de;"></span> |
| xl | 48px | `--space-xl` | <span style="display:inline-block;width:48px;height:16px;background:#2e86de;"></span> |

### Usage Guidelines

- **xs (8px)** — Tight spacing within components: list item margins, inline padding, icon gaps
- **sm (16px)** — Default paragraph spacing, form element padding, small gaps between elements
- **md (24px)** — Section padding, content area gutters, card internal padding
- **lg (32px)** — Major section separators, heading top margins, card grid gaps
- **xl (48px)** — Page-level section breaks, hero section padding, top-level heading margins

### Utility Classes

Spacing is available via utility classes for both margin and padding:

```css
/* Margin */
.m-xs  { margin: 8px; }
.mt-sm { margin-top: 16px; }
.mb-md { margin-bottom: 24px; }
.ml-lg { margin-left: 32px; }
.mr-xl { margin-right: 48px; }

/* Padding */
.p-xs  { padding: 8px; }
.pt-sm { padding-top: 16px; }
.pb-md { padding-bottom: 24px; }
.pl-lg { padding-left: 32px; }
.pr-xl { padding-right: 48px; }

/* Gap (for flex/grid layouts) */
.space-md { gap: 24px; }
```

### CSS Implementation

```css
:root {
  --space-xs: 8px;
  --space-sm: 16px;
  --space-md: 24px;
  --space-lg: 32px;
  --space-xl: 48px;
}
```

---

## UI Component Patterns

### Navigation Cards

Navigation cards are used on landing pages to direct visitors to major sections. They display a title and short description within a bordered, hoverable container.

<div class="nav-cards">
  <a class="nav-card" href="#/sexual-health-tariff/">
    <h3>Sexual Health Tariff</h3>
    <p>Comprehensive documentation for the Sexual Health Tariff Grouper application.</p>
  </a>
  <a class="nav-card" href="#/health-pathways">
    <h3>Health Pathways</h3>
    <p>Pathway-based approaches to healthcare delivery and commissioning.</p>
  </a>
</div>

**Markdown usage:**

```html
<div class="nav-cards">
  <a class="nav-card" href="#/sexual-health-tariff/">
    <h3>Sexual Health Tariff</h3>
    <p>Comprehensive documentation for the Tariff Grouper application.</p>
  </a>
  <a class="nav-card" href="#/health-pathways">
    <h3>Health Pathways</h3>
    <p>Pathway-based approaches to healthcare delivery.</p>
  </a>
</div>
```

**Styles applied:**

```css
.nav-cards {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: var(--space-md);
}

.nav-card {
  border: 1px solid var(--pa-border);
  border-radius: 6px;
  padding: var(--space-md);
  background-color: var(--pa-surface);
  transition: box-shadow 0.2s ease, border-color 0.2s ease;
}

.nav-card:hover {
  border-color: var(--pa-primary);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
}
```

---

### Blockquotes

Blockquotes are used for callouts, notes, and highlighted information. They have a coloured left border using accent-1.

> This is an example blockquote. Use blockquotes for important notes, callouts, or to highlight key information for the reader.

**Markdown usage:**

```markdown
> This is an example blockquote. Use blockquotes for important notes,
> callouts, or to highlight key information for the reader.
```

**Styles applied:**

```css
.markdown-section blockquote {
  border-left: 4px solid var(--pa-accent-1);
  background-color: var(--pa-surface);
  padding: var(--space-sm) var(--space-md);
  margin: var(--space-sm) 0;
  font-style: italic;
  border-radius: 0 4px 4px 0;
}
```

---

### Code Blocks

Inline code and fenced code blocks use the surface colour as background with a subtle border.

Inline example: `var(--pa-primary)` renders with a surface background.

Fenced code block example:

```css
.example {
  colour: var(--pa-primary);
  padding: var(--space-sm);
  border: 1px solid var(--pa-border);
}
```

**Styles applied:**

```css
.markdown-section code {
  font-size: 0.875em;
  padding: 2px 6px;
  background-color: var(--pa-surface);
  border-radius: 3px;
  border: 1px solid var(--pa-border);
}

.markdown-section pre {
  padding: var(--space-sm);
  background-color: var(--pa-surface);
  border-radius: 4px;
  border: 1px solid var(--pa-border);
  overflow-x: auto;
}
```

---

### Image Captions

Screenshots and figures use a caption below the image in muted text. Captions should be no longer than 200 characters.

<figure>
  <img src="../assets/images/logo.png" alt="Pathway Analytics logo" loading="lazy">
  <figcaption>The Pathway Analytics logo displayed at standard size for reference.</figcaption>
</figure>

**Markdown usage:**

```html
<figure>
  <img src="path/to/image.png" alt="Description of image" loading="lazy">
  <figcaption>Caption describing what the image shows (max 200 characters).</figcaption>
</figure>
```

**Styles applied:**

```css
.markdown-section figure {
  margin: var(--space-sm) 0 var(--space-md);
  text-align: center;
}

.markdown-section figcaption {
  font-size: 0.85em;
  color: var(--pa-text-muted);
  text-align: center;
  margin-top: var(--space-xs);
}
```

---

### Buttons and CTAs

Buttons are used for primary actions and calls-to-action. Two variants are available: primary (filled) and secondary (outlined).

<a class="btn" href="#">Primary Button</a>
<a class="btn btn-secondary" href="#">Secondary Button</a>

**Markdown usage:**

```html
<a class="btn" href="https://example.com">Primary Button</a>
<a class="btn btn-secondary" href="https://example.com">Secondary Button</a>
```

**Styles applied:**

```css
.btn {
  display: inline-block;
  padding: 12px 24px;
  font-size: var(--font-size-base);
  font-weight: var(--font-weight-medium);
  color: #ffffff;
  background-color: var(--pa-primary);
  border-radius: 4px;
  transition: background-color 0.2s ease;
}

.btn:hover {
  background-color: var(--pa-primary-hover);
}

.btn-secondary {
  background-color: transparent;
  color: var(--pa-primary);
  border: 2px solid var(--pa-primary);
}

.btn-secondary:hover {
  background-color: var(--pa-primary);
  color: #ffffff;
}
```

---

### Edit Suggestion Link

Every documentation page includes a "Suggest an edit" link in the bottom-right corner. It is styled with reduced visual weight to avoid distracting from content.

<div class="edit-link">
  <a href="https://github.com/Pathway-Analytics/docs/edit/main/style-guide/README.md" target="_blank" rel="noopener">
    <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"></path><path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"></path></svg>
    Suggest an edit
  </a>
</div>

**Styles applied:**

```css
.edit-link {
  text-align: right;
  margin-top: var(--space-xl);
  padding-top: var(--space-sm);
  border-top: 1px solid var(--pa-border);
}

.edit-link a {
  font-size: 0.8em;
  color: var(--pa-text-muted);
  opacity: 0.6;
  transition: opacity 0.2s ease;
}

.edit-link a:hover {
  opacity: 1.0;
  color: var(--pa-primary);
}
```

---

## Icon Usage

### GitHub Icons

GitHub icons are stored in `assets/images/github/` and used for repository links and the corner widget.

| Icon | File | Usage |
|------|------|-------|
| GitHub Mark (dark) | `github-mark.svg` | Light mode — repository links, corner widget |
| GitHub Mark (white) | `github-mark-white.svg` | Dark mode — repository links, corner widget |

The GitHub corner widget links to the repository at https://github.com/Pathway-Analytics/docs/ and is positioned fixed in the top-right corner.

### External Link Indicator

External application links (Tariff Grouper login, Configuration Portal) display an arrow icon to distinguish them from internal documentation links:

```html
<svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 24 24"
     fill="none" stroke="currentColor" stroke-width="2"
     stroke-linecap="round" stroke-linejoin="round">
  <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path>
  <polyline points="15 3 21 3 21 9"></polyline>
  <line x1="10" y1="14" x2="21" y2="3"></line>
</svg>
```

### Dark Mode Toggle Icon

The dark mode toggle button uses a sun/moon icon pair. When in light mode a moon icon is displayed; when in dark mode a sun icon is shown. The toggle is positioned in the navbar area.

---

## Dark Mode

The site supports a dark colour scheme that activates via:
1. User toggle (persisted in `localStorage` under key `pa-theme-preference`)
2. Operating system preference (`prefers-color-scheme: dark`) when no stored preference exists

### Colour Mappings

| Token | Light Mode | Dark Mode | CSS Variable |
|-------|-----------|-----------|--------------|
| Primary | `#1f4788` | `#5b9bf5` | `--pa-primary` |
| Primary Hover | `#0056b3` | `#7db4f8` | `--pa-primary-hover` |
| Accent 1 | `#2e86de` | `#64b5f6` | `--pa-accent-1` |
| Accent 2 | `#27ae60` | `#81c784` | `--pa-accent-2` |
| Text | `#333333` | `#f1f1f1` | `--pa-text` |
| Text Muted | `#636b75` | `#adb5bd` | `--pa-text-muted` |
| Background | `#ffffff` | `#121212` | `--pa-background` |
| Surface | `#f8f9fa` | `#1e1e1e` | `--pa-surface` |
| Border | `#e9ecef` | `#444444` | `--pa-border` |

### CSS Implementation

```css
[data-theme="dark"] {
  --pa-primary: #5b9bf5;
  --pa-primary-hover: #7db4f8;
  --pa-accent-1: #64b5f6;
  --pa-accent-2: #81c784;
  --pa-text: #f1f1f1;
  --pa-text-muted: #adb5bd;
  --pa-background: #121212;
  --pa-surface: #1e1e1e;
  --pa-border: #444444;
}
```

### Logo Switching

When dark mode is active, the Pathway Analytics logo switches to its white variant to maintain visibility against the dark background:

- **Light mode:** `Pathway Analytics Logo small.png`
- **Dark mode:** `Pathway Analytics Logo small white.png`

### Contrast Requirements

All colour combinations maintain WCAG 2.1 AA compliance:
- Normal text (under 18px): minimum 4.5:1 contrast ratio
- Large text (18px or above): minimum 3:1 contrast ratio

---

## Layout

### Layout Modes

The site uses two layout modes based on the current section:

| Mode | CSS Class | Sidebar | Content Width | Used On |
|------|-----------|---------|---------------|---------|
| Full-width | `body.full-width` | Hidden | `max-width: 80ch`, centred | Landing page, Style Guide, Health Pathways, FTCi, Case Studies |
| Sidebar | `body.has-sidebar` | Visible (280px) | `max-width: 80ch`, offset left | Sexual Health Tariff section |

### Layout Variables

```css
:root {
  --content-max-width: 80ch;
  --sidebar-width: 280px;
  --navbar-height: 60px;
}
```

### Responsive Breakpoints

| Breakpoint | Behaviour |
|-----------|-----------|
| > 1024px | Full desktop layout with sidebar alongside content |
| 768px–1024px | Slightly compressed spacing, sidebar still visible |
| < 768px | Sidebar collapses to off-canvas panel, hamburger menu appears, touch targets enforced at 44×44px minimum |
