from html.parser import HTMLParser
from pathlib import Path
import json
import re
import xml.etree.ElementTree as ET

root = Path(__file__).resolve().parent.parent
class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.refs = []
        self.h1 = 0
    def handle_starttag(self, tag, pairs):
        attrs = dict(pairs)
        if 'id' in attrs:
            assert attrs['id'] not in self.ids, f'Duplicate id: {attrs["id"]}'
            self.ids.add(attrs['id'])
        if tag == 'h1': self.h1 += 1
        for key in ['href', 'src']:
            if key in attrs: self.refs.append(attrs[key])
        if tag == 'img': assert attrs.get('alt'), 'Image missing alt text'

source = (root / 'index.html').read_text()
page = Page()
page.feed(source)
assert page.h1 == 1
for ref in page.refs:
    if ref.startswith('#'): assert ref[1:] in page.ids, f'Missing fragment: {ref}'
    elif ref.startswith('/') and ref != '/': assert (root / ref.lstrip('/')).is_file(), f'Missing asset: {ref}'
assert (root / 'CNAME').read_text().strip() == 'asmofresh.com'
assert 'https://asmofresh.com/' in source
for schema in re.findall(r'<script type="application/ld\+json">(.*?)</script>', source, re.S): json.loads(schema)
ET.parse(root / 'sitemap.xml')
assert 'https://asmofresh.com/sitemap.xml' in (root / 'robots.txt').read_text()
assert 'data:image/' not in source, 'Images should be independently cacheable'
assert len(source.encode()) < 100_000, 'Main HTML exceeded its size budget'
print('Validated links, assets, SVG references, headings, metadata, and HTML size.')
