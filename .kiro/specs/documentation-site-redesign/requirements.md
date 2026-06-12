# Requirements Document

## Introduction

This document specifies the requirements for a complete redesign of the Pathway Analytics documentation and marketing site. The site is built on docsify and hosted at https://docs.pathwayanalytics.com. It will serve as both the primary documentation hub for the Sexual Health Tariff Grouper product and a marketing/informational site for Pathway Analytics' broader healthcare economics consultancy work. The redesign will deliver a clean, modern, professional design with audience-segmented content, comprehensive Tariff Grouper documentation, and eventually replace https://www.pathwayanalytics.com as the primary web presence.

## Glossary

- **Documentation_Site**: The docsify-based documentation and marketing site hosted at https://docs.pathwayanalytics.com
- **Docsify**: A lightweight JavaScript documentation site generator that renders Markdown files as web pages without a build step
- **Tariff_Grouper**: The Sexual Health Tariff Grouper — a SaaS web application that automates tariff implementation for healthcare activity
- **Commissioner**: A Local Authority District or County responsible for commissioning sexual health services and specifying tariff configurations
- **Provider**: A healthcare provider organisation that delivers sexual health services and submits activity data for tariff calculations
- **Executive**: A senior decision-maker (e.g. Director of Public Health, CFO) evaluating the Tariff Grouper for strategic or financial purposes
- **Tariff_Configuration**: The set of specifications describing the implementation of a tariff arrangement for a healthcare provider with a range of dates
- **Brand_Assets**: Brand assets hosted at https://mta-sts.pathwayanalytics.com/ including logos, favicons, and brand imagery
- **Dark_Mode**: An alternative colour scheme using dark backgrounds and light text to reduce eye strain
- **Landing_Page**: The homepage of the Documentation_Site that functions as both a marketing page and documentation entry point
- **Sidebar**: A persistent navigation panel providing hierarchical access to documentation sections
- **Navbar**: The top-level horizontal navigation bar providing access to major site sections
- **Configuration_Portal**: The public tariff configurations interface at https://production.pathwayanalytics.com/public/configuration
- **CCS_Digital_Marketplace**: The Crown Commercial Service G-Cloud marketplace where Pathway Analytics is listed as a G-Cloud 14 supplier
- **Search_Plugin**: The Docsify full-text search plugin that indexes all documentation pages
- **GitHub_Pages**: The static site hosting service used to deploy the Documentation_Site from the repository
- **Visitor**: Any person accessing the Documentation_Site via a web browser
- **WCAG**: Web Content Accessibility Guidelines — the international standard for web accessibility
- **Style_Guide**: A dedicated section of the Documentation_Site documenting the design system, colour palette, typography, spacing, and UI component patterns used across the site

## Requirements

### Requirement 1: Modern Visual Design System

**User Story:** As a Visitor, I want the site to have a clean, modern, professional appearance, so that I have confidence in the quality and credibility of Pathway Analytics' services.

#### Acceptance Criteria

