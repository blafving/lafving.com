#!/usr/bin/env python3
"""Generate child entry HTML pages from md files for lafving.com."""

import os
import re
import yaml

BASE = "/Users/blafving/Dev/lafving.com"
PAGES = f"{BASE}/pages"
SITEMAP = f"{BASE}/sitemap"

# Common CSS for all child pages
CSS = """
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    :root {
      --bg: #0b0f15; --bg-2: #111620; --bg-3: #181e2a; --bg-4: #1e2535;
      --border: rgba(148,180,220,0.09); --border-hi: rgba(148,180,220,0.18);
      --cyan: #4fc3f7; --cyan-dim: rgba(79,195,247,0.10);
      --amber: #e8a048; --amber-dim: rgba(232,160,72,0.10);
      --pink: #f06292; --pink-dim: rgba(240,98,146,0.10);
      --green: #4dd0a8; --green-dim: rgba(77,208,168,0.10);
      --text: #e4e8ef; --lead: #ccd6e0; --tagline: #b8c4d0;
      --prose: #b0bcc9; --muted: #7a8799; --subdued: #5a6778;
      --mono: 'IBM Plex Mono', monospace;
      --display: 'Bricolage Grotesque', sans-serif;
      --body: 'DM Sans', sans-serif;
    }
    body { background: var(--bg); color: var(--text); font-family: var(--body); font-size: 16px; line-height: 1.7; }
    nav { position: fixed; top: 0; left: 0; right: 0; z-index: 100; display: flex; justify-content: space-between; align-items: center; padding: 0 48px; height: 60px; background: rgba(13,16,20,0.90); backdrop-filter: blur(16px); border-bottom: 0.5px solid var(--border); }
    .nav-logo { font-family: var(--mono); font-size: 12px; font-weight: 500; color: var(--cyan); letter-spacing: 0.12em; text-decoration: none; }
    .nav-links { display: flex; gap: 36px; list-style: none; }
    .nav-links a { font-family: var(--mono); font-size: 11px; color: var(--muted); text-decoration: none; letter-spacing: 0.08em; transition: color 0.2s; }
    .nav-links a:hover { color: var(--text); }
    .page-outer { padding-top: 60px; }
    .child-page { padding: 80px 48px; max-width: 800px; margin: 0 auto; }
    .page-label { font-family: var(--mono); font-size: 10px; color: var(--cyan); letter-spacing: 0.2em; text-transform: uppercase; margin-bottom: 40px; display: flex; align-items: center; gap: 10px; }
    .page-label::before { content: ''; display: inline-block; width: 20px; height: 0.5px; background: var(--cyan); opacity: 0.5; }
    .child-heading { font-family: var(--display); font-size: clamp(28px, 3.5vw, 42px); font-weight: 500; letter-spacing: -0.02em; line-height: 1.15; color: var(--text); margin-bottom: 24px; }
    .child-meta { font-family: var(--mono); font-size: 11px; color: var(--muted); letter-spacing: 0.06em; margin-bottom: 32px; }
    .child-body p { font-size: 16px; color: var(--prose); line-height: 1.85; margin-bottom: 22px; }
    .child-body p:first-child { font-size: 19px; font-weight: 300; color: var(--lead); line-height: 1.75; }
    .child-body .pull { font-family: var(--display); font-size: 22px; font-weight: 300; color: var(--cyan); line-height: 1.5; border-left: 2px solid var(--cyan); padding-left: 20px; margin: 32px 0; opacity: 0.85; }
    .child-body ul { margin: 0 0 22px 20px; color: var(--prose); line-height: 1.7; }
    .child-body li { margin-bottom: 6px; }
    .child-body blockquote { border-left: 2px solid var(--cyan); padding-left: 20px; margin: 22px 0; color: var(--lead); }
    .chip-row { display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 12px; }
    .skill-chip { font-family: var(--mono); font-size: 10px; color: var(--muted); border: 0.5px solid var(--border-hi); border-radius: 3px; padding: 4px 10px; letter-spacing: 0.04em; }
    .outcome-chip { font-family: var(--mono); font-size: 10px; color: var(--amber); background: var(--amber-dim); border: 0.5px solid rgba(232,160,72,0.2); border-radius: 3px; padding: 4px 10px; letter-spacing: 0.04em; }
    .stack-chip { font-family: var(--mono); font-size: 10px; color: var(--green); border: 0.5px solid rgba(77,208,168,0.2); border-radius: 3px; padding: 4px 10px; letter-spacing: 0.04em; }
    .learnings-box { margin: 32px 0; padding: 20px 24px; border: 0.5px solid var(--border); border-radius: 6px; background: var(--bg-2); font-family: var(--mono); font-size: 13px; color: var(--prose); line-height: 1.7; }
    .learnings-box-label { font-size: 10px; color: var(--subdued); letter-spacing: 0.14em; text-transform: uppercase; margin-bottom: 12px; }
    .back-link { display: inline-block; font-family: var(--mono); font-size: 11px; color: var(--muted); text-decoration: none; letter-spacing: 0.06em; margin-bottom: 32px; }
    .back-link:hover { color: var(--cyan); }
    footer { background: var(--bg); border-top: 0.5px solid var(--border); padding: 24px 48px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 12px; }
    .footer-links { display: flex; gap: 28px; }
    .footer-links a { font-family: var(--mono); font-size: 11px; color: var(--subdued); text-decoration: none; letter-spacing: 0.06em; transition: color 0.2s; }
    .footer-links a:hover { color: var(--muted); }
    @media (max-width: 680px) { nav { padding: 0 20px; } .child-page { padding: 56px 20px; } footer { padding: 20px; } }
"""

