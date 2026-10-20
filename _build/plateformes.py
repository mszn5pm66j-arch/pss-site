# Intègre les plateformes crédit et investissement au site PSS (python3 _build/plateformes.py depuis la racine du dépôt).
# Sources d'origine : _build/sources/credit.html et _build/sources/investissement.html (copies des plateformes, à remplacer
# lors d'une mise à jour, puis relancer ce script). Résultat : plateformes/credit.html et plateformes/investissement.html.
#
# Ce que fait le script, sans toucher au contenu des plateformes ni au contenu des PDF :
#   1. habillage du site (pss-integration.css) et préchargement de la police Jura et de l'emblème (pss-integration.js) ;
#   2. logique de paiement du site : le diagnostic qui produit le PDF reste gratuit, tout le reste est « Sur devis »,
#      demandé depuis la page Contact du site (plus de renvoi WhatsApp depuis les pages) ;
#   3. PDF dans la charte PSS : fond nuit, emblème complet en haut, bloc de contacts en bas, police Jura, couleurs du site.
#      Les PDF sont produits par jsPDF, livré avec le site (plateformes/jspdf.umd.min.js).
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, '_build', 'sources')
OUT = os.path.join(ROOT, 'plateformes')

# ---------------------------------------------------------------- kit PDF commun (même interface que l'original, sur jsPDF)
KIT = r'''async function pssKit(o){
  const J = window.jspdf && window.jspdf.jsPDF; if(!J) return null;
  const doc = new J({unit:"pt", format:"a4", compress:true});
  doc.setProperties({title:o.title, author:"Praetorian Sentinel Smart", creator:"Praetorian Sentinel Smart", subject:o.title});
  try{ doc.setLanguage("fr-FR"); }catch(e){}
  const RS = window.PSS_PDF || {};
  let fam = "helvetica";
  if(RS.reg && RS.semi){ try{
    doc.addFileToVFS("Jura-Regular.ttf", RS.reg); doc.addFont("Jura-Regular.ttf", "Jura", "normal"); doc.addFont("Jura-Regular.ttf", "Jura", "italic");
    doc.addFileToVFS("Jura-SemiBold.ttf", RS.semi); doc.addFont("Jura-SemiBold.ttf", "Jura", "bold"); fam = "Jura"; }catch(e){ fam = "helvetica"; } }
  const STY = {r:"normal", b:"bold", i:"italic"};
  /* charte PSS : couleurs de l'original converties selon leur rôle (texte, fond, trait) */
  const MT = {"#0C2949":"#EAF7FD","#13263C":"#E6EEF4","#16242E":"#E6EEF4","#4A6076":"#B3C2CD","#3E515C":"#B3C2CD","#7B8FA3":"#8597A6","#6F818B":"#8597A6",
    "#B8912E":"#5ACEF6","#9A7233":"#5ACEF6","#9A6414":"#F0C070","#D9B65C":"#8FE0FF","#C9A25A":"#8FE0FF","#1D6B4E":"#5FF0B0","#3A6B4D":"#5FF0B0","#2E5A3F":"#7FE8B8",
    "#9B2C2C":"#F2A6A6","#9B3B2E":"#F2A6A6","#6E2C23":"#F2B8B8","#B3701F":"#F0C070","#1F5A96":"#8FD8FB","#1F4E7A":"#8FD8FB","#2E5C8A":"#8FD8FB",
    "#C8D6E6":"#9FB3C2","#D9CDB2":"#9FB3C2","#000000":"#E6EEF4"};
  const MF = {"#FFFFFF":"#0B1826","#F4F7FB":"#0A1826","#F6F5F0":"#0A1826","#EDEBE4":"#0C1C2C","#F6EEDA":"#0C2438","#EFE6D2":"#0C2438","#E8F0F9":"#0C2438",
    "#E6F2EC":"#0B2A22","#FBF1E0":"#2A2412","#F8E9E9":"#2C1616","#DCE4EE":"#12283A","#0C2949":"#0F2F48","#16242E":"#0F2F48","#B8912E":"#39C3FF","#9A7233":"#2A8FC4",
    "#9A6414":"#F0C070","#CFCBBF":"#1E3A50","#D6E1EC":"#1E3A50","#E0CB94":"#2A6A8F","#DCCBA5":"#2A6A8F","#D9B65C":"#5ACEF6","#C9A25A":"#5ACEF6",
    "#1D6B4E":"#5FF0B0","#3A6B4D":"#5FF0B0","#9B2C2C":"#F2A6A6","#9B3B2E":"#F2A6A6","#B3701F":"#F0C070","#1F5A96":"#5ACEF6","#000000":"#E6EEF4"};
  const MS = {"#D6E1EC":"#24465E","#CFCBBF":"#24465E","#E0CB94":"#2A6A8F","#DCCBA5":"#2A6A8F","#B8912E":"#39C3FF","#9A7233":"#39C3FF","#FFFFFF":"#24465E",
    "#F4F7FB":"#24465E","#E6F2EC":"#1E5A46","#FBF1E0":"#5A4A20","#F8E9E9":"#5A2A2A","#E8F0F9":"#24465E"};
  const hex = h => "#" + String(h).replace("#", "").toUpperCase();
  const rgb = h => { const n = parseInt(String(h).replace("#", ""), 16); return [n >> 16 & 255, n >> 8 & 255, n & 255]; };
  const col = h => rgb(h);
  const ct = h => rgb(MT[hex(h)] || h), cf = h => rgb(MF[hex(h)] || h), cs = h => rgb(MS[hex(h)] || MT[hex(h)] || h);
  const clean = s => String(s ?? "").replace(/[    ]/g, " ").replace(/[‐‑]/g, "-").replace(/→/g, "->").replace(/↗/g, "").replace(/⋯/g, "…").replace(/[\u0000-\u001f]/g, "");
  const CS = {has:c => c >= 32};
  const F = {}; ["r", "b", "i"].forEach(k => F[k] = {widthOfTextAtSize:(s, sz) => { doc.setFont(fam, STY[k]); doc.setFontSize(sz); return doc.getTextWidth(String(s)); }});
  const K = {doc, F, col, clean, W:595.28, H:841.89, M:50, CW:487, R:537, BOT:772, y:0, n:0, page:doc, fam, RS};
  const paint = (p, fill) => { const st = (p.fill ? "F" : "") + (p.stroke ? "D" : ""); if(p.fill) doc.setFillColor(...(fill ? fill(p.fill) : cf(p.fill))); if(p.stroke){ doc.setDrawColor(...cs(p.stroke)); doc.setLineWidth(p.bw || .6); } return st; };
  K.wd = (s, sz, f = "r") => F[f].widthOfTextAtSize(clean(s), sz);
  K.t = (s, x, y, p = {}) => {
    const txt = clean(s); if(!txt) return 0;
    const k = p.f || "r", sz = p.s || 9; doc.setFont(fam, STY[k]); doc.setFontSize(sz);
    const w = doc.getTextWidth(txt), xx = p.a === "r" ? x - w : p.a === "c" ? x - w / 2 : x;
    doc.setTextColor(...(p.raw ? rgb(p.c || "#E6EEF4") : ct(p.c || "#000000"))); doc.text(txt, xx, y);
    return w;
  };
  K.wrap = (s, w, sz, f = "r") => {
    const out = [];
    String(s ?? "").split("\n").forEach(par => {
      const words = clean(par).split(/\s+/).filter(Boolean); let line = "";
      words.forEach(wd => { const tr = line ? line + " " + wd : wd; if(!line || F[f].widthOfTextAtSize(tr, sz) <= w) line = tr; else { out.push(line); line = wd; } });
      out.push(line);
    });
    return out;
  };
  K.para = (s, x, y, w, p = {}) => { const sz = p.s || 9, lh = p.lh || sz * 1.55, ls = K.wrap(s, w, sz, p.f || "r"); ls.forEach((l, i) => K.t(l, x, y + i * lh, p)); return ls.length * lh; };
  K.rich = (runs, w, sz, ind = 0) => {
    const lines = [[]]; let lw = ind;
    runs.forEach(r => clean(r.t).split(/(\s+)/).forEach(tok => {
      if(!tok) return;
      const sp = /^\s+$/.test(tok), tw = F[r.f || "r"].widthOfTextAtSize(sp ? " " : tok, r.s || sz), cur = lines[lines.length - 1];
      if(sp){ if(cur.length){ cur.push({t:" ", f:r.f, c:r.c, s:r.s, w:tw}); lw += tw; } return; }
      if(lw + tw > w && cur.length){ while(cur.length && cur[cur.length - 1].t === " ") lw -= cur.pop().w; lines.push([]); lw = 0; }
      lines[lines.length - 1].push({t:tok, f:r.f, c:r.c, s:r.s, w:tw}); lw += tw;
    }));
    return lines;
  };
  K.drawRich = (lines, x, y, sz, lh, dc, ind = 0) => { lines.forEach((ln, i) => { let xx = x + (i ? 0 : ind); ln.forEach(tk => { if(tk.t !== " ") K.t(tk.t, xx, y + i * lh, {s:tk.s || sz, f:tk.f || "r", c:tk.c || dc}); xx += tk.w; }); }); return lines.length * lh; };
  K.rect = (x, y, w, h, p = {}) => { const st = paint(p, p.raw ? rgb : null); if(!st) return; if(p.r){ const r = Math.min(p.r, h / 2, w / 2); doc.roundedRect(x, y, w, h, r, r, st); } else doc.rect(x, y, w, h, st); };
  K.line = (x1, y1, x2, y2, c, w = .5) => { doc.setDrawColor(...cs(c)); doc.setLineWidth(w); doc.line(x1, y1, x2, y2); };
  K.circle = (x, y, r, p = {}) => { const st = paint(p); if(st) doc.circle(x, y, r, st); };
  K.path = (d, x, y, p = {}) => {
    const pts = []; let closed = false;
    String(d).replace(/([MLZ])\s*(-?[\d.]+)?[\s,]*(-?[\d.]+)?/gi, (m, c, a, b) => { if(c.toUpperCase() === "Z") closed = true; else pts.push([+a, +b]); return m; });
    if(pts.length < 2) return;
    const st = paint(p) || "D";
    doc.lines(pts.slice(1).map((q, i) => [q[0] - pts[i][0], q[1] - pts[i][1]]), x + pts[0][0], y + pts[0][1], [1, 1], st, closed);
  };
  K.arrow = (x, y, c, w = 7) => { K.line(x, y - 2.1, x + w - 1.2, y - 2.1, c, .55); K.path(`M0 0 L2.4 1.5 L0 3 Z`, x + w - 2.2, y - 3.6, {fill:c}); return w; };
  K.check = (x, y, c) => K.path("M0 2.6 L2.1 4.8 L6 0.6", x, y, {stroke:c, bw:1.2});
  K.blocks = (x, y, c) => { for(let i = 0; i < 5; i++) K.rect(x + i * 3.1, y - 5.6, 2.3, 5.8, {fill:c}); return 15.5; };
  K.qr = (text, x, y, size) => {
    if(typeof window.PSS_QR !== "function") return false;
    let m; try{ m = window.PSS_QR(text); }catch(e){ return false; }
    const n = m.length, q = 3, cell = size / (n + 2 * q);
    doc.setFillColor(255, 255, 255); doc.rect(x, y, size, size, "F"); doc.setFillColor(0, 0, 0);
    m.forEach((row, r) => { let c = 0; while(c < n){ if(!row[c]){ c++; continue; } let e = c; while(e < n && row[e]) e++;
      doc.rect(x + (c + q) * cell, y + (r + q) * cell, (e - c) * cell + .05, cell + .05, "F"); c = e; } });
    return true;
  };
  K.newPage = () => { if(K.n > 0) doc.addPage([K.W, K.H], "p"); K.n++; doc.setFillColor(0, 0, 0); doc.rect(0, 0, K.W, K.H, "F"); o.header(K); o.footer(K); K.y = o.top || 100; };
  K.need = h => { if(K.y + h > K.BOT){ K.newPage(); return true; } return false; };
  K.blob = async () => doc.output("blob");
  return K;
}
/* charte PSS des documents : emblème complet en haut, bloc de contacts en bas (mêmes sur toutes les pages) */
function pssCharterHead(K, sous, date, ref){
  const M = K.M, R = K.R;
  let x = M;
  if(K.RS.emb){ try{ K.doc.addImage(K.RS.emb, "JPEG", M - 6, 7, 82, 56.6, "pss-emb", "FAST"); x = M + 84; }catch(e){} }
  K.t("Praetorian Sentinel Smart", x, 31, {s:12.5, f:"b", c:"#E8EDFA", raw:1});
  K.t(sous, x, 45.5, {s:7.6, c:"#7FA9EE", raw:1});
  K.t(date, R, 31, {s:7.6, c:"#8A97AD", a:"r", raw:1}); K.t(ref, R, 45.5, {s:7.6, c:"#8A97AD", a:"r", raw:1});
  K.doc.setDrawColor(57, 195, 255); K.doc.setLineWidth(.6); K.doc.line(M, 70, R, 70);
}
function pssCharterFoot(K){
  const M = K.M, R = K.R, d = K.doc;
  d.setDrawColor(36, 70, 94); d.setLineWidth(.5); d.line(M, 782, R, 782);
  let x = M; x += K.t("WhatsApp Business", x, 795, {s:7, f:"b", c:"#5A8FE0", raw:1}) + 5; x += K.t("+213 555 37 23 45", x, 795, {s:7, c:"#E6EEF4", raw:1}) + 14;
  x += K.t("Email", x, 795, {s:7, f:"b", c:"#5A8FE0", raw:1}) + 5; K.t("men-ay_pro-managment@outlook.fr", x, 795, {s:7, c:"#E6EEF4", raw:1});
  K.t("Algérie - France - Espagne - Allemagne - Belgique - Québec", M, 807, {s:6.5, c:"#5F78B0", raw:1});
  K.t("Document établi pour son seul destinataire · page " + K.n, R, 807, {s:6.5, c:"#8597A6", a:"r", raw:1});
}'''

