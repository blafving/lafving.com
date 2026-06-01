# lafving.com — Design System

**Version:** 1.0 · April 2026  
**Site:** Single-page portfolio for Brandon Lafving — AI product owner / PM  
**Aesthetic:** Dark gallery. Content is spotlit against deep backgrounds, like exhibits in a well-lit museum. Sophisticated, curated, prose-forward. Stands apart from typical tech portfolio aesthetics (neither flat dark mode nor corporate light).

---

## Design Language

The site operates on three principles:

**Depth through layers, not shadow.** There are no drop shadows anywhere. Depth is created by stacking three background tones — a near-black base, a slightly lighter card surface, and a hover-state lift — with hairline 0.5px borders to define edges.

**Mono for metadata, display for headlines, sans for prose.** Three typefaces with strict roles. IBM Plex Mono signals system/technical context (labels, chips, nav, dates). Bricolage Grotesque is the expressive voice (names, headings, pull quotes). DM Sans handles all reading copy.

**Color signals role, not decoration.** Cyan is the primary interactive/identity color — it owns headings, links, and hover states. Amber is secondary — metadata, dates, secondary labels. Pink and green appear only for categorization (product cards, badges). Everything else is a shade of cool grey.

---

## Color Tokens

### Backgrounds
| Token | Value | Use |
|---|---|---|
| `--bg` | `#0d1014` | Page background, nav, footer |
| `--bg-2` | `#13171d` | Card surfaces, sidebar blocks |
| `--bg-3` | `#1a1f27` | Hover state for cards |

### Borders
| Token | Value | Use |
|---|---|---|
| `--border` | `rgba(255,255,255,0.07)` | Default hairline — section dividers, card edges |
| `--border-hi` | `rgba(255,255,255,0.14)` | Hover/active border on interactive elements |

### Accent Colors
| Token | Value | Role |
|---|---|---|
| `--cyan` | `#4fc3f7` | **Primary accent** — headings, links, interactive, nav logo |
| `--cyan-dim` | `rgba(79,195,247,0.10)` | Cyan tint for tag/chip backgrounds |
| `--amber` | `#e8a048` | **Secondary accent** — metadata, org labels, product accent |
| `--amber-dim` | `rgba(232,160,72,0.10)` | Amber tint |
| `--pink` | `#f06292` | **Tertiary** — product card accent bar (categorization only) |
| `--pink-dim` | `rgba(240,98,146,0.10)` | Pink tint |
| `--green` | `#4dd0a8` | **Status / active** — pulsing dot, workshop badge, card accent |
| `--green-dim` | `rgba(77,208,168,0.10)` | Green tint |

### Text Colors
| Token | Value | Use |
|---|---|---|
| `--text` | `#e4e8ef` | Primary text — titles, card names, body on dark |
| `--muted` | `#7a8799` | Secondary text — descriptions, meta, link values |
| `--faint` | `#3a4452` | Tertiary / decorative — kicker labels, dates, disabled states |
| *(unnamed)* | `#b8c4d0` | Warm light grey — hero tagline, connect prose, lead text |
| *(unnamed)* | `#b0bcc9` | Mid prose — pitch bubbles, about body paragraphs |
| *(unnamed)* | `#ccd6e0` | Bright prose — about first paragraph (lead-in) |

---

## Typography

### Typefaces
| Token | Family | Weights | Role |
|---|---|---|---|
| `--display` | Bricolage Grotesque | 300, 400, 500, 700 | Display — hero name, section headings, pull quotes, card names |
| `--body` | DM Sans | 300, 400, 500 (+ italic 300) | Prose — all reading copy, hero eyebrow |
| `--mono` | IBM Plex Mono | 400, 500 | System — nav, labels, chips, kickers, dates, section labels |

All fonts loaded from Google Fonts. Base font-size: **16px**. Base line-height: **1.7**.

### Type Scale
| Size | Font | Weight | Use |
|---|---|---|---|
| `clamp(54px, 7vw, 92px)` | Display | 700 | Hero name |
| `clamp(30px, 4.5vw, 56px)` | Display | 300 | Pitch opening question |
| `clamp(28px, 3.5vw, 42px)` | Display | 500 | Section headings |
| `22px` | Display | 300 | Pull quote (cyan, left-bordered) |
| `20px` | Display | 500 | Product card names |
| `19px` | Body | 300 | About first paragraph (lead-in) |
| `18px` | Body | 400 | Hero eyebrow |  
| `17px` | Body | 300 | Pitch body, connect prose, bubble text |
| `16px` | Body | 400 | About prose body, ideas intro |
| `15px` | Body | 300 | Project descriptions, pitch close (italic) |
| `14px` | Body | 400 | Product descriptions, project tags text, connect link values |
| `13px` | Body | 400 | Sidebar list items, idea descriptions |
| `12px` | Mono | 400 | Footer links, ideas note, nav logo |
| `11px` | Mono | 400 | Nav links, talk dates, talk venue, status bar text |
| `10px` | Mono | 400 | All micro labels — section label, product meta, kickers, chips, stat chips, risk numbers, sidebar labels, org tags, idea type, idea status, connect link label |

### Letter Spacing Conventions
- Display headings: `-0.025em` (tight)
- Body: `0` (default)
- Mono section labels: `0.20em` (wide)
- Mono kickers: `0.18em`
- Mono nav links: `0.08–0.12em`
- Mono chips: `0.04–0.10em`

