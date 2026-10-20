/* Praetorian Sentinel Smart — gabarit commun : en-tête (MENU / CONTACT), menu plein écran, carrousel du bas, pied de page */
(function () {
  var WA = '213555372345';
  var MAIL = 'men-ay_pro-managment@outlook.fr';
  var FB = 'https://www.facebook.com/search/top?q=Praetorian%20Sentinel%20Smart';
  var SECTIONS = [
    { id: 'accueil', n: '01', t: 'Accueil', href: 'index.html', subs: [['Vous êtes ?', 'index.html#pour-qui'], ['Nos solutions', 'index.html#services'], ['AIT', 'index.html#agent']] },
    { id: 'cabinet', n: '02', t: 'Le cabinet', href: 'cabinet.html', s: 'Qui nous sommes et comment nous travaillons', subs: [['Notre méthode', 'methode.html'], ["Nos domaines d'expertise", 'divisions.html'], ['Nos références', 'references.html'], ['Notre conformité', 'notreconformite.html'], ['Nous rejoindre', 'carrieres.html']] },
    { id: 'parcours', n: '03', t: 'Votre parcours', q: 'À qui nous adressons-nous ?', href: 'parcours.html', s: 'À qui nous adressons-nous ?', subs: [['Particuliers · crédit depuis l’étranger (5 pays)', 'parcours.html#particuliers'], ['Investisseurs · diagnostic initial (PDF)', 'parcours.html#investisseurs'], ['Porteurs de projet · diagnostic de lancement (PDF)', 'parcours.html#porteurs'], ['Professionnels et entreprises · IA métier', 'parcours.html#professionnels'], ['Trouver mon offre en 3 étapes', 'parcours.html#filtre'], ['Accompagnement sur devis', 'parcours.html#devis']] },
    { id: 'ia', n: '04', t: 'IA métier', href: 'ia-metier.html', s: 'L’intelligence artificielle augmentée, adaptée à votre métier', subs: [['Documentaire interactif', 'ia-metier.html#documenter'], ['Veille métier', 'ia-metier.html#surveiller'], ['Assistants et automatisation', 'ia-metier.html#automatiser']] },
    { id: 'academie', n: '05', t: 'Académie PSS', href: 'academie.html', s: 'Transmettre, former, élever les standards', subs: [['Nos formations', 'academie.html']] },
    { id: 'avis', n: '06', t: 'Avis clients', href: 'avis.html', s: 'Ce qu’ils disent de nous et nos résultats', subs: [['Références professionnelles', 'references.html'], ['Donner votre avis', 'donner-mon-avis.html']] },
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
  stage.insertBefore(el('<div class="bgwrap" aria-hidden="true"><div class="bgland"></div></div>'), stage.firstChild);

  /* ---- en-tête ---- */
  var hd = el('<header class="hd">' +
    '<a href="index.html" aria-label="Accueil"><img class="emblem" src="assets/emblem-cadre.png" alt="Emblème Praetorian Sentinel Smart"></a>' +
    '<a href="index.html" aria-label="Praetorian Sentinel Smart"><img class="wordmark" src="assets/praetorian.png" alt="Praetorian Sentinel Smart"></a>' +
    '<button class="pill menu" aria-label="Ouvrir le menu" aria-expanded="false">MENU ' + I_BARS + '</button>' +
    '<a class="pill contact" href="contact.html">CONTACT ' + I_MAIL + '</a>' +
    '<div class="hline"></div><span class="scout"></span></header>');
  stage.appendChild(hd);
  /* l'étoile de la ligne du haut va et vient en permanence (animation CSS « scoutgo ») */

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
  if (pageEl && !pageEl.classList.contains('app')) pageEl.insertAdjacentHTML('beforeend', footer());

  /* ---- menu plein écran ---- */
  var here = location.pathname.split('/').pop() || 'index.html';
  var groups = SECTIONS.concat(EXTRA).map(function (s) {
    var on = s.id === secId;
    return '<div class="grp"><a class="top' + (on ? ' on' : '') + (s.q ? ' hasq' : '') + '" href="' + (isHome && s.id !== 'accueil' && s.id !== 'espace' ? 'index.html#' + s.id : s.href) + '">' + s.t + (s.q ? '<span class="q">' + s.q + '</span>' : '') + '</a>' +
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

  /* ---- carrousel du bas : une position continue (0 = Accueil … 6 = Contactez-nous) qui suit le doigt ---- */
  var nav = el('<nav class="nav" aria-label="Rubriques"></nav>');
  stage.appendChild(nav);
  var items = SECTIONS.map(function (s) { return { t: s.t, href: isHome ? (s.id === 'accueil' ? '#' : '#' + s.id) : s.href, s: s.s, n: s.n }; });
  var N = items.length, SLOT = 254, CX = 591;
  var ic = page === 'espace' || page === 'documentation' ? 0 : (isHome ? 1 : -1);
  var hh = '<div class="navdrag"></div><div class="cap"></div><div class="labs">';
  items.forEach(function (it, j) { hh += '<a class="lab" draggable="false" href="' + it.href + '" data-k="' + j + '">' + esc(it.t) + '</a>'; });
  hh += '<span class="arc"></span></div><div class="track"></div>';
  items.forEach(function (it, j) { hh += '<span class="star" data-k="' + j + '"></span>'; });
  hh += '<span class="star0"></span>' +
    '<button class="chev l" aria-label="Rubrique précédente">' + CL + '</button><button class="chev r" aria-label="Rubrique suivante">' + CR + '</button>' +
    '<a class="ic i0' + (ic === 0 ? ' on' : '') + '" href="espace.html" aria-label="Espace client">' + I_USER + '</a>' +
    '<a class="ic i1' + (ic === 1 ? ' on' : '') + '" href="' + (isHome ? '#services' : 'index.html#services') + '" aria-label="Nos solutions">' + I_CASE + '</a>' +
    '<a class="ic i2" href="' + PSS.wa('Bonjour Praetorian Sentinel Smart, ') + '" target="_blank" rel="noopener" aria-label="WhatsApp PSS">' + I_SCREEN + '</a>';
  nav.innerHTML = hh;
  var labs = [].slice.call(nav.querySelectorAll('.lab')), stars = [].slice.call(nav.querySelectorAll('.star')), cap = nav.querySelector('.cap'), arc = nav.querySelector('.arc');
  var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;

  var pos = secIdx, anim = null, drag = null, listeners = [], settlers = [], showCap = false, capK = -1;
  function U() { return Math.min(stage.clientWidth || window.innerWidth, 430) / 1166; }
  function mix(a, b, t) { return a + (b - a) * t; }
  function clamp(v, a, b) { return v < a ? a : (v > b ? b : v); }

  function render() {
    var u = U();
    for (var j = 0; j < N; j++) {
      var d = j - pos, ad = Math.abs(d), t = Math.min(1, ad);
      var e = labs[j];
      var sc = mix(35 / 27, 1, t);
      var op = ad <= 1.15 ? 1 : clamp(1 - (ad - 1.15) * 2.2, 0, 1);
      if (isHome && j === 0) op *= clamp(pos / 0.7, 0, 1);   /* sur l'accueil, pas d'étiquette « Accueil » */
      var c = Math.min(1, ad * 1.1);
      e.style.transform = 'translate3d(' + (d * SLOT * u).toFixed(2) + 'px,0,0) scale(' + sc.toFixed(3) + ')';
      e.style.opacity = op.toFixed(3);
      e.style.color = 'rgb(' + Math.round(mix(236, 34, c)) + ',' + Math.round(mix(241, 46, c)) + ',' + Math.round(mix(245, 60, c)) + ')';
      e.style.pointerEvents = op > 0.3 ? 'auto' : 'none';
      var st = stars[j];
      st.style.transform = 'translate3d(' + (d * SLOT * u).toFixed(2) + 'px,0,0)';
      st.style.opacity = (ad < 0.3 ? ad / 0.3 : (ad > 1.6 ? clamp(1 - (ad - 1.6) * 2.5, 0, 1) : 1)).toFixed(3);
    }
    if (isHome) arc.style.opacity = clamp(pos / 0.7, 0, 1).toFixed(3);
    var k = Math.round(pos), still = !drag && !anim && Math.abs(pos - k) < 0.01;
    if (still && showCap && k > 0) {
      if (capK !== k) { cap.innerHTML = '<div class="t">' + esc(items[k].t.toUpperCase()) + '</div><div class="s">' + esc(items[k].s || '') + '</div>'; capK = k; }
      cap.classList.add('on');
    } else cap.classList.remove('on');
    for (var i = 0; i < listeners.length; i++) listeners[i](pos);
  }
  function setPos(p) { pos = p; render(); }
  function ease(t) { return t < .5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2; }
  function easeOut(t) { return 1 - Math.pow(1 - t, 3); }
  function stopAnim() { if (anim) { cancelAnimationFrame(anim.raf); anim = null; } }
  function animateTo(target, ms, fn, out) {
    stopAnim();
    var from = pos, t0 = performance.now(), dist = Math.abs(target - from);
    if (ms == null) ms = 380 + 300 * Math.min(dist, 3);
    if (reduce) ms = Math.min(ms, 200);
    if (dist < 0.001) { pos = target; render(); settle(); if (fn) fn(); return; }
    anim = { raf: 0 };
    (function step(now) {
      var t = clamp((now - t0) / ms, 0, 1), e = out ? easeOut(t) : ease(t);
      pos = from + (target - from) * e;
      if (t >= 1) { pos = target; anim = null; render(); settle(); if (fn) fn(); return; }
      render(); anim.raf = requestAnimationFrame(step);
    })(t0);
  }
  function settle() { var k = Math.round(pos); for (var i = 0; i < settlers.length; i++) settlers[i](k); }

  /* glisser : la barre (1 case = 1 rubrique) et, sur l'accueil, la scène */
  var moved = false, dragEnd = 0;
  function recent() { return moved && performance.now() - dragEnd < 450; }
  function down(e, perPx) {
    if (e.button > 0) return;
    stopAnim();
    drag = { x: e.clientX, y: e.clientY, p: pos, axis: null, per: perPx, hist: [[performance.now(), pos]], id: e.pointerId, tgt: e.currentTarget };
    moved = false;
  }
  function moveP(e) {
    if (!drag || e.pointerId !== drag.id) return;
    var dx = e.clientX - drag.x, dy = e.clientY - drag.y;
    if (!drag.axis) {
      if (Math.abs(dx) < 7 && Math.abs(dy) < 7) return;
      drag.axis = Math.abs(dx) >= Math.abs(dy) ? 'x' : 'y';
      if (drag.axis === 'y' && drag.tgt === nav) { drag = null; return; }
      moved = true;
      try { drag.tgt.setPointerCapture(drag.id); } catch (er) {}
    }
    var delta = drag.axis === 'x' ? -dx : -dy;
    var p = drag.p + delta / drag.per;
    if (p < 0) p = -Math.pow(-p, 0.6) * 0.35;
    if (p > N - 1) p = N - 1 + Math.pow(p - (N - 1), 0.6) * 0.35;
    pos = p;
    var now = performance.now(); drag.hist.push([now, pos]); if (drag.hist.length > 6) drag.hist.shift();
    render();
  }
  function up(e) {
    if (!drag || e.pointerId !== drag.id) return;
    var d = drag; drag = null;
    if (!moved) { render(); return; }
    dragEnd = performance.now();
    var h = d.hist, a = h[0], b = h[h.length - 1], dt = Math.max(16, b[0] - a[0]);
    var v = (b[1] - a[1]) / dt * 1000;               /* rubriques par seconde */
    var target = Math.round(clamp(pos + v * 0.18, Math.floor(pos) - (v < -0.8 ? 1 : 0), Math.ceil(pos) + (v > 0.8 ? 1 : 0)));
    target = clamp(target, 0, N - 1);
    animateTo(target, 260 + 260 * Math.min(1.5, Math.abs(target - pos)), null, true);
  }
  window.addEventListener('pointermove', moveP, { passive: true });
  window.addEventListener('pointerup', up);
  window.addEventListener('pointercancel', up);
  nav.addEventListener('pointerdown', function (e) { if (e.target.closest('.chev,.ic')) { moved = false; return; } down(e, SLOT * U()); });
  /* un clic après un glissement ne doit pas ouvrir de lien */
  nav.addEventListener('click', function (e) { if (recent()) { e.preventDefault(); e.stopPropagation(); moved = false; } }, true);

  window.PSS.go = null; /* l'accueil peut remplacer la navigation */
  function go(d) {
    if (window.PSS.go) return window.PSS.go(d);
    var k = Math.round(pos) + d;
    if (k < 0) k = N - 1; if (k > N - 1) k = 0;
    animateTo(k);
  }
  nav.addEventListener('click', function (e) {
    if (e.target.closest('.chev.l')) { e.preventDefault(); go(-1); return; }
    if (e.target.closest('.chev.r')) { e.preventDefault(); go(1); return; }
    var a = e.target.closest('.lab');
    if (a && !isHome) { e.preventDefault(); var n = +a.getAttribute('data-k'); if (n === Math.round(pos)) location.href = items[n].href; else animateTo(n); }
  });
  /* pages intérieures : on ouvre la page de la rubrique où la barre s'arrête */
  if (!isHome) settlers.push(function (k) { if (k !== secIdx) location.href = items[k].href; });
  window.addEventListener('resize', render);
  render();

  window.PSS.nav = {
    get pos() { return pos; }, setPos: setPos, animateTo: animateTo, stop: stopAnim,
    onChange: function (fn) { listeners.push(fn); }, onSettle: function (fn) { settlers.push(fn); },
    caption: function (on) { showCap = on; render(); },
    dragFrom: function (e, perPx) { down(e, perPx); },
    get dragging() { return !!drag && moved; }, get justMoved() { return recent(); }
  };
  window.PSS.toggleMenu = toggle;
  window.PSS.items = items;
})();
