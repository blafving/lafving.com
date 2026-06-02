# Index Integration Brief

## Goal
Update `index.html` (1558 lines) to be a landing page with concise teasers that link to sub-pages. Preserve existing nav, hero, pitch (bubbles), connect, footer, and ALL CSS/JS.

## What to KEEP (unchanged)
- `<head>` — meta tags, og/twitter, fonts.css, all `<style>` CSS, schema.org JSON-LD
- Nav — `<nav id="site-nav">` with all links and hamburger toggle
- Hero — `.hero` section with eyebrow, name, tagline, CTAs
- Pitch — `#pitch` div with all thought bubbles
- Footer — with links and status
- Connect section — `#connect` with email/social
- ALL CSS — every class definition, animation, responsive breakpoint
- ALL JS — hamburger toggle, scroll spy at bottom of file

## What to REPLACE with teaser cards/sections
Replace the inline sections with compact teasers that link to sub-pages. Use the existing CSS classes where possible (`.section-outer`, `section`, `.section-label`, `.section-heading`), but adapt for condensed view.

### 1. About → single teaser card
Link: `pages/about.html`
Text (2-3 sentences): "AI product owner at Wharton. Princeton '06, fencer, writer. Building at the intersection of language, technology, and human need."
CTA: "Read about →"

### 2. Products → 3 mini cards in a row (inline-grid or flex)
Section label: "products"
Heading: "Things I own"
Cards link to:
- `pages/product/lecture-recall.html` — "Lecture Recall · Wharton 2023–Present" — "Custom AI course chatbot built on vector DB of transcripts."
- `pages/product/facelect.html` — "Facelect · Wharton 2022–Present" — "Private elections app, 2× usage growth."
- `pages/product/attendance-class-recording.html` — "Attendance & Class Recording · Wharton" — "School-wide attendance system shipped by vendor."

### 3. Projects → 3 mini items
Section label: "projects"
Heading: "Strategic work"
Items link to:
- `pages/project/ethan-mollick-genai-lab.html` — "Ethan Mollick GenAI Lab · Wharton 2025"
- `pages/project/adieu-active-directory.html` — "ADIEU AD Migration · UPenn"
- `pages/project/stratacache-digital-marketing.html` — "STRATACACHE Digital Marketing · 2019"

### 4. Talks → single teaser card
Link: `pages/talks.html`
Text: "Keynotes, talks, and workshops on GenAI, RAG, and building in the AI era."
CTA: "See talks →"

### 5. Stories → 2-row grid of mini cards
Section label: "stories"
Heading: "Stories"
Cards link to:
- `pages/story/at-wharton.html` — "At Wharton"
- `pages/story/keeping-up-with-ai.html` — "Keeping Up With AI"
- `pages/story/dallas-to-princeton.html` — "Dallas to Princeton"
- `pages/story/decade-of-writing.html` — "Decade of Writing"
- `pages/story/fencer-to-product-owner.html` — "Fencer to Product Owner"
- `pages/story/what-im-looking-for.html` — "What I'm Looking For"
- `pages/story/what-it-takes.html` — "What It Takes"

### 6. Prototypes → single teaser card
Link: `pages/prototypes.html`
Text: "Homegrown experiments and tools — research knowledge graph, CLI tools, agent harnesses."
CTA: "Explore prototypes →"

### 7. Ideas → single teaser card
Link: `pages/ideas.html`
Text: "Lab notebook — essays, experiments, and product ideas on AI, agents, and building."
CTA: "Read ideas →"

## Design constraints
- Use existing CSS color variables, font families, section labels (`.section-label` with cyan accent and line)
- Teaser cards should use `.product-card` style (bg-2, border, hover state) but be more compact
- Each teaser section should have: section-label (lowercase, cyan), optional short heading, compact content, CTA link styled as mono text with arrow
- Don't add new CSS class names unless necessary. Reuse existing `.product-card`, `.section-outer`, `section`, `.section-label`, `.section-heading`, `.btn-outline`
- The connect section should remain unchanged
- The nav should have links updated to point to sub-pages instead of #anchor: about.html, products.html, projects.html, talks.html, stories.html, prototypes.html, ideas.html, connect (connect stays #anchor or to about.html)

## File location
/Users/blafving/Dev/lafving.com/index.html

## Sub-page URL patterns
- Products: pages/product/{slug}.html
- Projects: pages/project/{slug}.html
- Ideas: pages/idea/{slug}.html
- Stories: pages/story/{slug}.html
- Prototypes: pages/prototype/{slug}.html
- Talks: pages/talk/{slug}.html
- About: pages/about.html
- Index listing pages: pages/products.html, pages/projects.html, etc.
