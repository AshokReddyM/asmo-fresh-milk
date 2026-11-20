"""Build two static, crawlable information pages from the site's shared shell."""
from pathlib import Path
import json
import re
from html import escape

ROOT = Path(__file__).resolve().parent.parent
HOME = (ROOT / 'index.html').read_text()
BASE = 'https://asmofresh.com'
PAGES = [
    {
        'slug': 'buffalo-milk',
        'title': 'Buffalo Milk in Ongole — ₹90 per Litre | Asmo Fresh Milk',
        'description': 'Explore Asmo buffalo milk in Ongole at ₹90 per litre, with free delivery. Compare glass bottle sizes and plan your daily milk quantity.',
        'label': 'Buffalo milk',
        'heading': 'Buffalo milk for<br><em>your everyday.</em>',
        'intro': 'Asmo Fresh Milk offers buffalo milk in glass bottles in Ongole. Our milk rate is ₹90 per litre, with free delivery. Choose a bottle size and tell us your delivery address to get started.',
        'image': 'asmo-bottle.webp',
        'alt': 'Asmo Fresh Milk glass bottle packaging illustration',
        'body': '''
<section id="sizes"><h2>Choose a bottle that fits your routine</h2><p>We offer 500 ml, 1 litre, and 2 litre glass bottles. The right quantity depends on how often your household makes tea or coffee, prepares breakfast, or uses milk in cooking. Start with the amount you already use instead of choosing more than you need.</p>
<div class="table-scroll"><table><caption>Buffalo milk bottle sizes and example uses</caption><thead><tr><th scope="col">Bottle size</th><th scope="col">An everyday starting point</th><th scope="col">If used each day for 7 days</th></tr></thead><tbody><tr><th scope="row">500 ml</th><td>Smaller households or tea and coffee</td><td>3.5 litres</td></tr><tr><th scope="row">1 litre</th><td>A regular household breakfast routine</td><td>7 litres</td></tr><tr><th scope="row">2 litres</th><td>Larger households or milk for cooking</td><td>14 litres</td></tr></tbody></table></div><p class="article-note">These are planning examples, not a recommended serving size. Bottle imagery is illustrative. Confirm the total price for your chosen size when you enquire.</p></section>
<section id="price"><h2>Buffalo milk price: ₹90 per litre</h2><p>The confirmed rate for Asmo buffalo milk is ₹90 for 1 litre. Delivery in Ongole has no delivery charge. For a household using 1 litre every day, the milk cost works out to ₹630 for 7 days, or ₹2,700 for a 30-day planning period.</p><p>These totals are simple quantity estimates, not a prepaid plan or an automatic subscription. Before ordering, confirm the amount you need, the delivery schedule, and the payable total with us.</p><a class="button" href="/#order">Enquire about milk at ₹90/litre →</a></section>
<section id="everyday"><h2>Milk for the moments you already enjoy</h2><p>From morning chai and coffee to porridge, homemade curd, and sweets, milk is part of many household routines. Think about your regular use first, then any extra milk needed for cooking or guests. You can request a daily, alternate-day, or one-time delivery schedule.</p><p>Asmo offers buffalo milk. If you need details about processing, storage instructions, or the current batch, ask us directly before ordering.</p></section>
<section id="glass"><h2>Glass bottles and your first delivery</h2><p>Our available bottle sizes are presented in glass packaging. When arranging your first order, ask about bottle handover and any return arrangements, along with delivery timing. This makes the first delivery easier for both your household and the delivery team.</p><p>Ready to choose? Share your preferred bottle size, your locality in Ongole, and a contact number. We’ll confirm your address and the next steps personally.</p></section>
<section id="questions"><h2>Questions about our buffalo milk</h2><details><summary>How much is one litre of Asmo milk?</summary><p>One litre costs ₹90. Delivery in Ongole is free.</p></details><details><summary>Can I request a smaller bottle?</summary><p>Yes. Our listed sizes include 500 ml, 1 litre, and 2 litres. Include your preferred size in the enquiry and confirm its final amount with us.</p></details><details><summary>Is this cow milk or buffalo milk?</summary><p>Asmo Fresh Milk offers buffalo milk. The website’s product and bottle information refers to buffalo milk.</p></details></section>''',
        'related': ('/milk-delivery-ongole/', 'See how free delivery in Ongole works'),
    },
    {
        'slug': 'milk-delivery-ongole',
        'title': 'Free Buffalo Milk Delivery in Ongole | Asmo Fresh Milk',
        'description': 'Get buffalo milk delivered in Ongole at ₹90 per litre with no delivery charges. See schedule options and how to confirm delivery to your address.',
        'label': 'Ongole milk delivery',
        'heading': 'Fresh milk delivery.<br><em>Here in Ongole.</em>',
        'intro': 'Asmo Fresh Milk currently serves Ongole with buffalo milk at ₹90 per litre and free delivery. Send us your locality and preferred quantity so we can confirm service to your address.',
        'image': 'asmo-breakfast.webp',
        'alt': 'Asmo milk bottle beside chai and breakfast in a kitchen illustration',
        'body': '''
<section id="coverage"><h2>Milk delivery in Ongole</h2><p>We currently deliver in Ongole. Delivery availability is confirmed for each address, so please include your neighbourhood, PIN code, and a nearby landmark in your enquiry. A city-level service area does not mean every address is automatically covered.</p><p>If you are looking for buffalo milk delivery near you in Ongole, the quickest next step is to call <a href="tel:+919989986695">99899 86695</a> or use our <a href="/#order">delivery enquiry form</a>. We’ll check your address and discuss a suitable delivery time.</p></section>
<section id="cost"><h2>₹90 per litre. No delivery charges.</h2><p>Asmo buffalo milk costs ₹90 for one litre. Delivery in Ongole is free. Tell us your chosen bottle size and how often you would like milk so we can confirm the total before you place an order.</p><p>The website does not take payments or automatically create a subscription. Sending an enquiry starts a conversation about your order; it does not confirm a delivery or charge your account.</p></section>
<section id="schedule"><h2>Choose a delivery routine</h2><div class="schedule-explainer"><div><h3>Daily</h3><p>Request milk for an everyday tea, coffee, or breakfast routine. Tell us the quantity you typically use each day.</p></div><div><h3>Alternate days</h3><p>Request a less frequent schedule if that better matches your household’s needs. Confirm the specific delivery days with us.</p></div><div><h3>One-time</h3><p>Enquire about a single delivery before deciding on a regular routine, or when you need milk for a particular occasion.</p></div></div><p>These are delivery preferences, subject to address and schedule confirmation. Contact us directly if your quantity or availability changes; the website does not manage pauses, cancellations, or rescheduling.</p></section>
<section id="start"><h2>How to arrange your first delivery</h2><ol class="article-steps"><li><strong>Choose your bottle size.</strong> Explore 500 ml, 1 litre, and 2 litre options on our <a href="/buffalo-milk/">buffalo milk page</a>.</li><li><strong>Share your Ongole address details.</strong> Include your locality, PIN code, and a landmark, along with your contact number.</li><li><strong>Tell us your preferred schedule.</strong> Choose daily, alternate days, or one-time delivery.</li><li><strong>Confirm the details with us.</strong> Check address coverage, timing, quantity, and the payable amount before the order is placed.</li></ol></section>
<section id="contact"><h2>Contact Asmo Fresh Milk</h2><p>Call <a href="tel:+919989986695">+91 99899 86695</a> to ask about milk delivery in Ongole. You can also email <a href="mailto:aaashokreddy@gmail.com">aaashokreddy@gmail.com</a>.</p><p>Our enquiry form prepares an email with your details for you to review and send. If your device does not have an email app, copy the prepared enquiry into your preferred email service, or call us instead.</p><a class="button" href="/#order">Check my delivery address →</a></section>
<section id="questions"><h2>Delivery questions</h2><details><summary>Is milk delivery free in Ongole?</summary><p>Yes. We do not charge a delivery fee in Ongole. Confirm service to your exact address when you enquire.</p></details><details><summary>Do you deliver outside Ongole?</summary><p>Our current service city is Ongole. We have not announced coverage outside Ongole.</p></details><details><summary>Can I choose an exact delivery time online?</summary><p>No. Delivery timing is agreed personally after we check your address and preferred schedule.</p></details></section>''',
        'related': ('/buffalo-milk/', 'Compare buffalo milk bottle sizes'),
    },
]

