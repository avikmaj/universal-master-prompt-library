from pathlib import Path
import json,sys
errors=[]
sector=list(Path("prompts").glob("*/*/sector-expert.md"))
if len(sector)!=175: errors.append(f"Expected 175 normalized sectors; found {len(sector)}")
required=["## Metadata","## Prompt","<role>","<task>","<output_specification>","<quality_criteria>","<constraints>"]
for f in sector:
 t=f.read_text()
 for x in required:
  if x not in t: errors.append(f"{f} missing {x}")
idx=json.loads(Path("upstream/aj-geddes-useful-ai-prompts/PROMPT-INDEX.json").read_text())
files=[p for p in Path("upstream/aj-geddes-useful-ai-prompts/prompts").rglob("*.md") if p.name!="README.md"]
if len(files)!=len(idx["prompts"]): errors.append(f"Upstream index/file mismatch: {len(idx['prompts'])}/{len(files)}")
print(f"Normalized sectors: {len(sector)}")
print(f"Upstream prompts: {len(files)}")
if errors: print("\n".join(errors)); sys.exit(1)
print("Validation passed")