NAV_HTML = """  <nav>
    <a class="nav-logo" href="../index.html">LAFVING.COM</a>
    <ul class="nav-links">
      <li><a href="about.html">about</a></li>
      <li><a href="products.html">products</a></li>
      <li><a href="projects.html">projects</a></li>
      <li><a href="talks.html">talks</a></li>
      <li><a href="ideas.html">ideas</a></li>
      <li><a href="stories.html">stories</a></li>
      <li><a href="prototypes.html">prototypes</a></li>
    </ul>
  </nav>"""

FOOTER_HTML = """  <footer>
    <div></div>
    <div class="footer-links">
      <a href="about.html">about</a>
      <a href="products.html">products</a>
      <a href="projects.html">projects</a>
      <a href="talks.html">talks</a>
      <a href="ideas.html">ideas</a>
      <a href="stories.html">stories</a>
      <a href="prototypes.html">prototypes</a>
    </div>
  </footer>"""

NAV_LINKS = {
    "products": "products.html",
    "projects": "projects.html",
    "talks": "talks.html",
    "ideas": "ideas.html",
    "stories": "stories.html",
    "prototypes": "prototypes.html",
}


def parse_md(filepath):
    """Parse a markdown file and return (frontmatter_dict, body_lines)."""
    with open(filepath) as f:
        content = f.read()
    lines = content.strip().split('\n')
    fm = {}
    body_start = 0
    in_fm = False
    fm_lines = []
    for i, line in enumerate(lines):
        if line.strip() == '---':
            if not in_fm:
                in_fm = True
                continue
            else:
                body_start = i + 1
                break
        if in_fm:
            fm_lines.append(line)
    try:
        fm = yaml.safe_load('\n'.join(fm_lines))
    except Exception:
        fm = {}
    body = '\n'.join(lines[body_start:]) if body_start < len(lines) else ""
    return fm, body


def generate_product_page(fm, body, output_path):
    """Generate a product child page."""
    name = fm.get('name', 'Product')
    org = fm.get('org', '')
    date_start = fm.get('date_start', '')
    date_end = fm.get('date_end', 'Present')
    accent = fm.get('accent', 'cyan')
    skills = fm.get('skills', [])
    outcomes = fm.get('outcomes', [])

    accent_class = f"accent-{accent}" if accent in ['cyan','amber','pink','green'] else 'accent-cyan'

    skills_html = ""
    if skills:
        chips = " ".join(f'<span class="skill-chip">{s}</span>' for s in skills)
        skills_html = f'<div class="chip-row">{chips}</div>'

    outcomes_html = ""
    if outcomes:
        chips = " ".join(f'<span class="outcome-chip">{o}</span>' for o in outcomes)
        outcomes_html = f'<div class="chip-row">{chips}</div>'

    meta = f"{org} &nbsp;·&nbsp; {date_start} – {date_end}"

    page = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{name} — Products | Brandon Lafving</title>
  <link rel="stylesheet" href="../fonts.css" />
  <style>
{CSS}
  </style>
