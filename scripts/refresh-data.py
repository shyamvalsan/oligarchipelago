"""Explicit, offline-build data refresh. Standard library only; never run by the website.

Run from the repository root: python3 scripts/refresh-data.py
Fetches factual fields only: no Forbes biographies, photographs, or editorial text.
"""
import concurrent.futures
import datetime
import json
from pathlib import Path
import urllib.request

ROOT = Path(__file__).resolve().parent.parent
FORBES = 'https://www.forbes.com/forbesapi/person/billionaires/2026/position/true.json?limit=500'
COUNTRIES = {
    'Australia': ('AU','Oceania'), 'Austria': ('AT','Europe'), 'Belgium': ('BE','Europe'),
    'Brazil': ('BR','South America'), 'Canada': ('CA','North America'), 'Chile': ('CL','South America'),
    'China': ('CN','Asia'), 'Colombia': ('CO','South America'), 'Cyprus': ('CY','Asia'),
    'Czech Republic': ('CZ','Europe'), 'Denmark': ('DK','Europe'), 'Egypt': ('EG','Africa'),
    'Eswatini (Swaziland)': ('SZ','Africa'), 'France': ('FR','Europe'), 'Germany': ('DE','Europe'),
    'Greece': ('GR','Europe'), 'Hong Kong': ('HK','Asia'), 'India': ('IN','Asia'),
    'Indonesia': ('ID','Asia'), 'Ireland': ('IE','Europe'), 'Israel': ('IL','Asia'),
    'Italy': ('IT','Europe'), 'Japan': ('JP','Asia'), 'Kazakhstan': ('KZ','Asia'),
    'Malaysia': ('MY','Asia'), 'Mexico': ('MX','North America'), 'Netherlands': ('NL','Europe'),
    'New Zealand': ('NZ','Oceania'), 'Nigeria': ('NG','Africa'), 'Norway': ('NO','Europe'),
    'Philippines': ('PH','Asia'), 'Portugal': ('PT','Europe'), 'Russia': ('RU','Europe'),
    'Saudi Arabia': ('SA','Asia'), 'Singapore': ('SG','Asia'), 'South Africa': ('ZA','Africa'),
    'South Korea': ('KR','Asia'), 'Spain': ('ES','Europe'), 'St. Kitts and Nevis': ('KN','North America'),
    'Sweden': ('SE','Europe'), 'Switzerland': ('CH','Europe'), 'Taiwan': ('TW','Asia'),
    'Thailand': ('TH','Asia'), 'Turkey': ('TR','Asia'), 'Ukraine': ('UA','Europe'),
    'United Arab Emirates': ('AE','Asia'), 'United Kingdom': ('GB','Europe'),
    'United States': ('US','North America'), 'Venezuela': ('VE','South America'), 'Vietnam': ('VN','Asia'),
}
INDICATORS = {
    'gdp': 'NY.GDP.MKTP.CD', 'gdpPerCapita': 'NY.GDP.PCAP.CD',
    'gdpPpp': 'NY.GDP.MKTP.PP.CD', 'gdpPerCapitaPpp': 'NY.GDP.PCAP.PP.CD',
}

def fetch(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Oligarchipelago-research/0.1'})
    with urllib.request.urlopen(req, timeout=60) as response:
        return json.load(response)

def main():
    records = fetch(FORBES)['personList']['personsLists']
    assert len(records) == 500, 'Expected exactly 500 Forbes entries; inspect before updating.'
    people = []
    for p in records:
        assert p['year'] == 2026 and p['finalWorth'] > 0
        country = p['countryOfCitizenship']
        iso, continent = COUNTRIES[country]  # Stop on an unmapped country.
        self_made, origin_score = p.get('selfMade'), p.get('selfMadeRank')
        origin = 'self-made' if self_made is True else 'family-linked' if self_made is False else 'unknown'
        if self_made is False and origin_score is not None:
            origin = 'inherited' if origin_score <= 2 else 'mixed'
        people.append({
            'id': p['uri'], 'name': p['personName'], 'rank': p['rank'],
            'position': p['position'], 'wealth': p['finalWorth'] / 1000,
            'country': country, 'iso': iso, 'continent': continent,
            'industry': p['category'], 'sourceOfWealth': p['source'],
            'origin': origin, 'forbesSelfMade': self_made, 'forbesSelfMadeScore': origin_score,
            'age': p.get('age'), 'profileUrl': 'https://www.forbes.com/profile/' + p['uri'] + '/',
        })
    assert len(set(p['id'] for p in people)) == 500
    assert all(people[i]['wealth'] >= people[i+1]['wealth'] for i in range(499))

    countries = {name: {'iso': iso, 'continent': continent} for name, (iso, continent) in COUNTRIES.items()}
    def indicator(item):
        key, code = item
        url = f'https://api.worldbank.org/v2/country/all/indicator/{code}?date=2024&format=json&per_page=400'
        result = fetch(url)
        assert isinstance(result, list) and result[0]['pages'] == 1
        return key, code, {row['country']['id']: row for row in result[1]}
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        for key, code, rows in pool.map(indicator, INDICATORS.items()):
            for name, c in countries.items():
                row = rows.get(c['iso'])
                c[key] = None if not row or row['value'] is None else {
                    'value': row['value'], 'year': int(row['date']), 'indicator': code,
                    'url': f'https://data.worldbank.org/indicator/{code}?locations={c["iso"]}',
                }
    dataset = {
        'meta': {
            'edition': 2026, 'wealthDate': '2026-03-01',
            'retrievedAt': datetime.datetime.now(datetime.timezone.utc).isoformat(),
            'forbesUrl': FORBES, 'targetCount': 500, 'economicYear': 2024,
            'note': 'First 500 entries in Forbes annual-list order. Tied ranks preserved; tie at cutoff is not expanded. Country is Forbes citizenship attribution, not residence or asset location. GDP is 2024, not 2026.',
        }, 'people': people, 'countries': countries,
    }
    # Write only once all remote reads and validation succeed.
    target = ROOT / 'data' / 'billionaires.json'
    target.parent.mkdir(exist_ok=True)
    target.write_text(json.dumps(dataset, ensure_ascii=False, indent=2) + '\n')
    print(f'Wrote {len(people)} people and {len(countries)} economies to {target}')
    print('GDP missing:', [n for n,c in countries.items() if c['gdp'] is None])

if __name__ == '__main__':
    main()