---

## Spacing & Layout

### Page Structure
- Max content width: **1100px** (sections), **1200px** (pitch split bubbles), **680px** (hero content, bubble-center)
- Nav height: **60px** (fixed, sticky)
- Section padding (desktop): **80px 48px**
- Section padding (mobile ≤680px): **56px 20px**
- Nav padding (desktop): **0 48px**
- Nav padding (mobile): **0 20px**

### Grid & Gap Scale
| Context | Layout | Gap |
|---|---|---|
| About | `1fr 320px` (sidebar) | `64px` |
| Connect | `1fr 1fr` | `64px` |
| Pitch split bubbles | `1fr 1fr` | `64px` |
| Product grid | `repeat(auto-fit, minmax(300px, 1fr))` | `20px` |
| Ideas grid | `repeat(auto-fit, minmax(280px, 1fr))` | `16px` |
| Risk grid | `1fr 1fr` | `12px` |
| Project list | Single column | `0` (border-separated) |
| Talk list | `80px 1fr auto` | `24px` |

### Breakpoints
| Breakpoint | Changes |
|---|---|
| `≤900px` | About/Connect → single column; project item → single column; talk badge hidden |
| `≤680px` | Nav compressed; hero mask switches to vertical; sections → 20px horizontal padding; bubble split → single column; risk grid → single column |

### Border Radius Scale
- Buttons, chips, tags: **3px**
- Exhibit images, product cards: **4px**
- Idea cards, sidebar blocks, connect links, section labels (pill): **6px**
- Product cards: **8px**

---

## Borders & Dividers

All borders are **0.5px** — hairline throughout. No 1px borders.

- Section separators: `0.5px solid var(--border)` — horizontal rules between major page sections
- Card edges: `0.5px solid var(--border)` at rest → `var(--border-hi)` on hover
- Nav bottom: `0.5px solid var(--border)`
- Footer top: `0.5px solid var(--border)`
- Pull quote left border: `2px solid var(--cyan)` — the only thick border in the system
- Project item rows: `0.5px solid var(--border)` (bottom only)
- Talk item rows: `0.5px solid var(--border)` (bottom only)

---

## Motion & Animation

### Entrance (Hero)
**fadeUp** keyframe: `opacity: 0, translateY: 20px` → `opacity: 1, translateY: 0`  
Duration: `0.6s`, easing: `ease`, applied with staggered `animation-fill-mode: forwards`

| Element | Delay |
|---|---|
| Hero eyebrow | `0.1s` |
| Hero name | `0.2s` |
| Hero tagline | `0.3s` |
| Hero CTAs | `0.5s` |

### Hover Transitions
- Color changes (links, nav, footer): `0.2s`
- Background/border changes (cards): `0.2s`
- Button lift (`translateY(-1px)`): `0.15s`

### Ambient Loops
| Animation | Duration | Easing | Effect |
|---|---|---|---|
| Status dot pulse | `2.5s` infinite | ease | Opacity 1 → 0.35 → 1 |
| CSS nebula breathe | `9s` infinite | ease-in-out | brightness/saturation ±14%/18% |

---

## Buttons

Two button styles, both using IBM Plex Mono at 11px/500 weight, 0.08em letter-spacing, 3px border-radius.

| Style | Background | Text | Border | Hover |
|---|---|---|---|---|
| **Primary** | `var(--cyan)` | `#0d1014` | none | `opacity: 0.85` + lift |
| **Outline** | transparent | `var(--cyan)` | `0.5px solid rgba(79,195,247,0.4)` | `var(--cyan-dim)` bg + lift |

Padding: `13px 26px`

---

## Accent Bar System (Product Cards)

Product cards use a 3×32px vertical accent bar at the top-left of each card to signal category:

| Color | Token |
|---|---|
| Cyan | `accent-cyan` |
| Amber | `accent-amber` |
| Pink | `accent-pink` |
| Green | `accent-green` |

---

## Backdrop & Blur

Nav uses `backdrop-filter: blur(16px)` with `background: rgba(13,16,20,0.90)` — frosted glass against page content when scrolled.

---

## Hero Image Treatment

The hero background image is masked with a left-to-right linear gradient:  
`transparent 0% → rgba(0,0,0,0.6) 28% → black 52%`

This lets copy sit on clean dark space (left) while the photo bleeds in on the right. On mobile (≤680px), the mask switches to vertical (`transparent 0% → black 50%`) and opacity drops to 0.3 — the photo becomes a subtle texture behind the text rather than a compositional element.

---

## CSS Nebula (Pitch Section)

Bubble 3 uses a pure-CSS "nebula" exhibit — layered radial gradients in purple, blue, and magenta on a near-black base, with a slow breathing animation. No external image dependency. Sits in a `400px` tall container.

---

## Section Label Pattern

All section labels (about, products, projects, etc.) use:
- IBM Plex Mono, 10px, 0.20em letter-spacing, all-caps
- `var(--cyan)` color
- A 20×0.5px cyan line before the text (via `::before`)

---

## Nav

Fixed, full-width. Logo left (`LAFVING.COM`, Mono 12px, cyan, 0.12em tracking). Links right (Mono 11px, `--muted` at rest → `--text` on hover, 0.08em tracking, 36px gap desktop / 20px mobile).

**Known gap:** No mobile hamburger menu. At viewports ≤~400px the nav links will overflow. This is an open pre-launch issue.
