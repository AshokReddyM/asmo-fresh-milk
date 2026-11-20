# Asmo Fresh Milk

Static website published from `main` at https://asmofresh.com using GitHub Pages. No paid hosting or build service is required.

## Develop and check

```sh
python3 -m http.server 5174 --bind 127.0.0.1
python3 scripts/check-site.py
node --check app.js
```

The page uses HTML, CSS, and a small JavaScript file. The existing brand logo is embedded as SVG. Generated product and lifestyle illustrations use optimized WebP files in `assets/`, with responsive sizes and lazy loading below the fold. The hero image loads with high priority. Prompts and image provenance are recorded in `assets/image-prompts.md`. Fonts are requested from Google Fonts with local fallbacks.

## Enquiries

The form prepares an email to the contact address from the original website. The visitor reviews it and opens their own email app or copies the text. There is no backend, automated email submission, payment, or confirmed order. Website JavaScript does not persist personal information. Pricing and delivery availability require confirmation by the business.

## Domains

`CNAME` holds the existing canonical domain, `asmofresh.com`. `amsofresh.com` is a different spelling and must be configured separately after registrar access is established; do not replace the working domain accidentally. No DNS change can register an unregistered domain.

## Validation performed

Checked 320, 390, 768, and 1440 px layouts, mobile navigation, bottle-size selection, enquiry text preparation, stale-result clearing, FAQ expansion, reduced-motion behavior, and content visibility with JavaScript disabled. These checks do not send an enquiry.

## SEO and local content

Confirmed by the business: Ongole is the current service city; buffalo milk is ₹90 per litre; delivery is free. Exact address coverage and timing are confirmed on enquiry. Do not add neighbourhoods, a street address, business hours, ratings, or certification claims without confirmation.

Crawlable pages:
- `/`: brand, local price, delivery information, enquiry form
- `/buffalo-milk/`: bottle sizes, litre price, quantity planning, product questions
- `/milk-delivery-ongole/`: local service coverage, delivery schedules, enquiry steps

Run `python3 scripts/build-content.py` after editing the homepage shell or page definitions, then `python3 scripts/check-site.py`. Generated pages are committed so GitHub Pages serves them without a build dependency. `navigation.js` is shared; `app.js` handles the homepage enquiry form.

Each page has a unique title, description, canonical URL, and linked structured data. The product offer is only for the confirmed 1-litre price (INR 90); other bottle prices are not invented. Organization markup uses the actual logo and Ongole service area. No address-dependent LocalBusiness rich-result claim is made. The sitemap lists all three canonical URLs.

Search Console: the signed-in account did not have verified access to this property during setup. Owner verification and sitemap submission remain pending; publish the site first, then verify the correct account and submit `https://asmofresh.com/sitemap.xml`. A verified Google Business Profile with accurate service-area details is also useful for local visibility. These changes cannot guarantee a search position.

References: [Google SEO Starter Guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide), [Organization structured data](https://developers.google.com/search/docs/appearance/structured-data/organization), [Sitemap guidance](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap).
