---
name: Research Vault
kind: research-vault
status: building
description: "A unified research database. Markdown article representations + AI-driven processing — currently local, moving toward a GCP-hosted web app with iPad UI."
stack:
  - "Markdown source-of-truth"
  - "Claude + agent processing"
  - "GCP (planned)"
  - "iPad-first web UI (planned)"
learnings: "Local markdown + agents proves the loop; the bottleneck is sync, search, and mobile access — solvable with cheap cloud primitives."
connected_to:
  - type: idea
    slug: bedrock-for-pms
  - type: product
    slug: lecture-recall
---

# Research Vault

A homegrown research system. Articles I find on the web get stored as markdown representations, then combined with AI-driven processing — summarization, tagging, cross-reference, semantic search.

Currently runs on my local machine with Claude and other agents. Migrating toward a GCP-backed app with an iPad-readable web UI so research can happen wherever I am. This site (lafving.com) is the same content model in miniature — products, projects, ideas, prototypes, stories — applied to my own work first.
