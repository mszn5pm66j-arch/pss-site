/* Praetorian Sentinel Smart — gabarit commun (en-tête, menu plein écran, carrousel du bas, avatar AIT, pied de page) */
(function () {
  var WA = '213555372345';
  var MAIL = 'men-ay_pro-managment@outlook.fr';
  var FB = 'https://www.facebook.com/search/top?q=Praetorian%20Sentinel%20Smart';
  var SECTIONS = [
    { id: 'accueil', n: '01', t: 'Accueil', href: 'index.html', subs: [['Pour qui ?', 'index.html#pour-qui'], ['Nos services', 'index.html#services'], ['AIT', 'index.html#agent']] },
    { id: 'cabinet', n: '02', t: 'Le cabinet', href: 'cabinet.html', subs: [['Notre méthode', 'methode.html'], ['Nos références', 'references.html'], ['Notre conformité', 'notreconformite.html'], ['Nous rejoindre', 'carrieres.html']] },
    { id: 'segments', n: '03', t: 'Nos segments', href: 'divisions.html', subs: [['3.1 Réglementaire & investissement', 'division-2.html'], ["3.2 Maîtrise d'ouvrage", 'division-3.html'], ['3.3 Ingénierie financière', 'division-4.html'], ['3.4 Architecture intelligente augmentée', 'division-1.html']] },
    { id: 'academie', n: '04', t: 'Académie PSS', href: 'academie.html', subs: [] },
    { id: 'offres', n: '05', t: 'Nos offres', href: 'toutes-les-offres.html', subs: [['Diagnostic', 'diagnostic.html'], ['Toutes les offres', 'toutes-les-offres.html']] },
    { id: 'avis', n: '06', t: 'Avis clients', href: 'avis.html', subs: [['6.1 Références professionnelles', 'references.html'], ['6.2 Donner votre avis', 'donner-mon-avis.html']] },
    { id: 'contact', n: '07', t: 'Contactez-nous', href: 'contact.html', subs: [['Contact', 'contact.html'], ['Questions fréquentes', 'faq.html']] }
  ];
  var EXTRA = [{ id: 'espace', n: '·', t: 'Espace client', href: 'espace.html', subs: [['Base documentaire', 'documentation.html']] }];
  var LEGAL = [['Mentions légales', 'mentions.html'], ['Confidentialité', 'confidentialite.html'], ['Conditions', 'conditions.html'], ['Conformité', 'notreconformite.html'], ['FAQ', 'faq.html'], ['Plan du site', 'plan.html']];

  var ARROW = '<svg viewBox="0 0 14 14"><path d="M3 11 11 3M5 3h6v6"/></svg>';
  var CL = '<svg width="14" height="14" viewBox="0 0 14 14" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M9 2 4 7l5 5"/></svg>';
  var CR = '<svg width="14" height="14" viewBox="0 0 14 14" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M5 2l5 5-5 5"/></svg>';
  var I_USER = '<svg viewBox="0 0 24 24"><circle cx="12" cy="8" r="4"/><path d="M4 21c0-4.4 3.6-7 8-7s8 2.6 8 7"/></svg>';
  var I_CASE = '<svg viewBox="0 0 24 24"><rect x="3" y="8" width="18" height="12" rx="2"/><path d="M9 8V6a2 2 0 0 1 2-2h2a2 2 0 0 1 2 2v2M3 13h18"/></svg>';
  var I_SCREEN = '<svg viewBox="0 0 24 24"><rect x="4" y="4" width="16" height="12" rx="1.5"/><path d="M8 20h8M12 16v4"/></svg>';

  var body = document.body;
  var stage = document.querySelector('.stage');
  var page = body.getAttribute('data-page') || '';
  var secId = body.getAttribute('data-sec') || 'accueil';
  var secIdx = Math.max(0, SECTIONS.findIndex(function (s) { return s.id === secId; }));
  var isHome = page === 'index';

  function el(html) { var d = document.createElement('div'); d.innerHTML = html.trim(); return d.firstChild; }
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }

  window.PSS = {
    WA: WA, MAIL: MAIL, FB: FB, SECTIONS: SECTIONS, ARROW: ARROW,
    wa: function (text) { return 'https://wa.me/' + WA + (text ? '?text=' + encodeURIComponent(text) : ''); },
    mail: function (subject, text) { return 'mailto:' + MAIL + '?subject=' + encodeURIComponent(subject || '') + '&body=' + encodeURIComponent(text || ''); },
    esc: esc
  };

  /* ---- en-tête ---- */
  var hd = el('<div class="hd">' +
    '<a href="index.html" aria-label="Accueil"><img class="emblem" src="assets/emblem.png" alt="Emblème Sentinelle"></a>' +
    '<a href="index.html" aria-label="Praetorian Sentinel Smart"><img class="wordmark" src="assets/wordmark.png" alt="Praetorian Sentinel Smart"></a>' +
    '<a class="signup" href="espace.html">M\'inscrire</a>' +
    '<button class="menu" aria-label="Ouvrir le menu" aria-expanded="false"><i></i><i></i><i></i></button>' +
    '<div class="hline"></div><span class="scout"></span></div>');
  stage.appendChild(hd);
  hd.querySelector('.scout').style.left = (14.65 + secIdx * 13.3) + '%';

  /* ---- pied de page ---- */
  function footer() {
    return '<footer class="ft"><div class="legal">' + LEGAL.map(function (l) { return '<a href="' + l[1] + '">' + l[0] + '</a>'; }).join('') + '</div>' +
      '<div class="co"><div><b>WhatsApp Business</b><a href="' + PSS.wa() + '" target="_blank" rel="noopener">+213 555 37 23 45</a></div>' +
      '<div><b>Email</b><a href="mailto:' + MAIL + '">' + MAIL + '</a></div></div>' +
      '<div class="pays">Algérie - France - Espagne - Allemagne - Belgique - Québec</div>' +
      '<a class="fb" href="' + FB + '" target="_blank" rel="noopener"><svg viewBox="0 0 24 24"><path d="M14 8V6.5c0-.8.5-1.5 1.6-1.5H17V2h-2.4C11.9 2 11 3.8 11 6.2V8H9v3h2v11h3V11h2.5l.5-3H14z"/></svg>Page Facebook</a>' +
      '<div class="mn">Praetorian Sentinel Smart · SARL de droit algérien · Oran · cabinet privé, non affilié à une institution publique.</div></footer>';
  }
  window.PSS.footer = footer;
  var pageEl = document.querySelector('.page');
  if (pageEl) pageEl.insertAdjacentHTML('beforeend', footer());

  /* ---- menu plein écran ---- */
  var here = location.pathname.split('/').pop() || 'index.html';
  var groups = SECTIONS.concat(EXTRA).map(function (s) {
    var on = s.id === secId && !body.hasAttribute('data-nosec');
    return '<div class="grp"><a class="top' + (on ? ' on' : '') + '" href="' + s.href + '"><span>' + s.n + '</span>' + s.t + '</a>' +
      (s.subs.length ? '<div class="subs">' + s.subs.map(function (x) { return '<a href="' + x[1] + '"' + (x[1] === here ? ' class="on"' : '') + '>' + x[0] + '</a>'; }).join('') + '</div>' : '') + '</div>';
  }).join('');
  var ov = el('<nav class="ov" aria-label="Menu principal"><div class="ov-in">' + groups + footer() + '</div></nav>');
  stage.appendChild(ov);
  var mbtn = hd.querySelector('.menu');
  function toggle(force) {
    var open = typeof force === 'boolean' ? force : !stage.classList.contains('open');
    stage.classList.toggle('open', open);
    mbtn.setAttribute('aria-expanded', open);
    mbtn.setAttribute('aria-label', open ? 'Fermer le menu' : 'Ouvrir le menu');
    if (open) Array.prototype.forEach.call(ov.querySelectorAll('.grp'), function (g, i) { g.style.animationDelay = (i * 0.05) + 's'; });
  }
  mbtn.addEventListener('click', function () { toggle(); });
  ov.addEventListener('click', function (e) { var a = e.target.closest('a'); if (a && a.getAttribute('href').indexOf('index.html#') === 0 && isHome) toggle(false); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') toggle(false); });

  /* ---- avatar AIT ---- */
  if (!body.hasAttribute('data-noavatar')) {
    stage.appendChild(el('<a class="avatar" href="index.html#agent" aria-label="Parler à AIT, notre agent"><img src="assets/avatar.png" alt="AIT"></a>'));
  }

  /* ---- carrousel du bas ---- */
  var nav = el('<nav class="nav" aria-label="Rubriques"></nav>');
  stage.appendChild(nav);
  var items = isHome
    ? [{ t: 'Pour qui ?', href: '#pour-qui' }, { t: 'Nos services', href: '#services' }, { t: 'AIT', href: '#agent' }]
    : SECTIONS.map(function (s) { return { t: s.t, href: s.href }; });
  function drawNav(cur) {
    var h = '';
    [cur - 1, cur, cur + 1].forEach(function (k, j) {
      if (k < 0 || k >= items.length) return;
      h += '<a class="lab p' + j + (j === 1 ? ' on' : '') + '" href="' + items[k].href + '">' + items[k].t + '</a>' +
        '<span class="star p' + j + (j === 1 ? ' on' : '') + '"></span>';
    });
    var ic = page === 'espace' || page === 'documentation' ? 0 : (isHome ? 1 : -1);
    nav.innerHTML = '<div class="track"></div>' + h +
      '<button class="chev l" aria-label="Rubrique précédente">' + CL + '</button>' +
      '<button class="chev r" aria-label="Rubrique suivante">' + CR + '</button>' +
      '<div class="icons">' +
      '<a class="ic p0' + (ic === 0 ? ' on' : '') + '" href="espace.html" aria-label="Espace client">' + I_USER + '</a>' +
      '<a class="ic p1' + (ic === 1 ? ' on' : '') + '" href="index.html#services" aria-label="Nos services">' + I_CASE + '</a>' +
      '<a class="ic p2" href="' + PSS.wa('Bonjour Praetorian Sentinel Smart, ') + '" target="_blank" rel="noopener" aria-label="WhatsApp PSS">' + I_SCREEN + '</a></div>';
  }
  var cur = isHome ? 0 : secIdx;
  function go(d) {
    var k = (cur + d + items.length) % items.length;
    if (isHome) { location.hash = items[k].href; } else { location.href = items[k].href; }
  }
  drawNav(cur);
  nav.addEventListener('click', function (e) {
    if (e.target.closest('.chev.l')) go(-1);
    else if (e.target.closest('.chev.r')) go(1);
  });
  var x0 = null;
  nav.addEventListener('touchstart', function (e) { x0 = e.touches[0].clientX; }, { passive: true });
  nav.addEventListener('touchend', function (e) {
    if (x0 === null) return; var dx = e.changedTouches[0].clientX - x0; x0 = null;
    if (Math.abs(dx) > 45) go(dx < 0 ? 1 : -1);
  });
  window.PSS.setNav = function (k) { cur = k; drawNav(k); };
  window.PSS.toggleMenu = toggle;
})();