1. THE Documentation_Site SHALL use a design system based on the primary brand colour (#1f4788) with at least two complementary accent colours derived from the existing Brand_Assets palette, defined as CSS custom properties
2. THE Documentation_Site SHALL use a sans-serif font stack beginning with Roboto and including at least two system fallback fonts, with a typographic hierarchy where h1 is at least 2em, h2 at least 1.5em, h3 at least 1.25em, body text line-height is between 1.6 and 1.8, and vertical spacing between text elements follows a base-unit scale of 8px multiples
3. THE Documentation_Site SHALL apply spacing and whitespace throughout all pages using a defined spacing scale based on 8px increments (8px, 16px, 24px, 32px, 48px) applied via CSS custom properties
4. THE Documentation_Site SHALL present content with a maximum line width of 80 characters for body text to ensure readability
5. WHEN a page loads, THE Documentation_Site SHALL render with a Cumulative Layout Shift (CLS) score of 0.1 or less and no flash of unstyled content, by loading critical CSS inline or before render-blocking scripts
6. IF the external font service is unavailable, THEN THE Documentation_Site SHALL render using the system fallback fonts defined in the font stack without layout shift or delay in text rendering

### Requirement 2: Docsify Configuration and Plugin Setup

**User Story:** As a developer, I want the docsify instance to be properly configured with appropriate plugins, so that the site has full-text search, responsive layout, and extensibility.

#### Acceptance Criteria

1. THE Documentation_Site SHALL serve content from a single `index.html` file using Docsify version 4 or later
2. THE Documentation_Site SHALL include the Docsify search plugin that displays matching results with page titles and content excerpts within the Sidebar area as the Visitor types, without requiring a page reload or form submission
3. THE Documentation_Site SHALL include the Docsify zoom-image plugin that displays a zoomed overlay when a Visitor clicks any image within the content area
4. THE Documentation_Site SHALL include a copy-code plugin that renders a visible "Copy" button on each code block, placing the code content into the clipboard when clicked
5. THE Documentation_Site SHALL use hash-based routing so that navigating to any defined content path returns the corresponding page content without requiring server-side URL rewriting
6. THE Documentation_Site SHALL load the sidebar navigation from Markdown files with section-specific sidebars supported via nested `_sidebar.md` files in each content directory
7. IF a plugin script fails to load from the CDN, THEN THE Documentation_Site SHALL still render page content and navigation without error

### Requirement 3: Responsive Layout

**User Story:** As a mobile user, I want the site to be fully usable on phones and tablets, so that I can access documentation from any device.

#### Acceptance Criteria

1. THE Documentation_Site SHALL render all content without horizontal scrolling, text truncation, or element overlap on viewports from 320px to 2560px wide
2. WHEN the viewport width is below 768px, THE Documentation_Site SHALL collapse the Sidebar into a toggleable off-canvas panel that slides in from the left edge of the screen
3. WHEN the viewport width is below 768px, THE Documentation_Site SHALL display the navigation as a hamburger menu button that toggles visibility of the navigation links
4. THE Documentation_Site SHALL constrain images to a maximum width of 100% of their containing element so that no image exceeds the viewport width
5. WHILE the viewport width is 768 pixels or less, THE Documentation_Site SHALL ensure all interactive elements have a minimum touch target size of 44x44 pixels
6. WHEN a Visitor taps outside the off-canvas panel or presses the toggle button while the panel is open on a viewport below 768px, THE Documentation_Site SHALL hide the off-canvas panel

### Requirement 4: Dark Mode Support

**User Story:** As a user who works in low-light environments, I want to toggle a dark colour scheme, so that I can read comfortably without eye strain.

#### Acceptance Criteria

1. THE Documentation_Site SHALL provide a Dark_Mode toggle control accessible from the Navbar area, rendered as a clickable button or icon
2. WHEN the Visitor activates Dark_Mode, THE Documentation_Site SHALL switch CSS custom properties to their dark-mode equivalents: --text-color to #f1f1f1, --background-color to #121212, --primary-color to #1a73e8, --secondary-color to #2c2c2c, and --border-color to #444444
3. THE Documentation_Site SHALL persist the Visitor's Dark_Mode preference in browser localStorage under a defined key
4. WHEN no stored preference exists in localStorage, THE Documentation_Site SHALL respect the operating system's preferred colour scheme via the `prefers-color-scheme: dark` media query
5. WHEN Dark_Mode is active, THE Documentation_Site SHALL maintain a minimum contrast ratio of 4.5:1 between text and background colours for normal text and 3:1 for large text (18px or above)
6. WHEN Dark_Mode is active, THE Documentation_Site SHALL switch to the white variant of the logo from Brand_Assets ("Pathway Analytics Logo small white.png")

### Requirement 5: Accessibility Compliance

**User Story:** As a user with accessibility needs, I want the site to follow accessibility best practices, so that I can navigate and read content using assistive technologies.

#### Acceptance Criteria

1. THE Documentation_Site SHALL meet WCAG 2.1 Level AA colour contrast requirements: a minimum contrast ratio of 4.5:1 for normal text and 3:1 for large text (18px or above, or 14px bold) across all pages
2. THE Documentation_Site SHALL provide a skip-navigation link as the first focusable element on each page, visible on keyboard focus, that moves focus to the main content area
3. THE Documentation_Site SHALL use semantic HTML elements (nav, main, article, aside, header, footer) for document structure
4. THE Documentation_Site SHALL provide alt text for all images: non-decorative images SHALL have alt text describing the image content in 150 characters or fewer, and decorative images SHALL have an empty alt attribute (alt="")
5. THE Documentation_Site SHALL ensure all interactive controls (links, buttons, and form inputs) are operable via keyboard and display a visible focus indicator with a minimum contrast ratio of 3:1 against adjacent colours
6. THE Documentation_Site SHALL use ARIA landmarks and labels on custom widgets and container elements that do not have a corresponding semantic HTML element
7. THE Documentation_Site SHALL use a logical heading hierarchy on each page, starting with a single h1 and progressing sequentially (h2, h3, h4) without skipping levels

### Requirement 6: Branded Landing Page

**User Story:** As a first-time Visitor, I want an engaging landing page that explains what Pathway Analytics does and directs me to relevant content, so that I can quickly understand the company's offerings.

#### Acceptance Criteria

1. THE Landing_Page SHALL display the Pathway Analytics logo sourced from Brand_Assets at a maximum height of 40 pixels in the Navbar
2. THE Landing_Page SHALL include a hero section with a value proposition of no more than 30 words describing Pathway Analytics' healthcare economics services
3. THE Landing_Page SHALL include navigation cards linking to: Sexual Health Tariff Grouper documentation, Health Pathways, FTCi, and Case Studies, with each card displaying a section title and one-sentence description
4. THE Landing_Page SHALL display the CCS_Digital_Marketplace G-Cloud 14 supplier accreditation as a linked image that opens the Digital Marketplace listing in a new browser tab
5. THE Landing_Page SHALL include a visible contact section containing a mailto link to enquiries@pathwayanalytics.com with descriptive link text
6. THE Landing_Page SHALL include a link to the Tariff_Grouper login at https://secure.pathwayanalytics.com/common/ visible without scrolling on a viewport of 768 pixels or larger

### Requirement 7: Audience-Segmented Tariff Grouper Documentation

**User Story:** As a Commissioner, Provider, or Executive, I want documentation tailored to my role, so that I can find relevant information without reading content intended for other audiences.

#### Acceptance Criteria

1. THE Documentation_Site SHALL provide an Executive Summary section within the Tariff Grouper documentation explaining the business case, benefits, and ROI of the Tariff_Grouper
2. THE Documentation_Site SHALL provide a Commissioner Guidance section covering tariff configuration ownership, the setup process, and monitoring responsibilities
3. THE Documentation_Site SHALL provide a Provider Onboarding section covering subscription setup, data submission workflows, and how to use the Tariff_Grouper application
4. WHEN a Visitor navigates to the Tariff Grouper documentation, THE Documentation_Site SHALL display labelled navigation links for each audience-specific path (Executive, Commissioner, Provider) visible without scrolling on a desktop viewport
5. THE Documentation_Site SHALL place the existing Tariff Configurations documentation within the Commissioner Guidance section, the Grouper Process documentation within the Commissioner Guidance section, and the Grouper setup documentation within the Provider Onboarding section
6. WHEN a Visitor selects an audience-specific path, THE Documentation_Site SHALL load only the content pages belonging to that audience section in the Sidebar
7. THE Documentation_Site SHALL provide a Governance section at path `sexual-health-tariff/governance` covering the governance framework for tariff arrangements including roles and responsibilities, decision-making authority, escalation procedures, and change management processes
8. THE Documentation_Site SHALL provide a Review Process section at path `sexual-health-tariff/review-process` documenting the periodic review cycle for tariff configurations including review frequency, stakeholder involvement, criteria for in-year changes, and the approval workflow
9. THE Documentation_Site SHALL provide a Technical Guidance section at path `sexual-health-tariff/technical-guidance` covering technical details for data submission including file formats, field specifications, validation rules, error handling, and integration requirements

### Requirement 8: How-To Guides with Screenshot Support

**User Story:** As a Provider user, I want step-by-step guides with annotated screenshots, so that I can learn how to use the Tariff Grouper application effectively.

#### Acceptance Criteria

1. THE Documentation_Site SHALL include how-to guides with numbered steps and supporting screenshots for the data upload, tariff calculation, and report generation Tariff_Grouper workflows
2. THE Documentation_Site SHALL store screenshots under `assets/images/` in subdirectories named by workflow (e.g., `assets/images/data-upload/`) with filenames following the pattern `step-<number>-<action>.png`
3. WHEN a Visitor clicks on a screenshot within a how-to guide, THE Documentation_Site SHALL display an enlarged version using the Docsify zoom-image plugin
4. THE Documentation_Site SHALL display a caption of no more than 200 characters below each screenshot describing what the screenshot illustrates
5. THE Documentation_Site SHALL apply the `loading="lazy"` attribute to all screenshot images so that images outside the visible viewport are not loaded until the Visitor scrolls within proximity
6. THE Documentation_Site SHALL render each how-to guide with a minimum of 3 numbered steps, where each step contains instructional text and at least one supporting screenshot

### Requirement 9: Navigation Structure and Sidebar Scope

**User Story:** As a documentation reader, I want a sidebar for navigating complex technical content but clean full-width layouts for simpler pages, so that navigation complexity matches content depth.

#### Acceptance Criteria

1. THE Documentation_Site SHALL display a Sidebar with hierarchical navigation ONLY within the Sexual Health Tariff Grouper documentation section (`sexual-health-tariff/` path and its sub-pages)
2. WHEN a Visitor navigates to the Landing_Page, Case Studies, Health Pathways, FTCi, or Style Guide sections, THE Documentation_Site SHALL NOT display a Sidebar and SHALL render content at full width within the maximum line-width constraint
3. THE Documentation_Site SHALL load the Sexual Health Tariff Sidebar from a `_sidebar.md` file within the `sexual-health-tariff/` directory, listing all sub-pages including Executive Summary, Commissioner Guidance, Provider Onboarding, How-To Guides, Tariff Configurations, Grouper Process, Subscriptions, Governance, Review Process, and Technical Guidance
4. WHEN the Visitor navigates to a page within the Sexual Health Tariff section, THE Documentation_Site SHALL visually distinguish the active page link from other Sidebar links using a different font weight or colour
5. THE Documentation_Site SHALL display sub-headings (up to heading level 3) from the current page within the Sidebar for in-page navigation within the Sexual Health Tariff section
6. THE Documentation_Site SHALL display a fixed-position Navbar on all pages that remains visible during vertical scrolling and contains links to all top-level sections (Home, Sexual Health Tariff, Health Pathways, FTCi, Case Studies)
7. WHEN the viewport width is below 768px within the Sexual Health Tariff section, THE Documentation_Site SHALL collapse the Sidebar into a toggleable off-canvas panel; on all other sections the full-width layout SHALL apply regardless of viewport width

### Requirement 10: Full-Text Search

**User Story:** As a Visitor looking for specific information, I want to search across all documentation, so that I can quickly find relevant content.

#### Acceptance Criteria

1. THE Search_Plugin SHALL provide a search input field accessible from the Sidebar area with placeholder text "Type to search"
2. WHEN the Visitor types a query, THE Search_Plugin SHALL display matching results with page titles and highlighted text snippets as clickable links that navigate to the matched page
3. THE Search_Plugin SHALL index all Markdown content to a depth of 4 heading levels
4. WHEN no results are found, THE Search_Plugin SHALL display the message "No matches found."
5. WHEN a Visitor types in the search input, THE Search_Plugin SHALL filter and display results in real-time without requiring a form submission

### Requirement 11: Branding and Logo Integration

**User Story:** As a brand stakeholder, I want consistent branding throughout the site using official assets, so that the site reflects the Pathway Analytics visual identity.

#### Acceptance Criteria

1. THE Documentation_Site SHALL display the Pathway Analytics logo sourced from https://mta-sts.pathwayanalytics.com/logo/Pathway%20Analytics%20Logo%20small.png in the Navbar at a maximum height of 40 pixels
2. THE Documentation_Site SHALL reference favicon assets from Brand_Assets via link elements in the HTML head: favicon.ico, apple-touch-icon.png, android-chrome-192x192.png, and android-chrome-512x512.png
3. THE Documentation_Site SHALL include Open Graph meta tags with og:image referencing the Pathway Analytics logo at a resolution of at least 1200×630 pixels
4. WHEN Dark_Mode is active, THE Documentation_Site SHALL switch the Navbar logo src to the white variant ("Pathway Analytics Logo small white.png") from Brand_Assets
5. THE Documentation_Site SHALL include Apple Touch Icon and PWA manifest icon references from Brand_Assets in the HTML head

### Requirement 12: SEO and Meta Configuration

**User Story:** As a marketing stakeholder, I want the site to have proper SEO metadata, so that the site ranks well in search engines and displays correctly when shared.

#### Acceptance Criteria

1. THE Documentation_Site SHALL include a meta title of 60 characters or fewer and a meta description of between 50 and 160 characters
2. THE Documentation_Site SHALL include Open Graph meta tags (og:title, og:description, og:image, og:url) where og:url matches the canonical URL and og:image references an image of at least 1200×630 pixels accessible via HTTPS
3. THE Documentation_Site SHALL include a canonical URL meta tag with the href value set to https://docs.pathwayanalytics.com
4. THE Documentation_Site SHALL include a JSON-LD script element containing a schema.org Organization object with the following properties: name, url, logo, and contactPoint (including contactType and email), and the JSON-LD SHALL be parseable as valid JSON
5. THE Documentation_Site SHALL include a robots meta tag with content value "index, follow"

### Requirement 13: Pricing and Subscription Information

**User Story:** As a potential customer, I want to see clear pricing and subscription details, so that I can understand the cost of using the Tariff Grouper.

#### Acceptance Criteria

1. THE Documentation_Site SHALL display subscription pricing stating: Provider+ at £680+VAT, Commissioner at £680+VAT, and Cluster Manager at £680+VAT plus £345+VAT per additional organisation
2. THE Documentation_Site SHALL state the subscription period as 10 months, automatically extended to 12 months if payment is received within 30 days of invoice
3. THE Documentation_Site SHALL list each subscription type (Basic Provider, Provider+, Commissioner, Cluster Manager) with its name, target user role (provider or commissioner), and included capabilities (data upload, tariff calculation, sandbox testing, KPI reports, or multi-organisation coverage as applicable)
4. THE Documentation_Site SHALL display a visible mailto link to enquiries@pathwayanalytics.com labelled for subscription requests on the subscriptions page
5. THE Documentation_Site SHALL state that subscription transfers are available in the event of a new appointee, long-term sickness, or comparable change in personnel

### Requirement 14: External Links and Application Access

**User Story:** As an existing subscriber, I want quick access to the Tariff Grouper login and public configuration search, so that I can access the application directly from the documentation site.

#### Acceptance Criteria

1. THE Documentation_Site SHALL include a link to the Tariff_Grouper login at https://secure.pathwayanalytics.com/common/ visible in the Navbar or within the first viewport (above the fold at 768 pixels viewport height) of the Sexual Health Tariff section landing page
2. THE Documentation_Site SHALL include a link to the Configuration_Portal at https://production.pathwayanalytics.com/public/configuration visible in the Navbar or within the first viewport of the Sexual Health Tariff section landing page
3. WHEN a Visitor clicks an external application link to the Tariff_Grouper or Configuration_Portal, THE Documentation_Site SHALL open the link in the same browser tab
4. THE Documentation_Site SHALL visually distinguish external application links from internal documentation links by displaying an external link icon (arrow or similar indicator) adjacent to the link text

### Requirement 15: Per-Page Edit Suggestion Link

**User Story:** As a community contributor, I want a discrete "Suggest an edit" link on each page that takes me directly to the correct file in GitHub's editor, so that I can propose improvements without searching for the source file.

#### Acceptance Criteria

1. THE Documentation_Site SHALL display a "Suggest an edit" link on every documentation page, positioned in the bottom-right corner of the content area with reduced visual weight (smaller font size, muted colour) so as not to distract from the page content
2. WHEN a Visitor clicks the "Suggest an edit" link, THE Documentation_Site SHALL open the corresponding Markdown source file in the GitHub edit interface at `https://github.com/Pathway-Analytics/docs/edit/main/{filepath}` in a new browser tab, where `{filepath}` is the relative path of the current page's Markdown file
3. THE Documentation_Site SHALL generate the edit link URL automatically using the Docsify `formatUpdated` hook or a custom plugin that derives the file path from the current route
4. THE Documentation_Site SHALL display a small pencil icon or GitHub icon adjacent to the "Suggest an edit" link text for visual context
5. THE Documentation_Site SHALL style the edit link with opacity of 0.6 or lower at rest, increasing to 1.0 on hover, to keep it discrete
6. THE Documentation_Site SHALL also display the Docsify corner widget in the top-right corner linking to the repository root at https://github.com/Pathway-Analytics/docs/ for general repository access

### Requirement 16: Case Studies Section

**User Story:** As a potential client, I want to read case studies of Pathway Analytics' healthcare economics work, so that I can understand the company's track record and capabilities.

#### Acceptance Criteria

1. THE Documentation_Site SHALL include a Case Studies section accessible from the Navbar link labelled "Case Studies" routing to the `case-studies` path, and from the Sidebar when sub-pages exist within the `case-studies/` directory
2. THE Documentation_Site SHALL render individual case study pages authored as Markdown files within the `case-studies/` directory, with each file appearing as a navigable page in the Sidebar
3. THE Documentation_Site SHALL display each case study page with the following sections as sequential headings: title (h1), client context (h2), challenge (h2), approach (h2), and outcomes (h2)
4. THE Documentation_Site SHALL provide a case studies index page at the `case-studies` path listing all available case studies, where each listing includes the case study title as a clickable link and a summary of no more than 200 characters

### Requirement 17: Health Pathways and FTCi Placeholder Sections

**User Story:** As a site maintainer, I want placeholder sections for Health Pathways and FTCi, so that future content can be added without restructuring the site.

#### Acceptance Criteria

1. THE Documentation_Site SHALL include a Health Pathways section with a landing page containing an h1 heading and introductory description, accessible via a Navbar link routing to the `health-pathways` path
2. THE Documentation_Site SHALL include an FTCi section with a landing page containing an h1 heading and introductory description, accessible via a Navbar link routing to the `ftci` path
3. THE Documentation_Site SHALL display placeholder content on each section landing page stating that full documentation is under development
4. WHEN a sub-page Markdown file is authored within the `health-pathways/` or `ftci/` directory, THE Documentation_Site SHALL display a Sidebar listing all sub-pages within that section via a section-specific `_sidebar.md` file

### Requirement 18: Performance and Loading

**User Story:** As a Visitor on a slow connection, I want the site to load quickly, so that I can access content without excessive waiting.

#### Acceptance Criteria

1. THE Documentation_Site SHALL load the initial page (HTML, CSS, docsify core) such that the first contentful paint occurs within 3 seconds on a 4G connection (15 Mbps download, 50ms round-trip latency)
2. THE Documentation_Site SHALL load plugin scripts using the `async` or `defer` attribute so that they do not block rendering of the initial page content
3. THE Documentation_Site SHALL reference all docsify and plugin JavaScript and CSS assets from CDN-hosted URLs rather than locally hosted files
4. THE Documentation_Site SHALL apply the `loading="lazy"` attribute to images not visible in the initial viewport
5. IF the Documentation_Site fails to fetch a Markdown content page within 10 seconds or receives a network error, THEN THE Documentation_Site SHALL display a visible text message indicating the requested page could not be loaded, rather than a blank screen

### Requirement 20: Embedded Tariff Configurations Page

**User Story:** As a Commissioner or Provider, I want to browse available tariff configurations directly within the documentation site, so that I can find my local tariff arrangement without navigating to a separate application.

#### Acceptance Criteria

1. THE Documentation_Site SHALL include a page at path `sexual-health-tariff/live-configurations` accessible from the Sexual Health Tariff Sidebar, labelled "Live Configurations"
2. THE Documentation_Site SHALL embed the "Available Tariff Configurations" content from https://production.pathwayanalytics.com/public/configuration using an iframe element
3. THE iframe SHALL be styled to fill the available content width (100%) and have a minimum height of 800 pixels, expanding to accommodate the embedded content without requiring a scrollbar within the iframe where possible
4. THE iframe SHALL hide the production site's native navigation header and footer, achieved either by targeting a specific section via a URL fragment/parameter supported by the production app, or by using CSS within the iframe (if same-origin) to set `display:none` on the navigation and footer elements
5. IF the production server's X-Frame-Options or Content-Security-Policy headers prevent embedding, THEN THE Documentation_Site SHALL display a fallback message with a direct link to https://production.pathwayanalytics.com/public/configuration opening in a new browser tab
6. THE page SHALL include a brief introductory paragraph above the iframe explaining what the tariff configurations list shows and how to search/filter within it
7. THE iframe SHALL include a `title` attribute describing its content for accessibility (e.g., "Available Tariff Configurations from Pathway Analytics")

### Requirement 21: Embedded Pathways Reference Page

**User Story:** As a Commissioner or Provider, I want to view the reference pathway costing breakdowns directly within the documentation site, so that I can understand the activity-based costing model without navigating to a separate application.

#### Acceptance Criteria

1. THE Documentation_Site SHALL include a page at path `sexual-health-tariff/pathways` accessible from the Sexual Health Tariff Sidebar, labelled "Pathways"
2. THE Documentation_Site SHALL embed the pathways content from https://production.pathwayanalytics.com/public/pathway/100 using an iframe element
3. THE iframe SHALL be styled to fill the available content width (100%) and have a minimum height of 800 pixels, expanding to accommodate the embedded content
4. THE iframe SHALL hide the production site's native navigation header and footer, achieved either by targeting a specific section via a URL fragment/parameter supported by the production app, or by using CSS within the iframe (if same-origin) to set `display:none` on the navigation and footer elements
5. IF the production server's X-Frame-Options or Content-Security-Policy headers prevent embedding, THEN THE Documentation_Site SHALL display a fallback message with a direct link to https://production.pathwayanalytics.com/public/pathway/100 opening in a new browser tab
6. THE page SHALL include a brief introductory paragraph above the iframe explaining what the pathways reference page shows, including the activity-based costing model with steps, clinical resources, consumables, and cost breakdowns
7. THE iframe SHALL include a `title` attribute describing its content for accessibility (e.g., "Sexual Health Pathway Costing Reference")
8. THE embedded page SHALL allow the Visitor to use the pathway search functionality within the iframe to navigate between different pathways

### Requirement 19: Style Guide Section

**User Story:** As a content author or developer, I want a published style guide section on the site documenting the design system choices, so that I can create consistent content and understand the visual language used across the site.

#### Acceptance Criteria

1. THE Documentation_Site SHALL include a Style Guide section accessible via a link in the footer area (not the Navbar), routing to the `style-guide` path
2. THE Style Guide section SHALL document the colour palette including: primary colour (#1f4788), primary hover colour (#0056b3), accent colours, light mode background (#ffffff), dark mode background (#121212), text colours for both modes, and border colours — each presented as a named swatch with hex value
3. THE Style Guide section SHALL document the typography system including: font family (Roboto with fallbacks), font weights used (400, 500, 700), heading sizes (h1 at 2em+, h2 at 1.5em+, h3 at 1.25em+), body text size, and line-height (1.6–1.8)
4. THE Style Guide section SHALL document the spacing scale (8px, 16px, 24px, 32px, 48px) with visual examples of each increment applied to margins and padding
5. THE Style Guide section SHALL document UI component patterns used across the site including: navigation cards, blockquotes, code blocks, image captions, buttons/CTAs, and the edit suggestion link — with rendered examples of each
6. THE Style Guide section SHALL document the icon usage including: GitHub icons, external link indicators, dark mode toggle icon, and any other icons used across the site
7. THE Style Guide section SHALL document the dark mode colour mappings showing light mode values alongside their dark mode equivalents
8. THE Style Guide section SHALL be authored as Markdown files within a `style-guide/` directory and rendered with a full-width layout (no sidebar), consistent with other non-technical sections
