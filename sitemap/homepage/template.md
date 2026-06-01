---
type: homepage
---

# Homepage Template

Single homepage entry. Defines the ordered narrative sequence shown on lafving.com root.

## Notes

Section content (products, projects, ideas, talks, prototypes, stories) auto-pulled from respective folders via type. Each entry's `connected_to` field surfaces related content inline (e.g., project talks, product ideas).

## Required Sections (in order)

1. **hero** — eyebrow + name + tagline + CTAs
2. **pitch** — drifting bubble sequence (question → exploration → risks → close)
3. **about** — link/excerpt to /about
4. **products** — grid of `products/*.md`
5. **projects** — list of `projects/*.md`
6. **talks** — inline list (until promoted to own type)
7. **ideas** — grid of `ideas/*.md`
8. **prototypes** — grid of `prototypes/*.md`
9. **connect** — CTA + links

## Frontmatter

```yaml
---
hero_eyebrow: string
hero_name: string
hero_tagline: string (multi-line ok)
hero_cta_primary: { label, href }
hero_cta_outline: { label, href }
pitch_question: string
pitch_bubbles: [{ kicker, body, exhibit }]
pitch_risks: [{ num, text }]
pitch_close: string
status_message: string
---
```
