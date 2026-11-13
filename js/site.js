/* Witch City Broom Workshops: nav toggle, click id to FareHarbor ref, nothing else. */
(function () {
  document.documentElement.classList.add('js');

  // Mobile navigation. Without JS the menu is simply visible.
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.getElementById('site-nav');
  if (toggle && nav) {
    var mq = window.matchMedia('(max-width: 760px)');
    function sync() {
      if (mq.matches) { nav.hidden = true; toggle.setAttribute('aria-expanded', 'false'); }
      else { nav.hidden = false; toggle.setAttribute('aria-expanded', 'false'); }
    }
    sync();
    mq.addEventListener ? mq.addEventListener('change', sync) : mq.addListener(sync);
    toggle.addEventListener('click', function () {
      var open = nav.hidden;
      nav.hidden = !open;
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
      if (open) { var first = nav.querySelector('a'); if (first) first.focus(); }
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && mq.matches && !nav.hidden) { nav.hidden = true; toggle.setAttribute('aria-expanded', 'false'); toggle.focus(); }
    });
  }

  // Carry the Google click id onto every FareHarbor booking link as ?ref=
  // so the booking record can be matched back to the ad click.
  var KEY = 'wcbw_click';
  try {
    var q = new URLSearchParams(location.search);
    var id = q.get('gclid') || q.get('gbraid') || q.get('wbraid');
    if (id) { localStorage.setItem(KEY, JSON.stringify({ id: id, t: Date.now() })); }
    var saved = JSON.parse(localStorage.getItem(KEY) || 'null');
    if (saved && Date.now() - saved.t < 90 * 24 * 3600 * 1000) {
      document.querySelectorAll('a[href*="fareharbor.com/embeds/book"]').forEach(function (a) {
        var u = new URL(a.href);
        if (!u.searchParams.get('ref')) { u.searchParams.set('ref', 'gclid_' + saved.id); a.href = u.toString(); }
      });
    }
  } catch (e) { /* storage blocked: booking still works, just without the ref */ }
})();

/* Review slider on the home page: buttons scroll the list one card at a time.
   Without JavaScript the list still scrolls sideways by touch, wheel or keyboard. */
(function () {
  document.querySelectorAll('[data-slider]').forEach(function (s) {
    var track = s.querySelector('.slider-track');
    var prev = s.querySelector('[data-prev]');
    var next = s.querySelector('[data-next]');
    if (!track || !prev || !next) return;
    function step() { var li = track.querySelector('li'); return li ? li.getBoundingClientRect().width + 24 : 300; }
    function update() {
      prev.disabled = track.scrollLeft <= 2;
      next.disabled = track.scrollLeft + track.clientWidth >= track.scrollWidth - 2;
    }
    var smooth = window.matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth';
    prev.addEventListener('click', function () { track.scrollBy({ left: -step(), behavior: smooth }); });
    next.addEventListener('click', function () { track.scrollBy({ left: step(), behavior: smooth }); });
    track.addEventListener('scroll', update, { passive: true });
    window.addEventListener('resize', update);
    update();
  });
})();
