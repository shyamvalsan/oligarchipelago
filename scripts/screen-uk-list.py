"""Name-screen all 500 against the current UK list. NOT an oligarch classifier.

Only public names, designation identifiers, reasons and source dates are retained.
No addresses, birth dates, identifiers or other personal details are saved.
Non-matches must remain unassessed; candidate identities require editorial review.
"""
import csv
import datetime
import hashlib
import io
import json
from pathlib import Path
import re
import unicodedata
import urllib.request

ROOT = Path(__file__).resolve().parent.parent
URL = 'https://sanctionslist.fcdo.gov.uk/docs/UK-Sanctions-List.csv'

def normalize(value):
    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode().lower()
    return re.sub(r'[^a-z ]', ' ', value).split()

def first_key(value):
    # Explicit common transliterations, not arbitrary fuzzy identity inference.
    aliases = {'alexey':'alexei','aleksey':'alexei','aleksei':'alexei','andrey':'andrei',
               'gennadiy':'gennady','suleyman':'suleiman','mikhail':'mikhail',
               'viatcheslav':'vyacheslav','vaguit':'vagit'}
    return aliases.get(value, value)

def main():
    people = json.loads((ROOT/'data/billionaires.json').read_text())['people']
    with urllib.request.urlopen(URL, timeout=120) as response:
        raw = response.read()
    lines=io.StringIO(raw.decode('utf-8-sig'))
    report_date=next(lines).strip()
    rows=csv.DictReader(lines)
    assert {'Name 6','Name 1','Unique ID','UK Statement of Reasons'} <= set(rows.fieldnames)
    by_name={}
    for row in rows:
        if row.get('Designation Type','').lower() != 'individual':
            continue
        surname=normalize(row.get('Name 6',''))
        first=normalize(row.get('Name 1',''))
        if not surname or not first:
            continue
        key=(' '.join(surname),first_key(first[0]))
        minimal={
            'designationId':row['Unique ID'],
            'name':' '.join(row.get(f'Name {i}','') for i in [1,2,3,4,5,6]).strip(),
            'reason':row.get('UK Statement of Reasons',''),
            'designationDate':row.get('Date Designated',''),
            'updatedAt':row.get('Last Updated',''),
            'url':f'https://search-uk-sanctions-list.service.gov.uk/designations/{row["Unique ID"]}/Individual',
        }
        by_name.setdefault(key,{})[row['Unique ID']]=minimal
    profiles={}
    for person in people:
        tokens=normalize(person['name'].split(' & family')[0])
        matches=by_name.get((tokens[-1],first_key(tokens[0])),{}) if len(tokens)>=2 else {}
        profiles[person['id']]={'status':'candidate-match' if matches else 'no-name-match', 'matches':list(matches.values())}
    result={
        'sourceUrl':URL,'publisher':'UK FCDO','reportDate':report_date,
        'retrievedAt':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'sourceSha256':hashlib.sha256(raw).hexdigest(),
        'license':'UK Open Government Licence v3.0; Crown copyright acknowledged.',
        'licenseUrl':'https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/',
        'screenedCount':len(people),
        'method':'Exact normalized surname and first name, with the explicit transliteration aliases in scripts/screen-uk-list.py. All 500 checked. This is a narrow name-screen, not comprehensive due diligence, identity verification, or an oligarchy assessment. No name match does not mean no designation or no oligarchic conduct. Designation alone never sets an editorial verdict.',
        'profiles':profiles,
    }
    (ROOT/'data/screening.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    matched=[(p['id'],profiles[p['id']]['matches'][0]['designationId']) for p in people if profiles[p['id']]['matches']]
    print('Screened:',len(profiles),'Candidate matches:',len(matched),'Report:',report_date)
    print(json.dumps(matched,indent=2))

if __name__=='__main__':main()
