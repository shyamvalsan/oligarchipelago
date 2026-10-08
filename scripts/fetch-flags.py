"""Vendor the 50 citizenship SVG assets; no dependency installation."""
import hashlib,json,urllib.request,xml.etree.ElementTree as ET
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
COMMIT='086f7e97d657358203916dbe84f61c2bccaa81eb'
BASE=f'https://raw.githubusercontent.com/lipis/flag-icons/{COMMIT}/'
OUT=ROOT/'assets/flags'
def get(path):
 return urllib.request.urlopen(urllib.request.Request(BASE+path,headers={'User-Agent':'oligarchipelago-local-assets'}),timeout=30).read()
def main():
 countries=json.loads((ROOT/'data/billionaires.json').read_text())['countries']
 # Validate all assets before writing, so a failed request cannot leave half a set.
 files={'LICENSE':get('LICENSE')}
 for iso in sorted({c['iso'].lower() for c in countries.values()}):
  raw=get(f'flags/1x1/{iso}.svg');tree=ET.fromstring(raw)
  assert tree.tag.endswith('svg') and b'<script' not in raw and b'http' not in raw.replace(b'http://www.w3.org/2000/svg',b'').replace(b'http://www.w3.org/1999/xlink',b'')
  files[iso+'.svg']=raw
 OUT.mkdir(exist_ok=True)
 for name,raw in files.items():(OUT/name).write_bytes(raw)
 (OUT/'provenance.json').write_text(json.dumps({'project':'lipis/flag-icons','commit':COMMIT,'license':'MIT','source':BASE,'files':{n:hashlib.sha256(b).hexdigest() for n,b in files.items()}},indent=2)+'\n')
 print('Vendored',len(files)-1,'flags')
if __name__=='__main__':main()