# ---------------------------------------------------------------- fabrique jsPDF de la plateforme crédit (unité mm)
PDFNEW = r'''function pdfNew(sous){
  if(!(window.jspdf && window.jspdf.jsPDF)) return null;
  const doc = new window.jspdf.jsPDF({unit:"mm", format:"a4"});
  const W = 210, H = 297, M = 16, CW = W - 2*M;
  const RS = window.PSS_PDF || {};
  let FAM = "helvetica";
  if(RS.reg && RS.semi){ try{
    doc.addFileToVFS("Jura-Regular.ttf", RS.reg); doc.addFont("Jura-Regular.ttf", "Jura", "normal"); doc.addFont("Jura-Regular.ttf", "Jura", "italic");
    doc.addFileToVFS("Jura-SemiBold.ttf", RS.semi); doc.addFont("Jura-SemiBold.ttf", "Jura", "bold"); FAM = "Jura"; }catch(e){ FAM = "helvetica"; } }
  /* charte PSS : fond nuit, texte clair, accents bleus */
  const C = {navy:[127,206,246], gold:[57,195,255], ink:[230,238,244], soft:[179,194,205], faint:[133,151,166], bg:[11,26,40], ok:[95,240,176], warn:[240,192,112]};
  const cl = s => String(s ?? "").replace(/[  ]/g, " ").replace(/→/g, "->").replace(/↗/g, "").replace(/⋯/g, "…");
  const st = {y:0, page:1};
  const fond = () => { doc.setFillColor(0, 0, 0); doc.rect(0, 0, W, H, "F"); };
  const ap = doc.addPage.bind(doc); doc.addPage = function(){ ap.apply(null, arguments); fond(); return doc; };
  const t = (s, x, yy, o = {}) => { doc.setFont(FAM, o.b ? "bold" : o.i ? "italic" : "normal"); doc.setFontSize(o.s || 9); doc.setTextColor(...(o.c || C.ink)); doc.text(cl(s), x, yy, o.align ? {align:o.align} : undefined); };
  const tw = (s, sz, b) => { doc.setFont(FAM, b ? "bold" : "normal"); doc.setFontSize(sz); return doc.getTextWidth(cl(s)); };
  const wrap = (s, w, size) => { doc.setFont(FAM, "normal"); doc.setFontSize(size); return doc.splitTextToSize(cl(s), w); };
  const foot = () => {
    doc.setDrawColor(36, 70, 94); doc.setLineWidth(.3); doc.line(M, 279, W - M, 279);
    let x = M; t("WhatsApp Business", x, 283.5, {b:1, s:7, c:[90,143,224]}); x += tw("WhatsApp Business", 7, 1) + 1.8;
    t("+213 555 37 23 45", x, 283.5, {s:7, c:C.ink}); x += tw("+213 555 37 23 45", 7) + 5;
    t("Email", x, 283.5, {b:1, s:7, c:[90,143,224]}); x += tw("Email", 7, 1) + 1.8; t("men-ay_pro-managment@outlook.fr", x, 283.5, {s:7, c:C.ink});
    t("Algérie - France - Espagne - Allemagne - Belgique - Québec", M, 288, {s:6.5, c:[95,120,176]});
    t(`Praetorian Sentinel Smart — ${sous} — page ${st.page}`, W - M, 288, {s:6.5, c:C.faint, align:"right"});
  };
  const need = hh => { if(st.y + hh > 272){ foot(); doc.addPage(); st.page++; st.y = 20; } };
  fond();
  let hx = M;
  if(RS.emb){ try{ doc.addImage(RS.emb, "JPEG", M - 2, 2.5, 29, 20, "pss-emb", "FAST"); hx = M + 30; }catch(e){} }
  t("Praetorian Sentinel Smart", hx, 11, {b:1, s:12.5, c:[232,237,250]});
  t(sous, hx, 16.5, {s:8.5, c:[127,169,238]});
  t(new Date().toLocaleDateString("fr-FR", {day:"numeric", month:"long", year:"numeric"}), W - M, 16.5, {s:8.5, c:[138,151,173], align:"right"});
  doc.setDrawColor(57, 195, 255); doc.setLineWidth(.35); doc.line(M, 25, W - M, 25);
  st.y = 35;
  const h2 = s => { need(14); t(s, M, st.y, {b:1, s:10.5, c:C.navy}); st.y += 2; doc.setDrawColor(...C.gold); doc.setLineWidth(.5); doc.line(M, st.y, M + 14, st.y); st.y += 6; };
  const liste = (items, couleur) => items.forEach(it => {
    const a = wrap(it[0], CW - 10, 9), b = it[1] ? wrap(it[1], CW - 10, 8) : [];
    need(a.length * 4.2 + b.length * 3.7 + 4);
    doc.setFillColor(...(couleur || C.gold)); doc.circle(M + 1.6, st.y - 1.4, 1.1, "F");
    doc.setFont(FAM, "bold"); doc.setFontSize(9); doc.setTextColor(...C.ink); doc.text(a, M + 6, st.y); st.y += a.length * 4.2;
    if(b.length){ doc.setFont(FAM, "normal"); doc.setFontSize(8); doc.setTextColor(...C.faint); doc.text(b, M + 6, st.y); st.y += b.length * 3.7; }
    st.y += 3;
  });
  const meta = rows => { doc.setFillColor(...C.bg); doc.rect(M, st.y - 5, CW, 8 + rows.length * 6, "F");
    rows.forEach(m => { t(m[0], M + 4, st.y, {s:7.4, c:C.faint}); t(m[1], M + 74, st.y, {b:1, s:8.8}); st.y += 6; }); st.y += 8; };
  const portee = txt => { const po = wrap(txt, CW - 8, 7.6); need(po.length * 3.5 + 10);
    doc.setFillColor(...C.bg); doc.rect(M, st.y - 4, CW, po.length * 3.5 + 6, "F");
    doc.setFont(FAM, "normal"); doc.setFontSize(7.6); doc.setTextColor(...C.faint); doc.text(po, M + 4, st.y); };
  return {doc, C, M, CW, st, t, wrap, h2, liste, meta, portee, foot};
}'''

