# Handoff notes

Status as of 2026-11-13: full site built with placeholder images. Everything
below needs an answer or an action before launch.

## Facts to confirm with Beth

These appear on the pages as written. Change them in `src/pages/` and rebuild.

- The five step timeline (home, workshop): pick your handle 0:00, wind and
  bind 0:15, stitch the shoulders 0:40, charms and ribbons 1:05, fly home 1:30.
  Written from how broomcorn brooms are made in general, not from watching a
  class. Beth should correct the order, the timings and anything the class does
  not do (handle choice, color choice, charms, name tag).
- Session times (home, visit): Mon to Thu 11:00, 2:00, 4:30; Fri and Sat adds
  7:00; Sun 11:00 and 2:00; extra sessions in October. Illustrative.
- Capacity of 12 makers per session.
- All ages welcome, and one guest per maker may come to watch free of charge (both from Beth, 2026-11-13). Not stated on the site: whether very young children need an adult making beside them, and whether there is a limit on guests when a session is full.
- Free changes and cancellations up to 48 hours before; no refund inside 48
  hours; a substitute is always allowed.
- Private sessions: minimum 7, maximum 12 at the bench, $135 per maker, bring
  your own snacks and non alcoholic drinks, held for a week while the group
  gathers.
- Shipping the finished broom home: the site says the workshop packs it, takes it to the shipping company and emails tracking, with flat rate shipping paid by the guest (Beth, 2026-11-13; no price shown on the site). Still to confirm: the flat rate amount and whether to publish it, US only or international, and typical transit time.
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
- Reviews on the site are 17 five star Google reviews of the workshop taken
  from the Witch City Broom Co. profile on 2026-11-13, trimmed to the workshop
  parts, names shortened to first name and last initial. They live in
  `src/reviews.json`; add or remove there and rebuild. Once the workshop has
  its own Google Business Profile, swap the write a review links on
  `/reviews/` for that profile's link.
- Google Analytics and the Google Ads tag: add the tag snippet to the head in
  `build.py` once the property exists. Add fareharbor.com to the cross domain
  list in Analytics so bookings credit the ad click.

## Besom copy, revised 2026-11-13

The broom copy was rewritten to describe a besom (round witch's broom) after
Dan confirmed the style. Sources: the workshop photo, the Broom Co. workshop
page and guest reviews. Still to confirm with Beth:

- Handles are natural wood branches (taken from one photo).
- Dried flowers and greenery are offered to every maker.
- The order of the four steps in the timeline, and the times beside them.
- The broom stands about four feet tall.
- Scissors are the only cutting tool on the bench (terms page).

## Photos and video (updated 2026-11-17)

Beth's photos are in now (from `WCBW-SITE/WCBW IMAGES`), cropped to each slot and saved as WebP in `images/`:
- home, groups section: `group-laughing.webp` (four friends laughing in the red velvet corner)
- workshop, who it suits: `family-brooms.webp` (family of five with a child, fits the all ages line)
- workshop, what you make: `maker-finished-broom.webp` (from Nov 13)
- workshop, clip: `video/building-a-broom.mp4` (720 by 1280, 30 fps, silent, click to play, poster `images/video-poster.webp`). The source clip has no audio track content, so no captions are needed. If a narrated version is ever swapped in, add a captions track.
- about, story: `broom-co-storefront.webp` (from Nov 13); about, the craft: `maker-helping.webp`
- private groups: `private-coven.webp` (six guests in costume)
- gift cards and the gift journal card: `finished-brooms.webp`
- journal, rainy day post and card: `ribbons-shelf.webp`; lore card: `hands-winding.webp`
- social share image `og.png` is now the costumed group photo

Still wanted: a landscape exterior of 32 Derby Square (the visit page and the map section use none), a photo of a packed broom ready to ship, and a true cover shot for a future hero photo (16:9, hands binding broomcorn). The Instagram graphic in the images folder was not used. Everyone pictured should have agreed to appear on the website; the guests in the group and family photos are the ones to double check.

## After launch

- Run the live URL through Google's Rich Results Test (structured data) and
  the Search Console URL inspection.
- Submit `sitemap.xml` in Search Console.
- Two journal posts are listed as coming soon with no link. Write them or
  remove the cards.
