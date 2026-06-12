# Style Guide

This guide documents the design system, available components, and markdown conventions used across the Pathway Analytics documentation site.

---

## Colour Palette

All colours are defined as CSS custom properties and adapt automatically between light and dark modes.

| Token | Light | Dark | Usage |
|-------|-------|------|-------|
| `--pa-primary` | `#1f4788` | `#6aa7f8` | Links, headings, active states |
| `--pa-primary-hover` | `#163561` | `#9dc4fb` | Hover states |
| `--pa-accent` | `#2e86de` | `#64b5f6` | Highlights, blockquote borders |
| `--pa-text` | `#2d3748` | `#e8eaed` | Body text |
| `--pa-text-muted` | `#636b75` | `#9aa5b4` | Secondary text, captions |
| `--pa-background` | `#ffffff` | `#0f1117` | Page background |
| `--pa-surface` | `#f7f8fa` | `#1a1d27` | Cards, code blocks, sidebar |
| `--pa-border` | `#e2e8f0` | `#2d3344` | Borders, dividers |

---

## Typography

| Element | Size | Weight | Notes |
|---------|------|--------|-------|
| Body text | 16px | 400 | Line-height 1.7, max-width 72ch |
| h1 | 2em | 700 | Primary blue colour |
| h2 | 1.5em | 700 | Bottom border separator |
| h3 | 1.2em | 500 | — |
| h4 | 1.05em | 500 | — |
| Code | 0.85em | mono | SF Mono / Fira Code |

Font stack: `Roboto, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif`

---

## Spacing

All spacing uses an 8px base scale:

| Token | Value | Usage |
|-------|-------|-------|
| `--space-xs` | 8px | Tight gaps, inline padding |
| `--space-sm` | 16px | Paragraph spacing, small gaps |
| `--space-md` | 24px | Section padding, card padding |
| `--space-lg` | 32px | Major separators |
| `--space-xl` | 48px | Page-level breaks |

---

## Headings

```markdown
# Heading 1 — page title (one per page)
## Heading 2 — major sections (gets bottom border)
### Heading 3 — subsections
#### Heading 4 — minor subsections
```

# Heading 1

## Heading 2

### Heading 3

#### Heading 4

---

## Navigation Cards

Used on landing pages to link to major sections:

```html
<div class="nav-cards">
  <a href="#/sexual-health-tariff/" class="nav-card">
    <h3>Card Title</h3>
    <p>Short description of the section.</p>
  </a>
  <a href="#/health-pathways/" class="nav-card">
    <h3>Another Card</h3>
    <p>Brief explanation of what this links to.</p>
  </a>
</div>
```

<div class="nav-cards">
  <a href="#/sexual-health-tariff/" class="nav-card">
    <h3>Example Card</h3>
    <p>This is how a navigation card renders on the page.</p>
  </a>
  <a href="#/style-guide/" class="nav-card">
    <h3>Style Guide</h3>
    <p>You are here — the design system reference.</p>
  </a>
</div>

---

## Blockquotes

Standard blockquotes use a blue left border:

```markdown
> This is a standard blockquote for general information.
```

> This is a standard blockquote for general information.

---

## Callouts

Special callout styles are applied based on the opening word:

### Note (amber border)

```markdown
> **Note:** This is a note callout with an amber left border.
```

> **Note:** This is a note callout with an amber left border.

### Important (red border)

```markdown
> **Important:** This is an important callout with a red left border.
```

> **Important:** This is an important callout with a red left border.

---

## Code

### Inline code

Use backticks for inline code: `variable`, `function()`, `file.md`

### Code blocks

Use triple backticks with an optional language identifier:

```sql
SELECT * FROM tariff_configurations
WHERE active = true;
```

```css
.nav-card {
  border: 1px solid var(--pa-border);
  border-radius: 6px;
  padding: var(--space-md);
}
```

---

## Tables

```markdown
| Column 1 | Column 2 | Column 3 |
|----------|----------|----------|
| Cell A   | Cell B   | Cell C   |
| Cell D   | Cell E   | Cell F   |
```

| Column 1 | Column 2 | Column 3 |
|----------|----------|----------|
| Cell A   | Cell B   | Cell C   |
| Cell D   | Cell E   | Cell F   |

---

## Lists

### Unordered

```markdown
- First item
- Second item
  - Nested item
- Third item
```

- First item
- Second item
  - Nested item
- Third item

### Ordered

```markdown
1. Step one
2. Step two
3. Step three
```

1. Step one
2. Step two
3. Step three

---

## Links

### Internal links

```markdown
[Link text](/sexual-health-tariff/configurations)
```

[Example internal link](/sexual-health-tariff/configurations)

### External links

Use an arrow indicator for external application links:

```markdown
[Tariff Grouper Login ↗](https://secure.pathwayanalytics.com/common/)
```

[Tariff Grouper Login ↗](https://secure.pathwayanalytics.com/common/)

---

## Images

### Standard image

```markdown
![Alt text description](assets/images/example.png)
```

### Image with caption

```html
<figure>
  <img src="assets/images/logo.png" alt="Pathway Analytics logo" loading="lazy">
  <figcaption>Caption text goes here (max 200 characters).</figcaption>
</figure>
```

Use `loading="lazy"` on all images below the fold.

---

## Horizontal Rules

Use `---` to create a horizontal divider between major sections:

```markdown
---
```

---

## Bold and Italic

```markdown
**Bold text** for emphasis
*Italic text* for secondary emphasis
***Bold italic*** for strong emphasis
```

**Bold text** for emphasis  
*Italic text* for secondary emphasis  
***Bold italic*** for strong emphasis

---

## Dark Mode

The site supports automatic dark/light mode switching. All colours adapt via CSS custom properties. Use the toggle button in the top-right corner.

Content authors don't need to do anything special — the theme handles colour adaptation automatically. Avoid using hardcoded colour values in inline styles.

---

## Edit Links

Every page automatically includes a "Suggest an edit" link in the bottom-right corner linking to the source file on GitHub. This is generated by a plugin — no markup needed.
