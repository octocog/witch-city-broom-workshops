#!/usr/bin/env python3
"""Builds the Witch City Broom Workshops site.

One page list drives everything: the HTML head, the shared header and footer,
the structured data, sitemap.xml and llms.txt. Page bodies live in src/pages/.
Run:  python3 build.py
"""
import html, json, os, re, datetime

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, "src", "pages")
SITE_URL = "https://www.witchcitybroomworkshops.com"
# Preview builds live under a project path on GitHub Pages and must stay out of
# search results. Run `python3 build.py preview` for that; plain `python3 build.py`
# builds for the real domain at the root.
import sys
PREVIEW = len(sys.argv) > 1 and sys.argv[1] == "preview"
BASE = "/witch-city-broom-workshops" if PREVIEW else ""
TODAY = datetime.date.today().isoformat()

BIZ = {
    "name": "Witch City Broom Workshops",
    "phone": "+1-978-815-0013",
    "phone_display": "(978) 815-0013",
    "email": "hello@witchcitybroomworkshops.com",
    "street": "32 Derby Square",
    "city": "Salem",
    "region": "MA",
    "zip": "01970",
    "price": "135",
}
REVIEWS = json.load(open(os.path.join(ROOT, "src", "reviews.json"), encoding="utf-8"))
MONTHS = ["January","February","March","April","May","June","July","August","September","October","November","December"]

STAR_SYMBOL = """<svg width="0" height="0" style="position:absolute" aria-hidden="true" focusable="false"><symbol id="star" viewBox="0 0 24 24"><path d="M12 1.6c.5 0 .9.3 1.1.8l2.3 5.4 5.8.6c1.1.1 1.5 1.5.7 2.2l-4.4 3.9 1.3 5.8c.2 1.1-.9 1.9-1.8 1.3L12 18.6l-5 3c-.9.6-2-.2-1.8-1.3l1.3-5.8-4.4-3.9c-.8-.7-.4-2.1.7-2.2l5.8-.6 2.3-5.4c.2-.5.6-.8 1.1-.8z"/></symbol></svg>"""

def stars_html():
    return ('<span class="stars" role="img" aria-label="Rated 5 out of 5 stars">' + '<svg class="star"><use href="#star"/></svg>' * 5 + '</span>')

def review_card(r, tag="li"):
    y, m = r["date"].split("-")
    when = f"{MONTHS[int(m)-1]} {y}"
    return (f'<{tag} class="review">{stars_html()}<blockquote><p>{html.escape(r["text"])}</p></blockquote>'
            f'<footer><b>{html.escape(r["name"])}</b> <span>Google review, {when}</span></footer></{tag}>')

def reviews_home():
    cards = "".join(review_card(r) for r in REVIEWS if r.get("home"))
    return f"""<div class="slider" data-slider>
      <div class="slider-controls"><button type="button" class="slider-btn" data-prev aria-label="Previous reviews">&#8592;</button><button type="button" class="slider-btn" data-next aria-label="Next reviews">&#8594;</button></div>
      <ul class="slider-track" tabindex="0" aria-label="Reviews, scroll sideways for more">{cards}</ul>
    </div>"""

def reviews_all():
    return '<ul class="review-grid">' + "".join(review_card(r) for r in REVIEWS) + "</ul>"

BOOK_URL = "https://fareharbor.com/embeds/book/witchcitywalkingtours/items/538917/?full-items=yes&flow=14733"
GIFT_URL = "https://fareharbor.com/embeds/book/witchcitywalkingtours/gift-cards/?full-items=yes"