</head>
<body>
{NAV_HTML}
  <div class="page-outer">
    <div class="child-page">
      <a href="../products.html" class="back-link">← products</a>
      <p class="page-label">product</p>
      <h1 class="child-heading">{name}</h1>
      <div class="child-meta">{meta}</div>
      <div class="child-body">
{body}
      </div>
      <div class="chip-row" style="margin-top:32px;">
        {skills_html}
      </div>
{f'<div class="chip-row">' + ''.join(f'<span class="outcome-chip">{o}</span>' for o in outcomes) + '</div>' if outcomes else ''}
    </div>
  </div>
{FOOTER_HTML}
</body>
</html>"""
    with open(output_path, 'w') as f:
        f.write(page)
    print(f"  Created: {output_path}")


def generate_project_page(fm, body, output_path):
    """Generate a project child page."""
    name = fm.get('name', 'Project')
    org = fm.get('org', '')
    date_start = fm.get('date_start', '')
    date_end = fm.get('date_end', 'Present')
    role = fm.get('role', '')
    skills = fm.get('skills', [])
    outcomes = fm.get('outcomes', [])

    role_html = f'<div style="color:var(--amber);font-family:var(--mono);font-size:11px;margin-bottom:8px;">{role}</div>' if role else ""

    skills_html = ""
    if skills:
        chips = " ".join(f'<span class="skill-chip">{s}</span>' for s in skills)
        skills_html = f'<div class="chip-row">{chips}</div>'

    outcomes_html = ""
    if outcomes:
        chips = " ".join(f'<span class="outcome-chip">{o}</span>' for o in outcomes)
        outcomes_html = f'<div class="chip-row">{chips}</div>'

    meta = f"{org} &nbsp;·&nbsp; {date_start} – {date_end}"

    page = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{name} — Projects | Brandon Lafving</title>
  <link rel="stylesheet" href="../fonts.css" />
  <style>
{CSS}
  </style>
</head>
<body>
{NAV_HTML}
  <div class="page-outer">
    <div class="child-page">
      <a href="../projects.html" class="back-link">← projects</a>
      <p class="page-label">project</p>
      <h1 class="child-heading">{name}</h1>
      <div class="child-meta">{meta}</div>
      {role_html}
      <div class="child-body">
{body}
      </div>
      <div class="chip-row" style="margin-top:32px;">
        {skills_html}
      </div>
{outcomes_html}
    </div>
  </div>
{FOOTER_HTML}
</body>
</html>"""
    with open(output_path, 'w') as f:
        f.write(page)
    print(f"  Created: {output_path}")


def generate_talk_page(fm, body, output_path):
    """Generate a talk child page."""
    title = fm.get('title', '')
    talk_type = fm.get('type', 'talk')
    date = fm.get('date', '')
    venue = fm.get('venue', '')
    featured = fm.get('featured', False)
    badge = fm.get('badge', '')

    badge_html = ""
    if badge:
        badge_class = f"badge-{badge}" if badge in ['featured','workshop'] else ''
        badge_html = f'<span class="talk-badge {badge_class}" style="margin-bottom:24px;display:inline-block;">{badge}</span>'

    meta = f"{date} &nbsp;·&nbsp; {talk_type} &nbsp;·&nbsp; {venue}"

    page = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title} — Talks | Brandon Lafving</title>
  <link rel="stylesheet" href="../fonts.css" />
  <style>
{CSS}
  </style>
</head>
<body>
{NAV_HTML}
  <div class="page-outer">
    <div class="child-page">
      <a href="../talks.html" class="back-link">← talks</a>
      <p class="page-label">talk</p>
      <h1 class="child-heading">{title}</h1>
      {badge_html}
      <div class="child-meta">{meta}</div>
      <div class="child-body">
{body}
      </div>
    </div>
  </div>
{FOOTER_HTML}
</body>
</html>"""
    with open(output_path, 'w') as f:
        f.write(page)
    print(f"  Created: {output_path}")


def generate_idea_page(fm, body, output_path):
    """Generate an idea child page."""
    title = fm.get('title', '')
    idea_type = fm.get('type', 'essay')
    status = fm.get('status', '')
    description = fm.get('description', '')

    type_map = {
        'essay': ('type-essay', 'Essay'),
        'experiment': ('type-exp', 'Experiment'),
        'product-idea': ('type-product', 'Product idea'),
        'research': ('type-research', 'Research'),
    }
    type_class, type_label = type_map.get(idea_type, ('type-essay', 'Essay'))

    status_display = f"// {status}" if status else ""

    desc_html = f'<div style="font-size:14px;color:var(--muted);font-family:var(--mono);letter-spacing:0.04em;margin-bottom:32px;line-height:1.7;">{description}</div>' if description else ""
    status_html = f'<div style="font-family:var(--mono);font-size:10px;color:var(--muted);letter-spacing:0.06em;margin-top:32px;">{status_display}</div>' if status else ""

    page = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title} — Ideas | Brandon Lafving</title>
  <link rel="stylesheet" href="../fonts.css" />
  <style>
{CSS}
  </style>
</head>
<body>
{NAV_HTML}
  <div class="page-outer">
    <div class="child-page">
      <a href="../ideas.html" class="back-link">← ideas</a>
      <p class="page-label">idea</p>
      <div class="idea-type {type_class}" style="margin-bottom:12px;">{type_label}</div>
      <h1 class="child-heading">{title}</h1>
      {desc_html}
      <div class="child-body">
{body}
      </div>
{status_html}
    </div>
  </div>
{FOOTER_HTML}
</body>
</html>"""
    with open(output_path, 'w') as f:
        f.write(page)
    print(f"  Created: {output_path}")


