# Witch City Broom Workshops

Website for the broom making workshop at 32 Derby Square, Salem, Massachusetts.
Static HTML, no framework, built for GitHub Pages.

## How it is put together

- `build.py` holds the page list (slug, title, description, parent) and stamps
  the shared head, header and footer onto every page. It also writes the
  structured data, `sitemap.xml`, `robots.txt` and `llms.txt` from that list.
- `src/pages/` holds the body of each page. Edit copy there, then run
  `python3 build.py` from this folder. Pages at the root are generated output.
- `css/site.css` is the only stylesheet. Colors and type live in the tokens at
  the top. Dark mode follows the visitor's system setting.
- `js/site.js` does two small things: the mobile menu, and carrying the Google
  click id onto FareHarbor booking links as `ref=` so bookings can be matched
  to ads.
- `images/` holds the logo files, the broom divider, icons, the share image and
  the placeholder images. Placeholders are SVG files named `ph-*.svg`; replace
  each with a photo of the same name and shape, or update the `src` in the page.

## Booking

Booking runs on FareHarbor, item 538917 under the Witch City Walking Tours
company. The calendar on `/book/` is FareHarbor's own embed. Every other
"book" link goes to `/book/`.

## Publishing

GitHub Pages from the `main` branch, root folder. Set the custom domain in the
repository settings and add the `CNAME` file. `.nojekyll` is already here.

Designed and maintained by [OctoCog Marketing & Design](https://octocog.com).
