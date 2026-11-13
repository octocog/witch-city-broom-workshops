# Handoff notes

Status as of 2026-11-13: full site built with placeholder images. Everything
below needs an answer or an action before launch.

## Facts to confirm with Beth

These appear on the pages as written. Change them in `src/pages/` and rebuild.

- Session times (home, visit): Mon to Thu 11:00, 2:00, 4:30; Fri and Sat adds
  7:00; Sun 11:00 and 2:00; extra sessions in October. Illustrative.
- Capacity of 12 makers per session.
- Ages 10 and up, with a booked adult beside anyone under 16.
- Free changes and cancellations up to 48 hours before; no refund inside 48
  hours; a substitute is always allowed.
- Private sessions: minimum 7, maximum 12 at the bench, $135 per maker, bring
  your own snacks and non alcoholic drinks, held for a week while the group
  gathers.
- Shipping the finished broom home: the site says the workshop packs it, takes it to the shipping company and emails tracking, with the guest paying the carrier's rate (confirmed by Dan 2026-11-13, no price shown). Still to confirm: US only or international, and typical transit time.
- Gift cards do not expire (also true under Massachusetts law for 7 years).
- Step free entrance, bench height 30 inches, lower work surface and
  wheelchair space on a day's notice, restroom on the same floor, large print
  step cards. Written from the mock, not from a site visit.
- Phone number. The site uses the Broom Co. shop line, (978) 815-0013.
- Email address hello@witchcitybroomworkshops.com does not exist yet.

## Accounts and connections

- Domain: witchcitybroomworkshops.com is assumed throughout. Register it, point
  DNS at GitHub Pages, add the `CNAME` file, set the custom domain in the repo.
- Formspree: create two forms and replace `REPLACE_WITH_FORM_ID` in
  `src/pages/private-groups.html` and `src/pages/contact.html`.
- FareHarbor gift cards: the link on `/gift-cards/` assumes gift cards are
  switched on for the Walking Tours company. Confirm the URL in the FareHarbor
  dashboard.
- Google Business Profile for the workshop at 32 Derby Square, then swap the
  review links on `/reviews/` for the profile's write a review link and
  connect a live review feed.
- Google Analytics and the Google Ads tag: add the tag snippet to the head in
  `build.py` once the property exists. Add fareharbor.com to the cross domain
  list in Analytics so bookings credit the ad click.

## Photos to shoot

Replace these SVG placeholders in `images/` with photos of the same shape.

- `ph-hero.svg` 16:9, hands winding broomcorn (reserved for a future hero photo)
- `ph-group.svg` 4:5, a group holding finished brooms
- `ph-private.svg` 16:9, a private party at the long bench
- `ph-finished.svg` 16:9, one finished broom with ribbon and charm
- `ph-detail.svg` 1:1, stitching the shoulders
- `ph-makers.svg` 4:5, the makers at the bench
- `ph-room.svg` 16:9, the room at Derby Square
- `ph-journal-rainy.svg`, `ph-journal-lore.svg`, `ph-journal-gift.svg` 16:9

## After launch

- Run the live URL through Google's Rich Results Test (structured data) and
  the Search Console URL inspection.
- Submit `sitemap.xml` in Search Console.
- Two journal posts are listed as coming soon with no link. Write them or
  remove the cards.
