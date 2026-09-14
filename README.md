# Universal Master Prompt Library

A GitHub-ready, model-agnostic Markdown prompt repository intended to cover the major tasks, professions, life needs and industries for which people use AI. It combines a normalized universal taxonomy with a pinned, complete snapshot of AJ Geddes's MIT-licensed `useful-ai-prompts` prompt collection.

## What is included

- **159 normalized sector starters** across eight collections.
- **All 679 prompt records** from the pinned upstream AJ Geddes snapshot.
- **All 47 upstream top-level prompt categories**, unchanged under `upstream/`.
- Human-readable, JSON and CSV catalogs.
- ChatGPT, Claude, Grok and generic-agent project instructions.
- Templates, validation scripts, source tracking, licensing notices and CI.
- Official-world-industry coverage using all 22 top-level ISIC Revision 5 sections.

## Important definition

No finite folder tree can literally represent every possible human activity. “Universal coverage” here means three complementary axes: reusable task methods, personal/professional domains, and all top-level world economic activity sections. New specialties can be added without changing the architecture.

## Start here

1. Search `CATALOG.md` or `catalog.json`.
2. Select the narrowest normalized sector under `prompts/`.
3. Use its `sector-expert.md`, or create a narrow task prompt from `templates/prompt-template.md`.
4. Search the complete upstream snapshot when a ready-made prompt may already exist.
5. Test, review and version prompts before high-consequence use.

## Search examples

```bash
python3 scripts/search.py "uvm coverage"
python3 scripts/search.py "healthcare operations"
python3 scripts/search.py "supply chain risk"
```

## Safety

Do not commit secrets, unpublished employer information, confidential semiconductor designs, personal medical identifiers, passport data or children's private information. Health, legal, financial, safety and emergency prompts provide research and preparation support—not professional authorization or emergency response.

## Licensing

Original scaffold files are CC0-1.0. The complete imported AJ Geddes prompt snapshot remains MIT-licensed; see `THIRD_PARTY_NOTICES.md` and the upstream license.
