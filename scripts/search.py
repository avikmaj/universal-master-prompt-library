from pathlib import Path
import json,sys
q=" ".join(sys.argv[1:]).lower().strip()
if not q: raise SystemExit("Usage: python3 scripts/search.py <terms>")
terms=q.split(); hits=[]
for f in Path("prompts").rglob("sector-expert.md"):
    text=f.read_text(errors="ignore").lower(); score=sum(text.count(t) for t in terms)
    if score: hits.append((score,str(f),f.read_text(encoding="utf-8", errors="replace").splitlines()[0].removeprefix("# ")))
for f in Path("upstream/aj-geddes-useful-ai-prompts/prompts").rglob("*.md"):
    if f.name=="README.md": continue
    text=f.read_text(errors="ignore").lower(); score=sum(text.count(t) for t in terms)
    if score: hits.append((score,str(f),f.read_text(encoding="utf-8", errors="replace").splitlines()[0].removeprefix("# ")))
for score,path,title in sorted(hits,reverse=True)[:30]: print(f"{score:4}  {title}  [{path}]")
