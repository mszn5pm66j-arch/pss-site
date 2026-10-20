/* Praetorian Sentinel Smart — réglages des plateformes intégrées dans le site */
(function () {
  var q = new URLSearchParams(location.search);
  /* plateforme investissement : profil présélectionné depuis « Votre parcours » */
  var profil = q.get('profil');
  if (profil) {
    var go = function () {
      var s = document.getElementById('profil');
      if (!s || !s.querySelector('option[value="' + profil + '"]')) return;
      s.value = profil;
      s.dispatchEvent(new Event('input', { bubbles: true }));
      s.dispatchEvent(new Event('change', { bubbles: true }));
    };
    if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', go); else go();
  }
  /* charte PSS des PDF : police Jura et emblème complet, préchargés pour que le document se prépare sans attente */
  function b64(buf) {
    var bytes = new Uint8Array(buf), out = '', step = 0x8000;
    for (var i = 0; i < bytes.length; i += step) out += String.fromCharCode.apply(null, bytes.subarray(i, i + step));
    return btoa(out);
  }
  function load(url) { return fetch(url).then(function (r) { if (!r.ok) throw new Error(url); return r.arrayBuffer(); }).then(b64); }
  window.PSS_PDF = window.PSS_PDF || {};
  Promise.all([load('../fonts/Jura-Regular.ttf'), load('../fonts/Jura-SemiBold.ttf'), load('../assets/emblem-full.jpg')])
    .then(function (r) { window.PSS_PDF.reg = r[0]; window.PSS_PDF.semi = r[1]; window.PSS_PDF.emb = 'data:image/jpeg;base64,' + r[2]; })
    .catch(function () { /* en cas d'échec, les PDF gardent la police standard */ });
})();