# slug, nav label (None = not in nav), title tag, meta description, parent slug, extra schema type
PAGES = [
    dict(slug="", nav="Home", title="Broom Making Workshops in Salem, MA",
         desc="Make your own full size broom in a 90 minute hands-on workshop at 32 Derby Square, Salem. $135 per person, all materials included, and we ship your broom home.", parent=None),
    dict(slug="workshop", nav="The workshop", title="The Broom Making Workshop",
         desc="What happens in the 90 minute broom making workshop in Salem: choose a handle, wind and bind the broomcorn, stitch, add charms and ribbons, then carry it out or let us ship it home.", parent=""),
    dict(slug="book", nav=None, title="Book a Broom Making Workshop",
         desc="See open dates and times for the Salem broom making workshop and book your seat. $135 per person, small groups, secure checkout.", parent=""),
    dict(slug="private-groups", nav="Private groups", title="Private Broom Making Parties and Group Events",
         desc="Book the Salem broom workshop for your bachelorette party, birthday, team outing or school group. Private sessions at 32 Derby Square.", parent=""),
    dict(slug="gift-cards", nav="Gift cards", title="Broom Workshop Gift Cards",
         desc="Give a seat at the Salem broom making workshop. Gift cards are emailed on purchase and redeemable on any open date.", parent=""),
    dict(slug="visit", nav="Plan your visit", title="Plan Your Visit to the Workshop",
         desc="Find the workshop at 32 Derby Square in downtown Salem. Parking, what to wear, arriving early, accessibility and the cancellation policy.", parent=""),
    dict(slug="faq", nav=None, title="Workshop Questions and Answers",
         desc="Answers to the questions we hear most about the Salem broom making workshop: ages, group size, what to bring, cancellations and travel.", parent="visit"),
    dict(slug="about", nav="About", title="About Witch City Broom Workshops",
         desc="The makers behind the Salem broom workshop, the craft of broomcorn brooms, and the family of Witch City brands.", parent=""),
    dict(slug="reviews", nav=None, title="Workshop Reviews",
         desc="What makers say about the Salem broom making workshop, pulled from Google and TripAdvisor, with a link to leave your own.", parent="about"),
    dict(slug="journal", nav=None, title="Journal",
         desc="Notes from the workshop: rainy day Salem, broom lore, gift ideas and what to do around Derby Square.", parent="about"),
    dict(slug="journal/rainy-day-salem", nav=None, title="A Rainy Day in Salem: What to Do Indoors",
         desc="Ten indoor things to do in Salem when the weather turns, from museums to a broom you make yourself.", parent="journal", article=True),
    dict(slug="contact", nav="Contact", title="Contact the Workshop",
         desc="Phone, email and address for Witch City Broom Workshops at 32 Derby Square, Salem, plus a short form for anything that is not a booking.", parent=""),
    dict(slug="cancellation-policy", nav=None, title="Cancellation Policy", desc="How to change or cancel a broom workshop booking and what refunds apply.", parent="visit"),
    dict(slug="accessibility", nav=None, title="Accessibility", desc="How the workshop and this website work for everyone, and how to tell us when something gets in the way.", parent="visit"),
    dict(slug="privacy", nav=None, title="Privacy", desc="What this website collects, what the booking system collects, and how to reach us about your data.", parent=""),
    dict(slug="terms", nav=None, title="Terms", desc="Plain terms for booking and attending a broom making workshop in Salem.", parent=""),
]
NAV = [p for p in PAGES if p["nav"]]
BY_SLUG = {p["slug"]: p for p in PAGES}

def url(slug):
    return SITE_URL + "/" + (slug + "/" if slug else "")

def path_for(slug):
    return os.path.join(ROOT, slug, "index.html") if slug else os.path.join(ROOT, "index.html")

def crumbs(page):
    chain = []
    p = page
    while p is not None:
        chain.append(p)
        p = BY_SLUG.get(p["parent"]) if p["parent"] is not None else None
    chain.reverse()
    return chain

