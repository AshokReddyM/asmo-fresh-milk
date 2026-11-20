# Asmo Fresh Milk

Static website published from `main` at https://asmofresh.com using GitHub Pages. No paid hosting or build service is required.

## Develop and check

```sh
python3 -m http.server 5174 --bind 127.0.0.1
python3 scripts/check-site.py
node --check app.js
```

The page uses HTML, CSS, and a small JavaScript file. Existing brand artwork is embedded as SVG; two images from the original website are stored in `assets/` and loaded lazily. Fonts are requested from Google Fonts with local fallbacks.

## Enquiries

The form prepares an email to the contact address from the original website. The visitor reviews it and opens their own email app or copies the text. There is no backend, automated email submission, payment, or confirmed order. Website JavaScript does not persist personal information. Pricing and delivery availability require confirmation by the business.

## Domains

`CNAME` holds the existing canonical domain, `asmofresh.com`. `amsofresh.com` is a different spelling and must be configured separately after registrar access is established; do not replace the working domain accidentally. No DNS change can register an unregistered domain.

## Validation performed

Checked 320, 390, 768, and 1440 px layouts, mobile navigation, bottle-size selection, enquiry text preparation, stale-result clearing, FAQ expansion, reduced-motion behavior, and content visibility with JavaScript disabled. These checks do not send an enquiry.
