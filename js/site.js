/* Praetorian Sentinel Smart — gabarit commun : en-tête (MENU / CONTACT), menu plein écran, carrousel du bas, pied de page */
(function () {
  var WA = '213555372345';
  var MAIL = 'men-ay_pro-managment@outlook.fr';
  var FB = 'https://www.facebook.com/search/top?q=Praetorian%20Sentinel%20Smart';
  var SECTIONS = [
    { id: 'accueil', n: '01', t: 'Accueil', href: 'index.html', subs: [['Pour qui ?', 'index.html#pour-qui'], ['Nos solutions', 'index.html#services'], ['AIT', 'index.html#agent']] },
    { id: 'cabinet', n: '02', t: 'Le cabinet', href: 'cabinet.html', s: 'Qui nous sommes et comment nous travaillons', subs: [['Notre méthode', 'methode.html'], ['Nos références', 'references.html'], ['Notre conformité', 'notreconformite.html'], ['Nous rejoindre', 'carrieres.html']] },
    { id: 'segments', n: '03', t: 'Nos segments', href: 'divisions.html', s: "Pour qui travaillons-nous et nos domaines d'intervention", subs: [['3.1 Réglementaire & investissement', 'division-2.html'], ["3.2 Maîtrise d'ouvrage", 'division-3.html'], ['3.3 Ingénierie financière', 'division-4.html'], ['3.4 Architecture intelligente augmentée', 'division-1.html']] },
    { id: 'academie', n: '04', t: 'Académie PSS', href: 'academie.html', s: 'Transmettre, former, élever les standards', subs: [] },
    { id: 'offres', n: '05', t: 'Nos offres', href: 'toutes-les-offres.html', s: 'Ce que nous proposons et nos solutions', subs: [['Diagnostic', 'diagnostic.html'], ['Toutes les offres', 'toutes-les-offres.html']] },
    { id: 'avis', n: '06', t: 'Avis clients', href: 'avis.html', s: 'Ce qu’ils disent de nous et nos résultats', subs: [['6.1 Références professionnelles', 'references.html'], ['6.2 Donner votre avis', 'donner-mon-avis.html']] },
    { id: 'contact', n: '07', t: 'Contactez-nous', href: 'contact.html', s: 'Entrer en relation avec le cabinet', subs: [['Contact', 'contact.html'], ['Questions fréquentes', 'faq.html']] }
  ];
  var EXTRA = [{ id: 'espace', n: '··', t: 'Espace client', href: 'espace.html', subs: [['Base documentaire', 'documentation.html']] }];
  var LEGAL = [['Mentions légales', 'mentions.html'], ['Confidentialité', 'confidentialite.html'], ['Conditions', 'conditions.html'], ['Conformité', 'notreconformite.html'], ['FAQ', 'faq.html'], ['Plan du site', 'plan.html']];

  var ARROW = '<svg viewBox="0 0 14 14"><path d="M3 11 11 3M5 3h6v6"/></svg>';
  var CL = '<svg viewBox="0 0 13 20"><path d="M11 2 3 10l8 8"/></svg>';
  var CR = '<svg viewBox="0 0 13 20"><path d="M2 2l8 8-8 8"/></svg>';
  var I_USER = '<svg viewBox="0 0 24 24"><circle cx="12" cy="8" r="4"/><path d="M4 21c0-4.4 3.6-7 8-7s8 2.6 8 7"/></svg>';
  var I_CASE = '<svg viewBox="0 0 24 24"><rect x="3" y="8" width="18" height="12" rx="2.5"/><path d="M9 8V6a2 2 0 0 1 2-2h2a2 2 0 0 1 2 2v2M3 13h18M11 13v2h2v-2"/></svg>';
  var I_SCREEN = '<svg viewBox="0 0 24 24"><rect x="4" y="4" width="16" height="12" rx="1.5"/><path d="M8 20h8M12 16v4"/></svg>';
  var I_BARS = '<svg viewBox="0 0 30 26"><path d="M3 5h24M3 13h24M3 21h24"/></svg>';
  var I_MAIL = '<svg viewBox="0 0 30 26"><rect x="3" y="4" width="24" height="18" rx="2"/><path d="M3 6l12 9 12-9"/></svg>';

  var body = document.body;
  var stage = document.querySelector('.stage');
  var page = body.getAttribute('data-page') || '';
  var secId = body.getAttribute('data-sec') || 'accueil';
  var secIdx = Math.max(0, SECTIONS.findIndex(function (s) { return s.id === secId; }));
  var isHome = page === 'index';
  if (!isHome) stage.classList.add('inner');

  function el(html) { var d = document.createElement('div'); d.innerHTML = html.trim(); return d.firstChild; }
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }

  window.PSS = {
    WA: WA, MAIL: MAIL, FB: FB, SECTIONS: SECTIONS, ARROW: ARROW, esc: esc,
    wa: function (text) { return 'https://wa.me/' + WA + (text ? '?text=' + encodeURIComponent(text) : ''); },
    mail: function (subject, text) { return 'mailto:' + MAIL + '?subject=' + encodeURIComponent(subject || '') + '&body=' + encodeURIComponent(text || ''); }
  };

  /* ---- fond ---- */
  stage.insertBefore(el('<div class="bgland" aria-hidden="true"></div>'), stage.firstChild);

  /* ---- en-tête ---- */
  var hd = el('<header class="hd">' +
    '<a href="index.html" aria-label="Accueil"><img class="emblem" src="assets/emblem-cadre.png" alt="Emblème Praetorian Sentinel Smart"></a>' +
    '<a href="index.html" aria-label="Praetorian Sentinel Smart"><img class="wordmark" src="assets/praetorian.png" alt="Praetorian Sentinel Smart"></a>' +
    '<button class="pill menu" aria-label="Ouvrir le menu" aria-expanded="false">MENU ' + I_BARS + '</button>' +
    '<a class="pill contact" href="contact.html">CONTACT ' + I_MAIL + '</a>' +
    '<div class="hline"></div><span class="scout"></span></header>');
  stage.appendChild(hd);
  var scout = hd.querySelector('.scout');
  function setScout(k) { scout.style.left = 'calc(' + (915 - k * 80) + ' * var(--u))'; }
  setScout(secIdx);

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
    var on = s.id === secId;
    return '<div class="grp"><a class="top' + (on ? ' on' : '') + '" href="' + (isHome && s.id !== 'accueil' && s.id !== 'espace' ? 'index.html#' + s.id : s.href) + '">' + s.t + '</a>' +
      (s.subs.length ? '<div class="subs">' + s.subs.map(function (x) { return '<a href="' + x[1] + '"' + (x[1] === here ? ' class="on"' : '') + '>' + x[0].replace(/^\d+\.\d+\s+/, '') + '</a>'; }).join('') + '</div>' : '') + '</div>';
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
  ov.addEventListener('click', function (e) { var a = e.target.closest('a'); if (a && isHome && a.getAttribute('href').indexOf('index.html#') === 0) toggle(false); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') toggle(false); });

  /* ---- carrousel du bas ---- */
  var nav = el('<nav class="nav" aria-label="Rubriques"></nav>');
  stage.appendChild(nav);
  var items = SECTIONS.map(function (s) { return { t: s.t, href: isHome ? (s.id === 'accueil' ? '#' : '#' + s.id) : s.href, s: s.s, n: s.n }; });
  var cur = secIdx;
  function drawNav(k, caption) {
    cur = k;
    var h = '<div class="cap' + (caption ? ' on' : '') + '">' + (caption ? '<div class="t">' + items[k].t.toUpperCase() + '</div><div class="s">' + (items[k].s || '') + '</div>' : '') + '</div><div class="labs">';
    [k - 1, k, k + 1].forEach(function (j, p) {
      if (j < 0 || j >= items.length) return;
      h += '<a class="lab p' + p + (p === 1 ? ' on' : '') + '" href="' + items[j].href + '" data-k="' + j + '">' + (p === 1 ? items[j].t : items[j].t.replace('Nos segments', 'Nos<br>segments').replace('Académie PSS', 'Académie<br>PSS').replace('Contactez-nous', 'Contactez-<br>nous')) + '</a>';
    });
    h += '</div><div class="track"></div>';
    [0, 1, 2].forEach(function (p) { if (k - 1 + p >= 0 && k - 1 + p < items.length) h += '<span class="star p' + p + (p === 1 ? ' on' : '') + '"></span>'; });
    var ic = page === 'espace' || page === 'documentation' ? 0 : (isHome || page === 'index' ? 1 : -1);
    h += '<button class="chev l" aria-label="Rubrique précédente">' + CL + '</button><button class="chev r" aria-label="Rubrique suivante">' + CR + '</button>' +
      '<a class="ic i0' + (ic === 0 ? ' on' : '') + '" href="espace.html" aria-label="Espace client">' + I_USER + '</a>' +
      '<a class="ic i1' + (ic === 1 ? ' on' : '') + '" href="' + (isHome ? '#services' : 'index.html#services') + '" aria-label="Nos solutions">' + I_CASE + '</a>' +
      '<a class="ic i2" href="' + PSS.wa('Bonjour Praetorian Sentinel Smart, ') + '" target="_blank" rel="noopener" aria-label="WhatsApp PSS">' + I_SCREEN + '</a>';
    nav.innerHTML = h;
    setScout(k);
  }
  window.PSS.go = null; /* l'accueil peut remplacer la navigation */
  function go(d) {
    if (window.PSS.go) return window.PSS.go(d);
    var k = (cur + d + items.length) % items.length;
    location.href = items[k].href;
  }
  drawNav(cur, false);
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
  window.PSS.setNav = drawNav;
  window.PSS.toggleMenu = toggle;
  window.PSS.items = items;
})();