def breadcrumb_html(page):
    if not page["slug"]:
        return ""
    items = []
    for i, p in enumerate(crumbs(page)):
        label = "Home" if not p["slug"] else p["nav"] or p["title"]
        if i == len(crumbs(page)) - 1:
            items.append(f'<li aria-current="page">{html.escape(label)}</li>')
        else:
            items.append(f'<li><a href="{"/" + (p["slug"] + "/" if p["slug"] else "")}">{html.escape(label)}</a></li>')
    return f'<nav aria-label="Breadcrumb"><ol class="crumbs">{"".join(items)}</ol></nav>'

def schema(page, body):
    org = {
        "@type": "LocalBusiness", "@id": SITE_URL + "/#business",
        "name": BIZ["name"], "url": SITE_URL + "/",
        "image": SITE_URL + "/images/og.png", "logo": SITE_URL + "/images/logo-blue.png",
        "telephone": BIZ["phone"], "email": BIZ["email"],
        "address": {"@type": "PostalAddress", "streetAddress": BIZ["street"], "addressLocality": BIZ["city"],
                    "addressRegion": BIZ["region"], "postalCode": BIZ["zip"], "addressCountry": "US"},
        "priceRange": "$$",
        "parentOrganization": {"@type": "Organization", "name": "Witch City Experiences", "url": "https://www.witchcityexperiences.com/"},
        "makesOffer": {"@type": "Offer", "url": url("book"), "price": BIZ["price"], "priceCurrency": "USD",
                        "availability": "https://schema.org/InStock",
                        "itemOffered": {"@type": "Service", "@id": SITE_URL + "/workshop/#service",
                                        "name": "Broom Making Workshop", "serviceType": "Craft workshop",
                                        "description": "A 90 minute hands-on class where you make a full size broomcorn broom and take it home.",
                                        "provider": {"@id": SITE_URL + "/#business"},
                                        "areaServed": {"@type": "City", "name": "Salem", "containedInPlace": {"@type": "State", "name": "Massachusetts"}}}},
    }
    website = {"@type": "WebSite", "@id": SITE_URL + "/#website", "url": SITE_URL + "/", "name": BIZ["name"],
               "publisher": {"@id": SITE_URL + "/#business"}, "inLanguage": "en-US"}
    webpage = {"@type": "WebPage", "@id": url(page["slug"]) + "#webpage", "url": url(page["slug"]),
               "name": page["title"], "description": page["desc"], "isPartOf": {"@id": SITE_URL + "/#website"},
               "about": {"@id": SITE_URL + "/#business"}, "inLanguage": "en-US"}
    graph = [org, website, webpage]
    if page["slug"]:
        webpage["breadcrumb"] = {"@id": url(page["slug"]) + "#breadcrumb"}
        graph.append({"@type": "BreadcrumbList", "@id": url(page["slug"]) + "#breadcrumb", "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": ("Home" if not p["slug"] else p["nav"] or p["title"]), "item": url(p["slug"])}
            for i, p in enumerate(crumbs(page))]})
    if page["slug"] == "faq":
        qas = re.findall(r"<summary>(.*?)</summary>\s*<div>(.*?)</div>", body, re.S)
        graph.append({"@type": "FAQPage", "@id": url("faq") + "#faq", "mainEntity": [
            {"@type": "Question", "name": html.unescape(re.sub(r"<[^>]+>", "", q)).strip(),
             "acceptedAnswer": {"@type": "Answer", "text": html.unescape(re.sub(r"<[^>]+>", "", a)).strip()}}
            for q, a in qas]})
    if page.get("article"):
        m = re.search(r'<time datetime="([^"]+)"', body)
        graph.append({"@type": "BlogPosting", "@id": url(page["slug"]) + "#article", "headline": page["title"],
                      "description": page["desc"], "url": url(page["slug"]), "mainEntityOfPage": {"@id": url(page["slug"]) + "#webpage"},
                      "datePublished": m.group(1) if m else TODAY, "dateModified": m.group(1) if m else TODAY,
                      "author": {"@id": SITE_URL + "/#business"}, "publisher": {"@id": SITE_URL + "/#business"},
                      "image": SITE_URL + "/images/og.png", "inLanguage": "en-US"})
    return json.dumps({"@context": "https://schema.org", "@graph": graph}, indent=1, ensure_ascii=False)

