# Praetorian Sentinel Smart — site (brouillon)

Reproduction du portail PSS hébergée sur GitHub Pages.

- `index.html` : accueil (trois questions, Pour qui ?, Nos services, AIT)
- `css/style.css` : charte (police Jura, couleurs, gabarit)
- `js/site.js` : en-tête, menu plein écran, carrousel du bas, avatar AIT, pied de page communs
- `_build/build.py` : génère les pages intérieures (`python3 _build/build.py`)
- `assets/` : fond, emblème, écriture PRAETORIAN, avatar ; `fonts/` : Jura (licence OFL)
- `parcours.html`, `ia-metier.html`, `credit.html`, `diagnostic-initial.html` : générées par `_build/build.py`
- `plateformes/` : plateformes crédit et investissement intégrées au site, dans la charte PSS (`python3 _build/plateformes.py`
  à partir des sources `_build/sources/`) ; PDF produits par jsPDF (`plateformes/jspdf.umd.min.js`, licence MIT) avec la police Jura (`fonts/`, licence OFL)
