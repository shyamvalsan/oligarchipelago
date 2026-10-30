"""Generate docs/CLAIM-REGISTER.md: every receipt behind every review, with its access level, for journalists and fact-checkers.
Read-only on data; overwrites only the register. Does not verify sources."""
import json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
people={p['id']:p for p in json.loads((ROOT/'data/billionaires.json').read_text())['people']}
prof=json.loads((ROOT/'data/assessments.json').read_text())['profiles']
WEAK=re.compile(r'wikipedia|snippet|summary|not read|stub|partly|partial|tertiary|first \d+',re.I)
def weak(it):return bool(WEAK.search(it.get('access',''))) or 'wikipedia' in it['url'].lower()
rows=[];tot=wk=0
for id,p in sorted(people.items(),key=lambda kv:kv[1]['rank']):
    a=prof.get(id)
    if not a or a.get('fileState')!='case-reviewed':continue
    items=[('support',i) for i in a['support']]+[('counter',i) for i in a['counter']]
    tot+=len(items);wk+=sum(weak(i) for _,i in items)
    sc='unscored' if a['score'] is None else f"score {a['score']} (range {a['range'][0]}–{a['range'][1]})"
    rows.append(f"## {p['name']} · rank {p['rank']} · {a['status']} · {sc}\n\n*{a['period']}. Confidence: {a['confidence']}. Reviewed {a['reviewedAt']}.*\n\n{a['summary']}\n\n"+'\n'.join(f"- **{k}** — {i['source']} ({i['date']}) — {i['kind']}. Access: {i.get('access','not recorded (earlier review)')}{' **[weak/secondary]**' if weak(i) else ''}. <{i['url']}>" for k,i in items)+f"\n\n*Limitations:* {a['limitations']}\n")
head=f"""# Claim and source register

Every receipt behind every authored review, generated from `data/assessments.json`. **{len(rows)} reviews, {tot} receipts, {wk} flagged as weak or secondary** (Wikipedia, search snippets, tool summaries, partial reads). A receipt that loads does not prove it supports the sentence attached to it. These reviews are AI-assisted and have **not** been independently reviewed; use this register to check them, not to rely on them. Scores are editorial estimates, not findings of fact or guilt. Corrections welcome.

"""
(ROOT/'docs/CLAIM-REGISTER.md').write_text(head+'\n'.join(rows))
print(len(rows),'reviews',tot,'receipts',wk,'weak')