def nav_html(page):
    items = []
    for p in NAV:
        href = "/" + (p["slug"] + "/" if p["slug"] else "")
        cur = ' aria-current="page"' if p["slug"] == page["slug"] else ""
        items.append(f'<li><a href="{href}"{cur}>{html.escape(p["nav"])}</a></li>')
    items.append(f'<li><a class="btn btn-gold" href="/book/">Book a workshop</a></li>')
    return "".join(items)

def render(page):
    fn = os.path.join(SRC, (page["slug"].replace("/", "__") or "home") + ".html")
    body = open(fn, encoding="utf-8").read()
    full_title = page["title"] if not page["slug"] else f'{page["title"]} | {BIZ["name"]}'
    if not page["slug"]:
        full_title = f'{BIZ["name"]} | {page["title"]}'
    page_url = url(page["slug"])
    og_type = "article" if page.get("article") else "website"
    body = body.replace("{{BREADCRUMB}}", breadcrumb_html(page)).replace("{{BOOK_URL}}", BOOK_URL).replace("{{GIFT_URL}}", GIFT_URL)
    body = body.replace("{{REVIEWS_HOME}}", reviews_home()).replace("{{REVIEWS_ALL}}", reviews_all())
    body = body.replace("{{PHONE}}", BIZ["phone_display"]).replace("{{PHONE_TEL}}", BIZ["phone"]).replace("{{EMAIL}}", BIZ["email"])
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(full_title)}</title>
<meta name="description" content="{html.escape(page["desc"])}">
<link rel="canonical" href="{page_url}">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="{BIZ["name"]}">
<meta property="og:title" content="{html.escape(page["title"])}">
<meta property="og:description" content="{html.escape(page["desc"])}">
<meta property="og:url" content="{page_url}">
<meta property="og:image" content="{SITE_URL}/images/og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Witch City Broom Workshops, Salem, Massachusetts">
<meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{html.escape(page["title"])}">
<meta name="twitter:description" content="{html.escape(page["desc"])}">
<meta name="twitter:image" content="{SITE_URL}/images/og.png">
<meta name="theme-color" content="#0B3E51">
<link rel="icon" href="/images/favicon-32.png" sizes="32x32" type="image/png">
<link rel="icon" href="/images/icon-512.png" sizes="512x512" type="image/png">
<link rel="apple-touch-icon" href="/images/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Josefin+Sans:ital,wght@0,300;0,400;0,600;1,300&family=Playfair+Display:ital,wght@0,400;0,500;0,600;1,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/css/site.css">
<script type="application/ld+json">
{schema(page, body)}
</script>
</head>
<body>
<a class="skip" href="#main">Skip to main content</a>
<header class="site-header">
  <div class="wrap">
    <a class="logo-link" href="/" aria-label="Witch City Broom Workshops home"><img src="/images/logo-white.png" alt="Witch City Broom Workshops" width="1200" height="558"></a>
    <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="site-nav">Menu</button>
    <nav class="site-nav" id="site-nav" aria-label="Main">
      <ul>{nav_html(page)}</ul>
    </nav>
  </div>
</header>
<main id="main" tabindex="-1">
{STAR_SYMBOL}
{body}
</main>
<section class="section section-ink" aria-labelledby="family-h">
  <div class="wrap">
    <h2 id="family-h" class="visually-hidden">The Witch City family of brands</h2>
    <p style="text-align:center;font-size:.95rem;margin-bottom:22px">Part of the Witch City Experiences family</p>
    <div class="family">
      <div class="brand"><h3><a href="https://witchcitywalkingtours.com/">Witch City Walking Tours</a></h3><p>Guided history tours, Old Town Hall</p></div>
      <div class="brand"><h3><a href="https://witchcitybroomco.com/">Witch City Broom Co.</a></h3><p>Handcrafted brooms and kits, 246 Essex Street</p></div>
      <div class="brand"><h3><a href="https://www.witchcityexperiences.com/">Witch City Experiences</a></h3><p>All three, one Salem day</p></div>
    </div>
  </div>
