# Implementation Plan: Documentation Site Redesign

## Overview

This plan implements the complete redesign of the Pathway Analytics documentation site (docs.pathwayanalytics.com) built on Docsify 4. The work is structured as: foundational setup (index.html, CSS custom properties, plugins), content structure reorganisation, page content authoring, and final integration/validation. All tasks produce static files with no build step.

## Tasks

- [x] 1. Set up application shell and design system foundation
  - [x] 1.1 Rewrite `index.html` with full Docsify 4 configuration, meta tags, and plugin references
    - Include SEO meta tags (title ≤60 chars, description 50–160 chars, canonical, robots, Open Graph, JSON-LD)
    - Include favicon and Apple Touch Icon references from Brand_Assets
    - Include Google Fonts preconnect and Roboto stylesheet link
    - Add `<noscript>` fallback message
    - Add skip-navigation link as first focusable element
    - Configure `window.$docsify` object per design (loadSidebar, loadNavbar, hash routing, search config, subMaxLevel: 3, auto2top, notFoundPage)
    - Reference CDN scripts: Docsify core v4, search plugin, zoom-image plugin, copy-code plugin (all with `async` or `defer`)
    - Include inline custom plugins (sidebar toggle, dark mode, edit link)
    - _Requirements: 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 5.2, 5.3, 11.2, 11.3, 11.5, 12.1, 12.2, 12.3, 12.4, 12.5, 18.1, 18.2, 18.3_

  - [x] 1.2 Create the CSS custom properties and base theme in `assets/css/custom.css`
    - Define `:root` custom properties for colours, spacing (8px scale), typography (Roboto, heading sizes, line-height 1.7)
    - Define `[data-theme="dark"]` overrides for all colour properties
    - Implement base/reset styles, font stack with system fallbacks, `font-display: swap`
    - Set content max-width to 80ch for body text readability
    - Define spacing utility classes using the 8px increment scale
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 4.2_

  - [x] 1.3 Implement layout styles (navbar, sidebar, content area, full-width mode)
    - Fixed-position navbar with 60px height, always visible on scroll
    - Sidebar at 280px width, visible only when `body.has-sidebar`
    - Full-width content area with max-width constraint when `body.full-width`
    - Responsive breakpoints at 768px and 1024px
    - Off-canvas sidebar below 768px with slide-in animation
    - Hamburger menu button below 768px
    - Touch targets ≥ 44x44px on mobile
    - _Requirements: 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 9.1, 9.2, 9.6, 9.7_

  - [x] 1.4 Implement typography, component styles, and accessibility CSS
    - Heading hierarchy styles (h1 at 2.25em, h2 at 1.625em, h3 at 1.3em)
    - Navigation card component styles (grid layout, title + description)
    - Button/CTA styles, image captions, blockquote styles
    - Edit link styles (opacity 0.6, hover to 1.0, small font, muted colour)
    - Focus indicators with 3:1 contrast ratio
    - Skip link styling (visible on focus, hidden otherwise)
    - Reduced motion media query
    - CLS prevention via inline critical CSS approach
    - _Requirements: 1.2, 1.5, 5.1, 5.2, 5.5, 5.6, 15.1, 15.5_

- [x] 2. Implement custom Docsify plugins
  - [x] 2.1 Implement the sidebar toggle plugin (inline in index.html)
    - Monitor route changes via `hook.doneEach`
    - Toggle `has-sidebar` / `full-width` CSS classes on `<body>` based on whether path starts with `/sexual-health-tariff`
    - Ensure full-width layout applies to landing page, case studies, health pathways, FTCi, and style guide
    - _Requirements: 9.1, 9.2, 9.7_

  - [x] 2.2 Implement the dark mode plugin (inline in index.html)
    - Create toggle button/icon in navbar area
    - Read preference hierarchy: localStorage (`pa-theme-preference`) → OS `prefers-color-scheme` → default light
    - Set `data-theme` attribute on `<html>` element
    - Persist preference to localStorage on toggle
    - Swap logo src between standard and white variants when theme changes
    - Wrap localStorage calls in try/catch for fallback
    - _Requirements: 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 11.4_

  - [x] 2.3 Implement the edit link plugin (inline in index.html)
    - Use `hook.afterEach` to append edit link HTML after rendered content
    - Derive file path from `vm.route.file`
    - Generate URL: `https://github.com/Pathway-Analytics/docs/edit/main/{filepath}`
    - Include pencil/GitHub icon SVG adjacent to link text
    - Open in new tab with `target="_blank" rel="noopener"`
    - Position in bottom-right of content area
    - _Requirements: 15.1, 15.2, 15.3, 15.4, 15.5, 15.6_

