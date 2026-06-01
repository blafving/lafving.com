# lafving.com — Content Model

**Version:** 0.1 · derived from Resume - IT Product Owner 2026 + index.html

Site is a curated, prose-forward portfolio. Five content types. Each type lives in its own folder with a `template.md` defining required + optional fields. Entries are markdown files with YAML frontmatter.

---

## Types

### 1. product
Things Brandon owns — built, shipped, and still responsible for. The visible deliverables of his career.

**Required fields:** `name`, `org`, `date_start`, `description`
**Optional:** `date_end` (omit = "Present"), `accent` (cyan/amber/pink/green), `stats[]`, `status` (active/maintained/sunset), `links[]`

**Examples:** Lecture Recall, Facelect, Attendance & Class Recording.

---

### 2. project
Strategic initiatives, partnerships, complex org problems navigated. Less "owned product," more "moved a thing through an organization." Shorter shelf life than products, often time-boxed.

**Required fields:** `name`, `org`, `date_start`, `description`
**Optional:** `date_end`, `tags[]`, `role`, `outcome`

**Examples:** Ethan Mollick GenAI Lab, ADIEU AD migration, STRATACACHE digital marketing.

---

### 3. idea
Lab notebook. Essays, experiments, half-formed product ideas, published research — anything Brandon is turning over in writing.

**Required fields:** `title`, `type` (essay / experiment / product-idea / research), `description`, `status` (in-progress / ongoing / drafting / outline / writing-up / shipped)
**Optional:** `tags[]`, `published_at`, `link`

**Examples:** "What does it mean to think with a machine?", "Claude vs. Codex vs. Opencode."

---

### 4. prototype
Homegrown experiments — code, tools, or systems Brandon builds for himself. Distinct from `product` (institutional ownership) and `idea` (writing). First entry: **prototypes/research** — the unified research database that this site sits inside.

**Required fields:** `name`, `kind` (tool / system / experiment / research-vault), `description`, `status` (concept / building / running / archived)
**Optional:** `stack[]`, `learnings`, `repo_link`, `live_link`

**Examples:** prototypes/research (this), future agent harnesses, CLI tools, etc.

---

### 5. story
Narrative content. Two subjects:
- **self** — autobiographical (default for /about page)
- **technology** — past, present, or future of tech, told as narrative rather than analysis

**Required fields:** `title`, `subject` (self / technology), `body`
**Optional:** `timeframe` (past / present / future) — applies to technology stories, `era` — applies to self-stories (childhood / academic / early-career / current), `tags[]`

The `/about` page filters `subject = self` by default. Filter toggle reveals `subject = technology` stories.

---

## Folder Layout

```
sitemap/
├── CONTENT-MODEL.md            (this file)
├── about.md                    (retained — short intro/bio)
├── homepage/
│   ├── template.md
│   └── homepage.md             (hero + pitch sequence definition)
├── products/
│   ├── template.md
│   └── <slug>.md per entry
├── projects/
│   ├── template.md
│   └── <slug>.md per entry
├── ideas/
│   ├── template.md
│   └── <slug>.md per entry
├── prototypes/
│   ├── template.md
│   └── <slug>.md per entry
└── stories/
    ├── template.md
    └── <slug>.md per entry
```

---

## Notes

- **Slugs** are kebab-case derived from name/title.
- **Frontmatter** parsed as YAML.
- **Body** is markdown — used as the long-form description in rendered HTML.
- **No images** in current iteration. Communication-only. Visual exhibits (nebula, hand) handled by design system, not content.
- Talks remain inline in homepage for now (low-volume, reverse-chronological list). Promote to own type if it grows.

---

### 6. talk
Keynotes, talks, workshops. Events where Brandon presents. Linked to related products/projects/ideas.

**Required fields:** `title`, `type` (keynote / talk / workshop), `date`, `venue`, `description`
**Optional:** `featured` (bool), `badge`, `connected_to[]`

**Examples:** "Infrastructure Is Critical to Strategy", "Slow Down Your Chatbot Build", "Failing 10× at Machine Learning".

---

## Cross-Content Linking: `connected_to`

All types (product, project, idea, prototype, story, talk) support optional `connected_to` field — an array of references to related content.

```yaml
connected_to:
  - type: project
    slug: ethan-mollick-genai-lab
  - type: talk
    slug: infrastructure-is-critical-to-strategy
```

This enables:
- Products → projects that created them → talks about those projects
- Projects → product outcomes → ideas that spawned them
- Ideas → products/prototypes built from them
- Talks → products/ideas they discuss

Homepage rendering can surface "related content" sections inline. Breadcrumbs work bidirectionally (project links to talk, talk links back to project).

---

## Folder Layout (Updated)

```
sitemap/
├── CONTENT-MODEL.md            (this file)
├── about.md                    (retained — short intro/bio)
├── homepage/
│   ├── template.md
│   └── homepage.md
├── products/
│   ├── template.md
│   └── <slug>.md per entry
├── projects/
│   ├── template.md
│   └── <slug>.md per entry
├── ideas/
│   ├── template.md
│   └── <slug>.md per entry
├── prototypes/
│   ├── template.md
│   └── <slug>.md per entry
├── talks/                      (NEW — previously inline on homepage)
│   ├── template.md
│   └── <slug>.md per entry
└── stories/
    ├── template.md
    └── <slug>.md per entry
```

---

## Open Questions for Brandon

1. Should talks remain inline on homepage (current state) or pull from `talks/` folder?
2. Any other cross-links you'd like surfaced (e.g., community → projects where you led)?