head = re.search(r'<head>(.*?)</head>', HOME, re.S)[1]
logo = re.search(r'<svg width="0".*?</svg>', HOME, re.S)[0]
header = re.search(r'<header .*?</header>', HOME, re.S)[0]
footer = re.search(r'<footer>.*?</footer>', HOME, re.S)[0]
# All homepage section links remain valid when reused on another route.
def home_links(html):
    return re.sub(r'href="#(?!logo)([^"]+)"', r'href="/#\1"', html)

for page in PAGES:
    url = BASE + '/' + page['slug'] + '/'
    pagehead = re.sub(r'<title>.*?</title>', '<title>' + escape(page['title']) + '</title>', head)
    for attr, value in [('name="description"', page['description']), ('property="og:title"', page['title']), ('property="og:description"', page['description']), ('property="og:url"', url)]:
        pagehead = re.sub(r'(<meta\s+' + attr + r'\s+content=")[^"]*', lambda m: m[1] + escape(value, quote=True), pagehead)
    pagehead = pagehead.replace('href="https://asmofresh.com/"', 'href="' + url + '"').replace('<script src="/app.js" defer></script>', '')
    graph = [{'@type': 'WebPage', '@id': url+'#webpage', 'url': url, 'name': page['title'], 'description': page['description'], 'inLanguage': 'en-IN', 'isPartOf': {'@id': BASE+'/#website'}, 'publisher': {'@id': BASE+'/#organization'}}, {'@type': 'BreadcrumbList', 'itemListElement': [{'@type':'ListItem','position':1,'name':'Home','item':BASE+'/'},{'@type':'ListItem','position':2,'name':page['label'],'item':url}]}]
    if page['slug'] == 'buffalo-milk':
        graph.append({'@type':'Product','@id':url+'#one-litre','name':'Asmo Fresh Buffalo Milk — 1 litre','description':'One litre of buffalo milk in a glass bottle, available for delivery in Ongole.','image':BASE+'/assets/asmo-bottle.webp','brand':{'@type':'Brand','name':'Asmo Fresh Milk'},'size':'1 litre','offers':{'@type':'Offer','url':BASE+'/#order','price':'90.00','priceCurrency':'INR','eligibleRegion':{'@type':'City','name':'Ongole'},'seller':{'@id':BASE+'/#organization'}}})
    else:
        graph.append({'@type':'Service','name':'Buffalo milk delivery in Ongole','serviceType':'Milk delivery','areaServed':{'@type':'City','name':'Ongole'},'provider':{'@id':BASE+'/#organization'},'description':'Buffalo milk at ₹90 per litre with no delivery charges in Ongole. Exact address coverage and timing confirmed on enquiry.'})
    pagehead = re.sub(r'<script type="application/ld\+json">.*?</script>', '<script type="application/ld+json">'+json.dumps({'@context':'https://schema.org','@graph':graph},ensure_ascii=False)+'</script>', pagehead, flags=re.S)
    nav = home_links(header).replace('href="/'+page['slug']+'/"', 'href="/'+page['slug']+'/" aria-current="page"')
    contents = f'''<!doctype html><html lang="en-IN"><head>{pagehead}</head><body><a class="skip" href="#main">Skip to content</a>{logo}<div class="announcement">Buffalo milk in Ongole · ₹90 per litre <span>Free delivery</span></div>{nav}<main id="main" class="article-page wrap"><nav class="breadcrumbs" aria-label="Breadcrumb"><a href="/">Home</a><span aria-hidden="true">/</span><span aria-current="page">{page['label']}</span></nav><header class="article-hero"><div><p class="eyebrow">ASMO FRESH MILK · ONGOLE</p><h1>{page['heading']}</h1><p>{page['intro']}</p><a href="/#order" class="button">Enquire about delivery →</a></div><img src="/assets/{page['image']}" alt="{page['alt']}" width="640" height="800" fetchpriority="high"></header><div class="article-layout"><aside class="article-aside"><p class="eyebrow">AT A GLANCE</p><dl><dt>Milk</dt><dd>Buffalo milk</dd><dt>Price</dt><dd>₹90 per litre</dd><dt>Service city</dt><dd>Ongole</dd><dt>Delivery fee</dt><dd>No delivery charges</dd></dl><a href="tel:+919989986695">Call 99899 86695 →</a></aside><article class="article-content">{page['body']}<div class="related-guide"><p class="eyebrow">MORE FROM ASMO</p><a href="{page['related'][0]}">{page['related'][1]} →</a></div></article></div></main>{home_links(footer)}</body></html>'''
    folder = ROOT / page['slug']
    folder.mkdir(exist_ok=True)
    (folder/'index.html').write_text(contents)
    print('Built /'+page['slug']+'/')

urls = [BASE+'/'] + [BASE+'/'+p['slug']+'/' for p in PAGES]
(ROOT/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join('<url><loc>'+u+'</loc></url>\n' for u in urls)+'</urlset>\n')