DEVIS = 'href="../contact.html" target="_top"'


def replace_once(s, a, b, label):
    if a not in s:
        raise SystemExit('introuvable : ' + label)
    return s.replace(a, b, 1)


def common(s, name):
    # 1. kit PDF
    a = s.find('async function pssKit(o){'); e = s.find('\n  return K;\n}\n', a)
    if a < 0 or e < 0:
        raise SystemExit('kit PDF introuvable : ' + name)
    s = s[:a] + KIT + s[e + len('\n  return K;\n}'):]
    # 2. en-têtes et pieds de page des documents
    def head(m):
        sous = m.group(1)
        return f'header:K => pssCharterHead(K, "{sous}", X.date, "Réf. " + X.ref),\n    footer:K => pssCharterFoot(K)}});'
    s, n = re.subn(r'header:K => \{\s*K\.rect\(0, 0, K\.W, 67.*?K\.t\("Praetorian Sentinel Smart".*?\n\s*K\.t\("([^"]+)".*?\n    \},\n    footer:K => \{.*?\}\}\);', head, s, flags=re.S)
    if n < 1:
        raise SystemExit('en-tête de document introuvable : ' + name)
    # 3. logique de paiement : le reste est sur devis, demandé depuis le site
    s = s.replace('Accès réservé · sur demande', 'Sur devis').replace('Accès réservé', 'Sur devis').replace('Accès sur demande.', 'Sur devis.').replace('Sur demande', 'Sur devis')
    s = re.sub(r'href="https://wa\.me/213555372345" target="_blank" rel="noopener"', DEVIS, s)
    for lab in ('Nous écrire sur WhatsApp', 'Nous contacter sur WhatsApp', 'WhatsApp +213 555 37 23 45</a>'):
        s = s.replace('>' + lab, '>' + ('Demander un devis</a>' if lab.endswith('</a>') else 'Demander un devis'))
    return s


