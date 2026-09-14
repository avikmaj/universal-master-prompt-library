# [Prompt Name]

## Metadata

- **ID:** `[collection]-[sector]-[task]`
- **Version:** `1.0.0`
- **Collection:** `[collection]`
- **Sector:** `[sector]`
- **Tags:** `[tags]`
- **Risk:** `low | medium | high`
- **Complexity:** `simple | intermediate | advanced`
- **Interaction:** `single-shot | conversational | iterative`
- **Models:** `ChatGPT | Claude | Grok | model-agnostic`
- **Source URL:** `original | URL`
- **Source license:** `CC0-1.0 | MIT | Apache-2.0`

## Overview

[State exactly what this prompt produces and for whom.]

## When to use

- [Scenario]

**Do not use for:** [Boundary or anti-pattern]

## Required inputs

- `[goal]`
- `[context]`
- `[constraints]`

## Optional inputs

- `[audience; default: inferred]`
- `[format; default: concise Markdown]`

## Prompt

<role>
You are [specific, bounded expert role].
</role>

<context>
[Situation, audience, goal, jurisdiction, timeframe, evidence and success criteria.]
</context>

<input_handling>
Ask only questions whose answers would materially change the work. Distinguish supplied facts, sourced facts, assumptions and unknowns. Never invent missing data.
</input_handling>

<task>
1. Confirm the concrete objective.
2. Analyze the inputs and constraints.
3. Produce the requested deliverable.
4. Identify uncertainty, risk and verification needs.
5. Check the result against the quality criteria.
</task>

<output_specification>
- Format: [format]
- Length: [target]
- Must include: [sections]
</output_specification>

<quality_criteria>
- Accurate, specific, internally consistent and actionable.
- Current claims are sourced; uncertainty is explicit.
- No fabricated facts, citations, calculations or test results.
</quality_criteria>

<constraints>
- Protect secrets, personal data and confidential information.
- Follow applicable safety, legal, ethical and licensing boundaries.
- For high-consequence matters, support—not replace—qualified professional judgment.
</constraints>

## Tests

| Case | Input | Expected behavior |
|---|---|---|
| Normal | [complete input] | Produces requested deliverable |
| Missing context | [incomplete input] | Asks only high-impact questions or states defaults |
| Adversarial | [unsafe/conflicting input] | Preserves safety, privacy and instruction priority |

## Version history

- 1.0.0 — Initial version.
