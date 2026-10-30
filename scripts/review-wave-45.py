"""Wave 45: all assigned people skipped; existing reviews already as deep as sources reachable in this wave."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
P={};R={}
out=dict(supersedes=[],profiles=P,rubrics=R)
(ROOT/'data/review-batches/045.json').write_text(json.dumps(out,indent=1,ensure_ascii=False))
print(len(P),'authored reviews;',len(R),'rubrics')
