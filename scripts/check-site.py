from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit
import json
import re
import xml.etree.ElementTree as ET

root = Path(__file__).resolve().parent.parent
routes = ['', 'buffalo-milk', 'milk-delivery-ongole']
class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids, self.refs, self.canonicals = set(), [], []
        self.h1 = 0
    def handle_starttag(self, tag, pairs):
        attrs = dict(pairs)
        if 'id' in attrs:
            assert attrs['id'] not in self.ids, f'Duplicate id: {attrs["id"]}'
            self.ids.add(attrs['id'])
        if tag == 'h1': self.h1 += 1
        for key in ['href', 'src']:
            if key in attrs: self.refs.append(attrs[key])
        if 'srcset' in attrs:
            self.refs.extend(item.strip().split()[0] for item in attrs['srcset'].split(','))
        if tag == 'img': assert attrs.get('alt'), 'Image missing alt text'
        if tag == 'link' and attrs.get('rel') == 'canonical': self.canonicals.append(attrs['href'])

pages = {}
for route in routes:
    source = (root / route / 'index.html').read_text()
    page = Page()
    page.feed(source)
    pages['/' + (route + '/' if route else '')] = page
    assert page.h1 == 1, f'{route}: expected one H1'
    assert page.canonicals == ['https://asmofresh.com/' + (route + '/' if route else '')]
    schemas = re.findall(r'<script type="application/ld\+json">(.*?)</script>', source, re.S)
    assert schemas, f'{route}: missing structured data'
    for schema in schemas:
        graph = json.loads(schema)['@graph']
        for item in graph:
            if item['@type'] == 'Product':
                assert item['offers']['price'] == '90.00'
                assert item['offers']['priceCurrency'] == 'INR'
                assert item['size'] == '1 litre'
    assert 'data:image/' not in source
    assert len(source.encode()) < 100_000
    assert 'Ongole' in source and '₹90' in source

for route, page in pages.items():
    for ref in page.refs:
        if ref.startswith('#'):
            assert ref[1:] in page.ids, f'{route}: missing fragment {ref}'
        elif ref.startswith('/'):
            target = urlsplit(ref)
            if target.path in pages:
                if target.fragment: assert target.fragment in pages[target.path].ids, ref
            else: assert (root / target.path.lstrip('/')).is_file(), f'Missing asset: {ref}'
    print('Validated', route)
assert (root / 'CNAME').read_text().strip() == 'asmofresh.com'
ns = {'s': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
sitemap = {e.text for e in ET.parse(root / 'sitemap.xml').findall('s:url/s:loc', ns)}
assert sitemap == {'https://asmofresh.com' + p for p in pages}
assert 'https://asmofresh.com/sitemap.xml' in (root / 'robots.txt').read_text()
print('Validated all internal links, responsive assets, canonical URLs, structured data, and sitemap coverage.')