- [x] 3. Checkpoint - Verify foundation
  - Ensure index.html loads correctly with Docsify, all plugins initialise without errors, dark mode toggles correctly, sidebar shows/hides based on route, and edit links appear. Ask the user if questions arise.

- [x] 4. Create navigation structure and content framework
  - [x] 4.1 Create `_navbar.md` with top-level navigation links
    - Links: Home, Sexual Health Tariff, Health Pathways, FTCi, Case Studies
    - Ensure Docsify renders this as the fixed navbar
    - _Requirements: 9.6_

  - [x] 4.2 Create `sexual-health-tariff/_sidebar.md` with full hierarchical navigation
    - Include all sections: Overview, Executive (Executive Summary), Commissioner (Commissioner Guidance, Tariff Configurations, Live Configurations, Pathways, Grouper Process, Governance, Review Process), Provider (Provider Onboarding, How-To Guides, Technical Guidance), Subscriptions & Pricing
    - Use bold text for audience group headings
    - _Requirements: 7.4, 7.6, 9.3, 9.4, 9.5_

  - [x] 4.3 Create directory structure for all content sections
    - Create `sexual-health-tariff/` subdirectory with all required markdown files (placeholders initially)
    - Create `health-pathways/` with `README.md` and `_sidebar.md`
    - Create `ftci/` with `README.md` and `_sidebar.md`
    - Create `case-studies/` with `README.md` and `_sidebar.md`
    - Create `style-guide/` with `README.md`
    - Create `assets/images/how-to/` subdirectories (data-upload, tariff-calculation, report-generation)
    - _Requirements: 7.1, 7.2, 7.3, 7.5, 7.7, 7.8, 7.9, 16.1, 17.1, 17.2, 17.4_