def generate_story_page(fm, body, output_path):
    """Generate a story child page."""
    title = fm.get('title', '')
    subject = fm.get('subject', 'self')
    era = fm.get('era', '')
    timeframe = fm.get('timeframe', '')
    tags = fm.get('tags', [])

    era_label = era if era else (timeframe if timeframe else '')
    meta_parts = []
    if era_label:
        meta_parts.append(era_label.title())
    if subject:
        meta_parts.append(subject.title())
    meta = " &nbsp;·&nbsp; ".join(meta_parts)

    tags_html = ""
    if tags:
        tag_chips = " ".join(f'<span class="story-tag">{t}</span>' for t in tags)
        tags_html = f'<div class="story-tags">{tag_chips}</div>'

    story_type = "biography" if subject == 'self' else "essay"

    page = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title} — Stories | Brandon Lafving</title>
  <link rel="stylesheet" href="../fonts.css" />
  <style>
{CSS}
    .story-tag {{ font-family: var(--mono); font-size: 9px; color: var(--cyan); opacity: 0.6; letter-spacing: 0.06em; }}
    .story-tags {{ display: flex; flex-wrap: wrap; gap: 6px; margin-top: 12px; }}
  </style>
</head>
<body>
{NAV_HTML}
  <div class="page-outer">
    <div class="child-page">
      <a href="../stories.html" class="back-link">← stories</a>
      <p class="page-label">story</p>
      <h1 class="child-heading">{title}</h1>
      <div class="child-meta">{meta}</div>
      <div class="child-body">
{body}
      </div>
      {tags_html}
    </div>
  </div>
{FOOTER_HTML}
</body>
</html>"""
    with open(output_path, 'w') as f:
        f.write(page)
    print(f"  Created: {output_path}")


def generate_prototype_page(fm, body, output_path):
    """Generate a prototype child page."""
    name = fm.get('name', 'Prototype')
    kind = fm.get('kind', 'tool')
    status = fm.get('status', '')
    description = fm.get('description', '')
    stack = fm.get('stack', [])
    learnings = fm.get('learnings', '')

    status_display = f"// {status}" if status else ""

    stack_html = ""
    if stack:
        chips = " ".join(f'<span class="stack-chip">{s}</span>' for s in stack)
        stack_html = f'<div class="chip-row">{chips}</div>'

    learnings_html = ""
    if learnings:
        learnings_html = f'''      <div class="learnings-box">
        <div class="learnings-box-label">Learnings</div>
        {learnings}
      </div>'''

    meta = f"{kind} &nbsp;·&nbsp; {status_display}"

    page = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{name} — Prototypes | Brandon Lafving</title>
  <link rel="stylesheet" href="../fonts.css" />
  <style>
{CSS}
  </style>
</head>
<body>
{NAV_HTML}
  <div class="page-outer">
    <div class="child-page">
      <a href="../prototypes.html" class="back-link">← prototypes</a>
      <p class="page-label">prototype</p>
      <h1 class="child-heading">{name}</h1>
      <div class="child-meta">{meta}</div>
      <div class="child-body">
{body}
      </div>
      {stack_html}
{learnings_html}
    </div>
  </div>
{FOOTER_HTML}
</body>
</html>"""
    with open(output_path, 'w') as f:
        f.write(page)
    print(f"  Created: {output_path}")


# --- Run generation ---

collections = {
    "products": {
        "dir": "product",
        "folder": "products",
        "generator": generate_product_page,
    },
    "projects": {
        "dir": "project",
        "folder": "projects",
        "generator": generate_project_page,
    },
    "talks": {
        "dir": "talk",
        "folder": "talks",
        "generator": generate_talk_page,
    },
    "ideas": {
        "dir": "idea",
        "folder": "ideas",
        "generator": generate_idea_page,
    },
    "stories": {
        "dir": "story",
        "folder": "stories",
        "generator": generate_story_page,
    },
    "prototypes": {
        "dir": "prototype",
        "folder": "prototypes",
        "generator": generate_prototype_page,
    },
}

created = []
for collection_name, config in collections.items():
    folder = config["folder"]
    out_dir = f"{PAGES}/{config['dir']}"
    src_dir = f"{SITEMAP}/{folder}"

    print(f"\n=== {folder} ===")
    for filename in sorted(os.listdir(src_dir)):
        if not filename.endswith('.md') or filename == 'template.md':
            continue
        src_path = os.path.join(src_dir, filename)
        slug = filename.replace('.md', '')
        out_path = os.path.join(out_dir, f"{slug}.html")

        fm, body = parse_md(src_path)
        config["generator"](fm, body, out_path)
        created.append(out_path)

print(f"\n--- Total: {len(created)} child pages created ---")