</section>
<footer class="site-footer">
  <div class="wrap">
    <nav aria-label="Footer">
      <ul>
        <li><a href="/cancellation-policy/">Cancellation policy</a></li>
        <li><a href="/accessibility/">Accessibility</a></li>
        <li><a href="/privacy/">Privacy</a></li>
        <li><a href="/terms/">Terms</a></li>
        <li><a href="/contact/">Contact</a></li>
      </ul>
    </nav>
    <p style="margin:0">{BIZ["name"]}, {BIZ["street"]}, {BIZ["city"]} {BIZ["region"]} {BIZ["zip"]}. <a href="tel:{BIZ["phone"]}">{BIZ["phone_display"]}</a></p>
    <p style="margin:0;flex-basis:100%">Designed and maintained by <a href="https://octocog.com" target="_blank" rel="noopener noreferrer">OctoCog Marketing &amp; Design</a></p>
  </div>
</footer>
<script src="/js/site.js" defer></script>
</body>
</html>
"""

def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if BASE and path.endswith(".html"):
        text = text.replace('href="/', f'href="{BASE}/').replace('src="/', f'src="{BASE}/')
        text = text.replace("<meta name=\"viewport\"", "<meta name=\"robots\" content=\"noindex, nofollow\">\n<meta name=\"viewport\"", 1)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)

def main():
    for p in PAGES:
        write(path_for(p["slug"]), render(p))
    # 404
    write(os.path.join(ROOT, "404.html"), render(dict(slug="404", nav=None, title="Page not found",
          desc="That page is not here. Try the workshop, booking or contact pages.", parent="")).replace(
          '<link rel="canonical" href="https://www.witchcitybroomworkshops.com/404/">', '<meta name="robots" content="noindex">'))
    # sitemap.xml (404 and 'thanks' style pages excluded)
    urls = "".join(f"  <url><loc>{url(p['slug'])}</loc><lastmod>{TODAY}</lastmod></url>\n" for p in PAGES)
    write(os.path.join(ROOT, "sitemap.xml"), f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n')
    write(os.path.join(ROOT, "robots.txt"), "User-agent: *\nDisallow: /\n" if PREVIEW else f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}/sitemap.xml\n")
    lines = [f"# {BIZ['name']}", "",
             "> Hands-on broom making workshops in downtown Salem, Massachusetts. 90 minutes, $135 per person, all materials included, every maker takes a full size broom home, or has it shipped home by the workshop. Held at 32 Derby Square. Booking runs on FareHarbor. Part of the Witch City Experiences family with Witch City Walking Tours and Witch City Broom Co.", "",
             "## Pages", ""]
    for p in PAGES:
        lines.append(f"- [{p['title']}]({url(p['slug'])}): {p['desc']}")
    lines += ["", "## Facts", "",
              f"- Address: {BIZ['street']}, {BIZ['city']}, {BIZ['region']} {BIZ['zip']}",
              f"- Phone: {BIZ['phone_display']}", f"- Price: ${BIZ['price']} per person", "- Length: 90 minutes", "- Shipping: the workshop ships each finished broom to the guest's home on request",
              f"- Book: {BOOK_URL}"]
    write(os.path.join(ROOT, "llms.txt"), "\n".join(lines) + "\n")
    open(os.path.join(ROOT, ".nojekyll"), "w").close()
    print(f"built {len(PAGES)} pages + 404, sitemap.xml, robots.txt, llms.txt" + (" [PREVIEW build, noindex, base " + BASE + "]" if PREVIEW else ""))

if __name__ == "__main__":
    main()