def inject(s, extra_head=''):
    return replace_once(s, '</head>', extra_head + '<link rel="stylesheet" href="pss-integration.css">\n<script src="pss-integration.js"></script>\n</head>', '</head>')


# ---------------------------------------------------------------- plateforme crédit
c = open(os.path.join(SRC, 'credit.html'), encoding='utf-8').read()
c = common(c, 'crédit')
a = c.find('function pdfNew(sous){'); e = c.find('\n  return {doc, C, M, CW, st, t, wrap, h2, liste, meta, portee, foot};\n}', a)
if a < 0 or e < 0:
    raise SystemExit('fabrique pdfNew introuvable')
c = c[:a] + PDFNEW + c[e + len('\n  return {doc, C, M, CW, st, t, wrap, h2, liste, meta, portee, foot};\n}'):]
c = replace_once(c, '<script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js"></script>', '<script src="jspdf.umd.min.js"></script>', 'jsPDF')
c = c.replace("""onclick="window.open('https://wa.me/213555372345','_blank')">Nous contacter""", """onclick="top.location.href='../contact.html'">Demander un devis""")
c = inject(c)
open(os.path.join(OUT, 'credit.html'), 'w', encoding='utf-8').write(c)

# ---------------------------------------------------------------- plateforme investissement
v = open(os.path.join(SRC, 'investissement.html'), encoding='utf-8').read()
v = common(v, 'investissement')
v = v.replace("puis envoyez-la-nous sur WhatsApp : nous précisons", "puis demandez votre devis : nous précisons")
v = inject(v, '<script src="jspdf.umd.min.js"></script>\n')
open(os.path.join(OUT, 'investissement.html'), 'w', encoding='utf-8').write(v)

for f in ('credit.html', 'investissement.html'):
    s = open(os.path.join(OUT, f), encoding='utf-8').read()
    print('ok', f, 'liens WhatsApp restants dans les pages :', len(re.findall(r'href="https://wa\.me', s)), '| « Sur devis » :', s.count('Sur devis'))
