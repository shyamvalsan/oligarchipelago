"""Wave 42: no reviews authored. Existing profiles for the nine assigned people were already as well sourced as what could be opened in this wave."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
P={};R={}
ids={p['id'] for p in json.loads((ROOT/'data/billionaires.json').read_text())['people']}
assert set(P)<=ids
out=dict(supersedes=[],profiles=P,rubrics=R)
(ROOT/'data/review-batches/042.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(len(P),'authored reviews;',len(R),'rubrics')