- [x] 5. Author landing page and top-level content
  - [x] 5.1 Rewrite `README.md` as the branded landing page
    - Hero section with value proposition (≤30 words)
    - Navigation cards grid: Sexual Health Tariff Grouper, Health Pathways, FTCi, Case Studies (each with title + one-sentence description)
    - G-Cloud 14 badge as linked image (opens Digital Marketplace in new tab)
    - External links: Tariff Grouper login (https://secure.pathwayanalytics.com/common/), Configuration Portal (https://production.pathwayanalytics.com/public/configuration) — both open in same tab, with external link icons
    - Contact section with mailto link to enquiries@pathwayanalytics.com
    - Footer with Style Guide link (route to `style-guide`)
    - _Requirements: 6.1, 6.2, 6.3, 6.4, 6.5, 6.6, 14.1, 14.2, 14.3, 14.4_

  - [x] 5.2 Create `health-pathways/README.md` placeholder landing page
    - h1 heading, introductory description, "documentation under development" statement
    - _Requirements: 17.1, 17.3_

  - [x] 5.3 Create `ftci/README.md` placeholder landing page
    - h1 heading, introductory description, "documentation under development" statement
    - _Requirements: 17.2, 17.3_

  - [x] 5.4 Create `case-studies/README.md` as the case studies index page
    - h1 heading, listing of available case studies (title as link + ≤200 char summary per entry)
    - Template structure for individual case study pages (title h1, client context h2, challenge h2, approach h2, outcomes h2)
    - _Requirements: 16.1, 16.2, 16.3, 16.4_

- [x] 6. Author Sexual Health Tariff Grouper documentation
  - [x] 6.1 Create `sexual-health-tariff/README.md` as the section landing page
    - Overview of the Tariff Grouper
    - Labelled navigation links for Executive, Commissioner, Provider audience paths visible without scrolling on desktop
    - Links to Tariff Grouper login and Configuration Portal (same tab, with external link icons)
    - _Requirements: 7.4, 14.1, 14.2, 14.3, 14.4_

  - [x] 6.2 Create `sexual-health-tariff/executive-summary.md`
    - Business case, benefits, and ROI explanation of the Tariff Grouper
    - _Requirements: 7.1_

  - [x] 6.3 Create `sexual-health-tariff/commissioner-guidance.md`
    - Tariff configuration ownership, setup process, monitoring responsibilities
    - _Requirements: 7.2_

  - [x] 6.4 Reorganise existing content into `sexual-health-tariff/configurations.md` and `sexual-health-tariff/grouper-process.md`
    - Move/adapt existing Tariff Configurations and Grouper Process content from archive
    - Place within Commissioner Guidance section context
    - _Requirements: 7.5_

  - [x] 6.5 Create `sexual-health-tariff/governance.md`
    - Governance framework: roles/responsibilities, decision-making authority, escalation procedures, change management
    - _Requirements: 7.7_

  - [x] 6.6 Create `sexual-health-tariff/review-process.md`
    - Periodic review cycle: review frequency, stakeholder involvement, criteria for in-year changes, approval workflow
    - _Requirements: 7.8_

  - [x] 6.7 Create `sexual-health-tariff/technical-guidance.md`
    - Technical data submission details: file formats, field specifications, validation rules, error handling, integration requirements
    - _Requirements: 7.9_

  - [x] 6.8 Create `sexual-health-tariff/provider-onboarding.md`
    - Subscription setup, data submission workflows, how to use the application
    - _Requirements: 7.3_

  - [x] 6.9 Create `sexual-health-tariff/how-to-guides.md`
    - Numbered step-by-step guides for: data upload, tariff calculation, report generation workflows
    - Each guide has ≥3 numbered steps with instructional text and at least one screenshot reference per step
    - Screenshots stored in `assets/images/how-to/{workflow}/step-{number}-{action}.png`
    - Image captions ≤200 characters below each screenshot
    - `loading="lazy"` attribute on all screenshot images
    - Zoom-image plugin activates on click
    - _Requirements: 8.1, 8.2, 8.3, 8.4, 8.5, 8.6_

  - [x] 6.10 Create `sexual-health-tariff/subscriptions.md`
    - Pricing: Provider+ £680+VAT, Commissioner £680+VAT, Cluster Manager £680+VAT + £345+VAT per additional org
    - Subscription period: 10 months, extended to 12 months if paid within 30 days
    - List each type (Basic Provider, Provider+, Commissioner, Cluster Manager) with name, target role, included capabilities
    - Subscription transfer policy
    - Mailto link to enquiries@pathwayanalytics.com for subscription requests
    - _Requirements: 13.1, 13.2, 13.3, 13.4, 13.5_

  - [x] 6.11 Create `sexual-health-tariff/live-configurations.md` with embedded iframe
    - Introductory paragraph explaining tariff configurations list and search/filter
    - iframe embedding https://production.pathwayanalytics.com/public/configuration
    - iframe: width 100%, min-height 800px, title attribute for accessibility
    - Fallback message with direct link if iframe blocked by CSP/X-Frame-Options
    - _Requirements: 20.1, 20.2, 20.3, 20.4, 20.5, 20.6, 20.7_

  - [x] 6.12 Create `sexual-health-tariff/pathways.md` with embedded iframe
    - Introductory paragraph explaining activity-based costing model (steps, clinical resources, consumables, cost breakdowns)
    - iframe embedding https://production.pathwayanalytics.com/public/pathway/100
    - iframe: width 100%, min-height 800px, title attribute for accessibility
    - Fallback message with direct link if iframe blocked
    - Allow pathway search functionality within iframe
    - _Requirements: 21.1, 21.2, 21.3, 21.4, 21.5, 21.6, 21.7, 21.8_

- [x] 7. Checkpoint - Verify content and navigation
  - Ensure all pages load via hash routing, sidebar navigation works correctly within the Sexual Health Tariff section, full-width layout applies to all other sections, all internal links resolve, and external links are correct. Ask the user if questions arise.

- [x] 8. Create Style Guide and finalise
  - [x] 8.1 Create `style-guide/README.md` documenting the complete design system
    - Colour palette: primary (#1f4788), primary hover (#0056b3), accents, light/dark backgrounds, text colours, borders — each as named swatch with hex value
    - Typography system: font family, weights (400, 500, 700), heading sizes, body text size, line-height
    - Spacing scale: 8px, 16px, 24px, 32px, 48px with visual examples
    - UI component patterns: navigation cards, blockquotes, code blocks, image captions, buttons/CTAs, edit suggestion link — with rendered examples
    - Icon usage: GitHub icons, external link indicators, dark mode toggle icon
    - Dark mode colour mappings: light values alongside dark equivalents
    - Full-width layout, no sidebar
    - _Requirements: 19.1, 19.2, 19.3, 19.4, 19.5, 19.6, 19.7, 19.8_

  - [x] 8.2 Create `_404.md` custom not-found page
    - Friendly message with helpful navigation links back to main sections
    - _Requirements: 18.5_

  - [x] 8.3 Add footer content to landing page with Style Guide link
    - Ensure Style Guide link is in the footer area, not the navbar
    - _Requirements: 19.1_

- [x] 9. Accessibility and performance validation
  - [x] 9.1 Run accessibility audit
    - Validate WCAG 2.1 AA colour contrast (4.5:1 normal text, 3:1 large text) in both themes
    - Verify skip-navigation link functionality
    - Verify keyboard operability of all interactive controls
    - Check ARIA landmarks and labels on custom widgets
    - Validate heading hierarchy (single h1, sequential progression)
    - Verify alt text on all images
    - Verify focus indicators meet 3:1 contrast
    - _Requirements: 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7_

  - [x] 9.2 Run performance validation
    - Verify First Contentful Paint < 3s on simulated 4G
    - Verify CLS ≤ 0.1
    - Confirm `loading="lazy"` on below-fold images
    - Confirm `async`/`defer` on all plugin scripts
    - Confirm no flash of unstyled content
    - _Requirements: 18.1, 18.2, 18.3, 18.4, 1.5_

  - [x] 9.3 Validate SEO and structured data
    - Verify JSON-LD parses as valid JSON with required schema.org Organization properties
    - Verify Open Graph tags render correctly
    - Verify robots meta tag, canonical URL, meta description length
    - _Requirements: 12.1, 12.2, 12.3, 12.4, 12.5_

  - [x] 9.4 Run link validation
    - Validate all internal links resolve (no 404s)
    - Validate all external links return 200
    - Verify Brand_Assets URLs return 200
    - _Requirements: 14.1, 14.2, 6.3, 6.4_

- [x] 10. Final checkpoint - Complete integration verification
  - Ensure all tests pass, all pages render correctly in both light and dark mode, responsive layout works at all breakpoints, sidebar is scoped correctly, and all requirements are covered. Ask the user if questions arise.

## Notes

- Tasks marked with `*` are optional validation tasks that can be skipped for faster delivery
- Each task references specific requirements for traceability
- Checkpoints ensure incremental validation at natural breakpoints
- No property-based tests are included because this is a static site with no pure-function logic suitable for PBT (as documented in the design)
- All plugins are inline JavaScript in index.html — no separate JS files or build step
- Screenshot images for how-to guides are expected to be captured manually and added to the repository
- The existing content in `.archive/` and current `sexual-health-tariff/` provides source material for reorganisation

## Task Dependency Graph

```json
{
  "waves": [
    { "id": 0, "tasks": ["1.1", "1.2"] },
    { "id": 1, "tasks": ["1.3", "1.4", "2.1", "2.2", "2.3"] },
    { "id": 2, "tasks": ["4.1", "4.2", "4.3"] },
    { "id": 3, "tasks": ["5.1", "5.2", "5.3", "5.4"] },
    { "id": 4, "tasks": ["6.1", "6.2", "6.3", "6.4", "6.5", "6.6", "6.7", "6.8", "6.10", "6.11", "6.12"] },
    { "id": 5, "tasks": ["6.9", "8.1", "8.2", "8.3"] },
    { "id": 6, "tasks": ["9.1", "9.2", "9.3", "9.4"] }
  ]
}
```
