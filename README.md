# Photo Fisher website

The public, static web presence for Photo Fisher — a photo and video navigator that helps people find moments in their camera roll quickly.

## What is here

- `index.html` — responsive landing page with product, how-it-works, privacy-first, store placeholder, and support sections.
- `privacy.html` — public V1 privacy-policy page linked from the landing page.
- `404.html` — GitHub Pages fallback page.
- `styles.css` — framework-free responsive styling and the abstract fishing visual system.
- `tests/test_site.py` — dependency-free content and launch-safety checks.

The site uses plain HTML and CSS. It does not contain private Photo Fisher app source, personal photos, signing keys, credentials, or secrets. There is no runtime data collection or backend in this repository.

## Preview locally

From the repository root, start any static file server, for example:

```sh
python3 -m http.server 8000
```

Then open `http://localhost:8000` in a browser. Run the content checks with:

```sh
python3 -m unittest discover -s tests -v
```

## GitHub Pages

This is intentionally build-free. Configure GitHub Pages to publish the repository’s `main` branch from its root directory. Relative links are used so the site also works when served from a project URL.

An active `CNAME` file is not included yet. Add one only after the owner confirms the exact custom hostname, such as a future `kuhtey.com` subdomain.

## Before public release

- **TODO:** configure or replace the neutral `privacy@kuhtey.com` alias. It is a placeholder, not a confirmed production inbox.
- **TODO:** verify the final legal publisher name and production privacy/support contact details.
- **TODO:** add the final Google Play and App Store URLs to the landing page.
- **TODO:** compare the final shipped V1 behavior with `privacy.html` and complete the matching Google Play Data Safety and App Store privacy disclosures.
- **TODO:** verify any future ad/analytics disclosures before adding an advertising SDK, analytics service, backend, account flow, uploads, or other data collection.
- **TODO:** confirm the exact custom-domain hostname before adding `CNAME`.

The privacy policy currently describes the V1 intent: local camera-roll access after permission, no account, no backend, no uploads, no analytics, no advertising SDK in V1, no sale of user photos, and no access to other apps. A system share action is user initiated. If a paid unlock is added, Google Play or the App Store may process purchases under their own terms and privacy policies.
