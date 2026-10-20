# Génère les pages intérieures du site PSS (python3 _build/build.py depuis la racine du dépôt).
# Le gabarit commun (en-tête, menu, carrousel du bas, avatar, pied de page) est ajouté par js/site.js.
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AR = '<svg viewBox="0 0 14 14"><path d="M3 11 11 3M5 3h6v6"/></svg>'
BK = '<svg viewBox="0 0 12 12"><path d="M8 2 4 6l4 4"/></svg>'
WA = 'https://wa.me/213555372345'
MAIL = 'men-ay_pro-managment@outlook.fr'
HORIZON = 'https://mszn5pm66j-arch.github.io/Cr-dit-22/Credittttttt.html#/niveau-1'


def lnk(label, href, ext=False):
    t = ' target="_blank" rel="noopener"' if ext or href.startswith('http') or href.startswith('mailto') else ''
    return f'<a class="lnk{" ext" if ext else ""}" href="{href}"{t}>{label} {AR}</a>'


def back(label, href):
    return f'<a class="back" href="{href}">{BK} {label}</a>'


def head(kick, title, lead=None, backto=None):
    kick = re.sub(r'^\d+(\.\d+)?\s*·\s*', '', kick)
    h = back(*backto) if backto else ''
    h += f'<div class="kick">{kick}</div><h1>{title}</h1>'
    if lead:
        h += f'<p class="lead">{lead}</p>'
    return h


def sec(sub, body='', links=(), first=False):
    sub = re.sub(r'^\d+\.\d+\s*/\s*', '', sub)
    ls = ''.join(lnk(*l) for l in links)
    return f'<section class="sec{" first" if first else ""}"><div class="sub">{sub}</div>{body}{"<div class=row>" + ls + "</div>" if ls else ""}</section>'


def p(t, dim=False):
    return f'<p{" class=dim" if dim else ""}>{t}</p>'


def steps(items):
    return '<ol class="steps">' + ''.join(f'<li><b>{n}</b><span><em>{t}</em>{d}</span></li>' for n, t, d in items) + '</ol>'


HUD = ('<div class="hud"><div class="st"><i></i>SYSTÈME ACTIF · ORAN / DZ01 / 04</div>'
       '<div class="nm">PRAETORIAN SENTINEL SMART</div><div class="tg">Concepteur de solutions &amp; Assistance au pilotage</div>'
       '<div class="ds">L\'ingénierie multidisciplinaire pour concevoir, structurer et exécuter vos projets en Algérie.</div></div>')

CREDIT = sec('Crédit Logement · Algérie Horizon',
             p('Le cabinet accompagne les particuliers et la diaspora pour un logement ou un crédit en Algérie, depuis la France, le Canada/Québec, l\'Espagne, l\'Allemagne et la Belgique.') +
             steps([('01', 'Gratuit', 'Évaluation de la faisabilité réglementaire, avec une fiche de synthèse et la liste des banques ouvertes aux non-résidents.'),
                    ('02', 'Diagnostic', 'Consultation en visioconférence et rapport écrit : documents à réunir et plan d\'action personnalisé.'),
                    ('03', 'Pré-dépôt', 'Préparation d\'un dossier complet (pièces, revenus, apostilles et traductions) selon votre situation.'),
                    ('04', 'Banque', 'Dépôt du dossier, directement ou par procuration, jusqu\'à un accord de principe écrit. La décision revient à la banque.')]),
             [('Accéder à Crédit Logement', HORIZON, True)])


# ---- page « Le cabinet » : domaines, approche, engagement ----
def ico(path):
    return f'<svg class="dico" viewBox="0 0 24 24">{path}</svg>'

DOMAINES = [
    ('Stratégie &amp; développement', 'Création, croissance et relance d\'activités.', 'diagnostic.html', '<path d="M3 17l6-6 4 4 7-8"/><path d="M14 7h6v6"/>'),
    ('Investissement &amp; ingénierie financière', 'Structuration des projets, montages et préparation des dossiers de financement.', 'division-4.html', '<path d="M4 20h16M6 20v-6h3v6M11 20V9h3v11M16 20V5h3v15"/>'),
    ('Structuration &amp; opérations internationales', 'Démarches administratives, coordination des besoins juridiques, implantations et commerce extérieur.', 'division-2.html', '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3.2 3 14.8 0 18M12 3c-3 3.2-3 14.8 0 18"/>'),
    ('Architecture &amp; maîtrise de projet', 'Conception d\'espaces, maquettes, diagnostics et organisation de la réalisation.', 'division-3.html', '<path d="M4 21 12 3l8 18M7.6 13h8.8M12 3v3"/>'),
    ('Veille &amp; systèmes IA', 'Intelligence artificielle (IA) : dispositifs de veille métier, organisation documentaire et automatisation des circuits de travail.', 'division-1.html', '<rect x="7" y="7" width="10" height="10" rx="1.5"/><path d="M10 3v4M14 3v4M10 17v4M14 17v4M3 10h4M3 14h4M17 10h4M17 14h4"/>'),
]
CAB_DOMAINES = ('<section class="sec first"><div class="sub">Nos domaines d\'intervention</div><div class="dgrid">' +
                ''.join(f'<a class="dcard" href="{h}">{ico(i)}<span><b>{t}</b><i>{d}</i></span>{AR}</a>' for t, d, h, i in DOMAINES) +
                '</div></section>')
CAB_APPROCHE = ('<section class="sec"><div class="sub">Notre approche</div>' +
                p('Relier la connaissance des métiers, la vision stratégique et la conception opérationnelle.') +
                '<div class="cadre"><div class="ct">Chaque mission s\'inscrit dans un cadre défini</div>'
                '<div class="c4"><span>Objectifs</span><span>Livrables</span><span>Responsabilités</span><span>Compétences à mobiliser</span></div></div>'
                '<div class="callout">' + ico('<rect x="7" y="7" width="10" height="10" rx="1.5"/><path d="M10 3v4M14 3v4M10 17v4M14 17v4M3 10h4M3 14h4M17 10h4M17 14h4"/>') +
                '<p>L\'intelligence artificielle s\'intègre à cette démarche comme un outil de travail et un levier de conception, au service des besoins réels du projet.</p></div></section>')
CAB_ENGAGEMENT = ('<section class="sec"><div class="sub">Notre engagement</div><ol class="flow">'
                  '<li><b>Concevoir</b><span>Donner une direction claire.</span></li>'
                  '<li><b>Structurer</b><span>Construire une réponse adaptée.</span></li>'
                  '<li><b>Piloter</b><span>Préparer les conditions de sa mise en œuvre.</span></li></ol></section>')

DIAG_CONTACT = [('Commencer par un diagnostic', 'diagnostic.html'), ('Parlons de votre projet', 'contact.html')]

PAGES = {
    'cabinet': ('cabinet', 'Le cabinet · Qui sommes-nous ?', 'Praetorian Sentinel Smart (PSS) est un cabinet de conseil stratégique et d\'ingénierie de projets, en Algérie et à l\'international.',
                head('Le cabinet', 'Qui sommes-nous ?', 'Praetorian Sentinel Smart (PSS) est un cabinet de conseil stratégique et d\'ingénierie de projets, au service des particuliers, des entrepreneurs, des investisseurs et des organisations, en Algérie et à l\'international.') +
                '<p class="lead">Nous concevons des solutions, structurons les moyens et organisons les interventions nécessaires pour faire avancer les projets et développer les activités.</p>' +
                CAB_DOMAINES + CAB_APPROCHE + CAB_ENGAGEMENT +
                sec('Pour aller plus loin', '', [('Notre méthode', 'methode.html'), ('Nos références', 'references.html'), ('Notre conformité', 'notreconformite.html'), ('Nous rejoindre', 'carrieres.html')]) +
                sec('Votre projet', p('Le plus simple est de commencer par un diagnostic : nous faisons le point avec vous et définissons la première étape.'), DIAG_CONTACT)),

    'methode': ('cabinet', 'Notre méthode · De votre projet à sa réalisation', 'Diagnostic, conseil et pilotage opérationnel en Algérie.',
                head('2.1 · Notre méthode', 'De votre projet à sa réalisation', 'Le cabinet propose un diagnostic, du conseil et un pilotage opérationnel en Algérie.', ('Le cabinet', 'cabinet.html')) +
                sec('Les trois étapes', steps([('01', 'Diagnostic', 'Faire le point sur votre situation et vos objectifs.'),
                                               ('02', 'Conseil', 'Définir les démarches et les priorités du projet.'),
                                               ('03', 'Pilotage', 'Accompagner la mise en œuvre du projet.')]),
                    [('Commencer par un diagnostic', 'diagnostic.html')], first=True)),

    'references': ('avis', 'Nos références professionnelles', 'Les références et expériences professionnelles du cabinet PSS.',
                   head('6.1 · Références professionnelles', 'Nos références professionnelles', 'Les références et expériences professionnelles du cabinet PSS.', ('Avis clients', 'avis.html')) +
                   sec('Références professionnelles', p('Les références détaillées seront présentées ici avec l\'accord des personnes concernées.'),
                       [('Échanger avec le cabinet', 'contact.html'), ('Laissez-nous votre avis', 'donner-mon-avis.html')], first=True)),

    'notreconformite': ('cabinet', 'Notre conformité', 'Engagement réglementaire, données et intelligence artificielle.',
                        head('2.3 · Notre conformité', 'Notre conformité', 'Engagement réglementaire, données et intelligence artificielle.', ('Le cabinet', 'cabinet.html')) +
                        sec('Réglementaire', p('Praetorian Sentinel Smart est un cabinet privé de droit algérien, basé à Oran, non rattaché à une institution publique.') +
                            p('Les autorisations et décisions relèvent des organismes compétents ; l\'accord de financement relève de la banque.'), first=True) +
                        sec('Données et intelligence artificielle (IA)', p('Les réponses au test d\'orientation et au parcours d\'avis sont conservées sur votre appareil.') +
                            p('Les photos ne sont ni envoyées ni conservées par le site.') +
                            p('L\'agent AIT (Artificial Intelligence Talk) n\'est pas encore relié à un service d\'intelligence artificielle : vous poursuivez l\'échange sur WhatsApp.'),
                            [('Politique de confidentialité', 'confidentialite.html')])),

    'divisions': ('segments', 'Nos segments · Quatre pôles d\'excellence', 'Des expertises combinées pour piloter un projet de bout en bout en Algérie.',
                  head('03 · Nos segments', 'Quatre pôles d\'excellence', 'Des expertises combinées pour piloter un projet de bout en bout en Algérie.') +
                  sec('3.1 / Réglementaire &amp; investissement', p('Cadre légal &amp; autorisations.'), [('Découvrir ce pôle', 'division-2.html'), ('Algérie Horizon · logement &amp; crédit diaspora', HORIZON, True)], first=True) +
                  sec('3.2 / Maîtrise d\'ouvrage', p('Pilotage opérationnel.'), [('Découvrir ce pôle', 'division-3.html')]) +
                  sec('3.3 / Ingénierie financière', p('Montages &amp; banques.'), [('Découvrir ce pôle', 'division-4.html'), ('Algérie Horizon · logement &amp; crédit diaspora', HORIZON, True)]) +
                  sec('3.4 / Architecture intelligente augmentée', p('Assistants &amp; automatisation.'), [('Découvrir ce pôle', 'division-1.html')])),

    'division-2': ('segments', 'Réglementaire & investissement', 'Foncier, autorisations et montages juridiques pour votre projet en Algérie.',
                   head('3.1 · Réglementaire', 'Réglementaire &amp; investissement', 'Foncier, autorisations et montages juridiques pour votre projet en Algérie.', ('Nos segments', 'divisions.html')) +
                   sec('Cadre légal &amp; autorisations', p('Foncier, autorisations et montages juridiques pour votre projet en Algérie.'), DIAG_CONTACT, first=True) + CREDIT),

    'division-3': ('segments', 'Maîtrise d\'ouvrage', 'Un accompagnement du cahier des charges à la réception des travaux.',
                   head('3.2 · Chantier', 'Maîtrise d\'ouvrage', 'Un accompagnement du cahier des charges à la réception des travaux.', ('Nos segments', 'divisions.html')) +
                   sec('Pilotage opérationnel', p('Un accompagnement du cahier des charges à la réception des travaux.'), DIAG_CONTACT, first=True) + HUD),

    'division-4': ('segments', 'Ingénierie financière', 'Structuration de votre société, montages financiers et préparation des échanges avec les banques.',
                   head('3.3 · Finance', 'Ingénierie financière', 'Structuration de votre société, montages financiers et préparation des échanges avec les banques.', ('Nos segments', 'divisions.html')) +
                   sec('Montages &amp; banques', p('Structuration de votre société, montages financiers et préparation des échanges avec les banques.'), DIAG_CONTACT, first=True) + CREDIT),

    'division-1': ('segments', 'Architecture intelligente augmentée', 'Des assistants et des automatisations adaptés à votre activité.',
                   head('3.4 · IA augmentée', 'Architecture intelligente augmentée', 'Des assistants et des automatisations adaptés à votre activité.', ('Nos segments', 'divisions.html')) +
                   sec('Assistants &amp; automatisation', p('Des assistants et des automatisations adaptés à votre activité.'), DIAG_CONTACT, first=True)),

    'academie': ('academie', 'Académie PSS · Apprendre et progresser', 'Formations et accompagnement métier avec Praetorian Sentinel Smart.',
                 head('04 · Académie PSS', 'Apprendre et progresser', 'Des formations et un accompagnement métier.') +
                 sec('Formation', p('Formations et accompagnement métier.'), [('Parlons de vos besoins', 'contact.html')], first=True) +
                 sec('Veille', p('Suivi des évolutions de votre métier.'), [('Parlons de vos besoins', 'contact.html')]) +
                 sec('Mise en pratique', p('Application des connaissances à votre projet.'), [('Parlons de vos besoins', 'contact.html')]) + HUD),

    'toutes-les-offres': ('offres', 'Nos offres · Un accompagnement adapté', 'Diagnostic, conseil et pilotage.',
                          head('05 · Nos offres', 'Un accompagnement adapté', 'Diagnostic, conseil et pilotage.') +
                          sec('5.1 / Diagnostic', p('Clarifier le besoin et choisir la première étape.'), [('Demander un diagnostic', 'diagnostic.html')], first=True) +
                          sec('5.2 / Formules d\'accompagnement', p('Deux volets : Conseil et Pilotage.'), [('Parlons de votre projet', 'contact.html')]) +
                          sec('Les trois étapes', steps([('01', 'Diagnostic', 'Clarifier le besoin.'), ('02', 'Conseil', 'Définir les priorités.'), ('03', 'Pilotage', 'Accompagner la réalisation.')]),
                              [('Commencer', 'diagnostic.html')])),

    'diagnostic': ('offres', 'Diagnostic · Faire le point sur votre projet', 'Clarifiez vos besoins et votre première étape avec le cabinet PSS.',
                   head('5.1 · Diagnostic', 'Faire le point sur votre projet', 'Clarifiez vos besoins et votre première étape avec le cabinet PSS.', ('Nos offres', 'toutes-les-offres.html')) +
                   sec('Votre première étape', p('Échangeons sur votre situation, vos objectifs et les démarches à préparer.'), [('Demander un diagnostic', 'contact.html')], first=True)),

    'contact': ('contact', 'Contactez-nous · Parlons de votre projet', 'Écrivez au cabinet PSS par WhatsApp, par e-mail ou parlez à notre agent.',
                head('07 · Contactez-nous', 'Parlons de votre projet', 'Écrivez-nous par WhatsApp, par e-mail, ou parlez à notre agent.') +
                sec('WhatsApp Business', p('+213 555 37 23 45'), [('Écrire sur WhatsApp', WA + '?text=' + 'Bonjour%20Praetorian%20Sentinel%20Smart%2C%20')], first=True) +
                sec('E-mail', p(MAIL), [('Envoyer un e-mail', 'mailto:' + MAIL)]) +
                sec('Parler à notre agent', p('AIT (Artificial Intelligence Talk) vous oriente vers la bonne première étape.'), [('Parler à notre agent', 'index.html#agent')]) +
                sec('Questions fréquentes', '', [('Questions fréquentes', 'faq.html')])),

    'espace': ('accueil', 'Espace client', 'Espace client du cabinet Praetorian Sentinel Smart.',
               head('Espace client', 'Votre espace client', 'Aucun compte n\'est nécessaire sur ce site. Votre consultant fait le point avec vous sur votre dossier.') +
               sec('Base documentaire', p('Les ressources utiles à votre projet.'), [('Base documentaire', 'documentation.html')], first=True) +
               sec('Votre consultant', p('Contactez votre consultant pour faire le point sur votre dossier.'), [('Contacter le cabinet', 'contact.html')])),

    'documentation': ('accueil', 'Base documentaire · Les ressources de votre projet', 'Documentation et accompagnement pour les projets en Algérie.',
                      head('Base documentaire', 'Les ressources de votre projet', 'Documentation et accompagnement pour vos projets en Algérie.', ('Espace client', 'espace.html')) +
                      sec('Base documentaire', p('Les ressources seront proposées ici. Écrivez au cabinet pour obtenir les documents utiles à votre projet.'), [('Demander une ressource', 'contact.html')], first=True)),

    'mentions': ('contact', 'Mentions légales', 'Identité et coordonnées du cabinet Praetorian Sentinel Smart à Oran.',
                 head('Informations légales', 'Mentions légales', 'Identité et coordonnées du cabinet Praetorian Sentinel Smart à Oran.') +
                 sec('Identité', p('Praetorian Sentinel Smart, SARL de droit algérien, Oran.') + p('Cabinet privé, non affilié à une institution publique.'), first=True) +
                 sec('Contact', p('WhatsApp Business : +213 555 37 23 45') + p('E-mail : ' + MAIL)) +
                 sec('Informations complémentaires', p('Les informations légales complémentaires seront ajoutées après validation du cabinet.', True))),

    'confidentialite': ('contact', 'Politique de confidentialité', 'Vos données restent sur votre appareil.',
                        head('Informations légales', 'Politique de confidentialité', 'Comment le site traite vos informations.') +
                        sec('Vos données restent sur votre appareil', p('Les réponses à votre avis sont enregistrées uniquement dans le navigateur de votre appareil.') +
                            p('Le test d\'orientation n\'envoie aucune réponse à un serveur.') +
                            p('La photo reste temporairement en mémoire : elle n\'est pas téléversée et n\'est pas conservée après la fermeture du parcours.'), first=True) +
                        sec('Un partage choisi', p('Le téléchargement de la fiche reste local. En cas de partage via Facebook, WhatsApp ou e-mail, les informations sont traitées par ce service selon ses propres conditions.'),
                            [('Poser une question sur la confidentialité', 'contact.html')])),

    'conditions': ('contact', 'Conditions d\'utilisation', 'Utilisation du site PSS et partage volontaire de votre fiche d\'expérience.',
                   head('Conditions', 'Conditions d\'utilisation', 'Utilisation du site PSS et partage volontaire de votre fiche d\'expérience.') +
                   sec('Utilisation du site', p('Le site présente le cabinet et permet de préparer une fiche de retour d\'expérience sans créer de compte.') +
                       p('Vous choisissez les informations et la photo à partager. Vérifiez leur contenu et masquez les données confidentielles avant publication.') +
                       p('Aucune publication n\'est automatique : le consentement donné dans le parcours ne remplace pas la confirmation dans l\'application de partage.') +
                       p('Les modalités d\'un accompagnement sont convenues directement avec le cabinet.'),
                       [('Contacter le cabinet', 'contact.html')], first=True)),
}

FAQ = [('Où intervenez-vous ?', 'Le cabinet accompagne les projets liés à l\'Algérie, depuis l\'Algérie et depuis l\'étranger : France, Espagne, Allemagne, Belgique, Québec.'),
       ('Faut-il créer un compte ?', 'Non. Le parcours d\'avis fonctionne sans inscription.'),
       ('Ma photo est-elle envoyée au cabinet ?', 'Non. La photo reste sur votre appareil et est intégrée à votre fiche en image (PNG).'),
       ('Comment partager mon avis ?', 'Vous préparez votre fiche, puis vous la téléchargez ou choisissez le partage proposé par votre téléphone. Vous confirmez vous-même la publication.'),
       ('Comment accéder à Algérie Horizon ?', 'Le lien logement et crédit diaspora se trouve dans les pôles Réglementaire &amp; investissement et Ingénierie financière.')]

PAGES['faq'] = ('contact', 'Questions fréquentes · Vos questions, nos réponses', 'Questions fréquentes sur le cabinet Praetorian Sentinel Smart.',
                head('Questions fréquentes', 'Vos questions, nos réponses', None, ('Contactez-nous', 'contact.html')) +
                '<section class="sec first">' + ''.join(f'<div class="qa"><button type="button">{q}<i>+</i></button><div class="ans"><p>{a}</p></div></div>' for q, a in FAQ) +
                '<div class="row">' + lnk('Poser une autre question', 'contact.html') + '</div></section>')

PLAN_EXTRA = [('·', 'Espace client', 'espace.html', [('Base documentaire', 'documentation.html')])]
SECS = [('01', 'Accueil', 'index.html', [('Pour qui ?', 'index.html#pour-qui'), ('Nos solutions', 'index.html#services'), ('AIT', 'index.html#agent')]),
        ('02', 'Le cabinet', 'cabinet.html', [('Notre méthode', 'methode.html'), ('Nos références', 'references.html'), ('Notre conformité', 'notreconformite.html'), ('Nous rejoindre', 'carrieres.html')]),
        ('03', 'Nos segments', 'divisions.html', [('3.1 Réglementaire &amp; investissement', 'division-2.html'), ('3.2 Maîtrise d\'ouvrage', 'division-3.html'), ('3.3 Ingénierie financière', 'division-4.html'), ('3.4 Architecture intelligente augmentée', 'division-1.html')]),
        ('04', 'Académie PSS', 'academie.html', []),
        ('05', 'Nos offres', 'toutes-les-offres.html', [('Diagnostic', 'diagnostic.html'), ('Toutes les offres', 'toutes-les-offres.html')]),
        ('06', 'Avis clients', 'avis.html', [('6.1 Références professionnelles', 'references.html'), ('6.2 Donner votre avis', 'donner-mon-avis.html')]),
        ('07', 'Contactez-nous', 'contact.html', [('Contact', 'contact.html'), ('Questions fréquentes', 'faq.html')])]
LEG = [('Mentions légales', 'mentions.html'), ('Confidentialité', 'confidentialite.html'), ('Conditions', 'conditions.html'), ('Conformité', 'notreconformite.html'), ('FAQ', 'faq.html'), ('Plan du site', 'plan.html')]
tree = '<ul class="tree">' + ''.join(
    f'<li><a href="{h}">{t}</a>' + ('<ul>' + ''.join(f'<li><a href="{x}">{re.sub(chr(94) + r"\d+\.\d+ ", "", y)}</a></li>' for y, x in s) + '</ul>' if s else '') + '</li>'
    for n, t, h, s in SECS + PLAN_EXTRA) + '</ul>'
PAGES['plan'] = ('accueil', 'Plan du site', 'Toutes les pages du site Praetorian Sentinel Smart.',
                 head('Plan du site', 'Toutes les pages') + '<section class="sec first"><div class="sub">Rubriques</div>' + tree + '</section>' +
                 '<section class="sec"><div class="sub">Informations légales</div><ul class="tree">' + ''.join(f'<li><a href="{h}">{t}</a></li>' for t, h in LEG) + '</ul></section>')

TPL = '''<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="theme-color" content="#02060b">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{title} · Praetorian Sentinel Smart</title>
<meta name="description" content="{desc}">
<link rel="icon" href="assets/emblem-cadre.png">
<link rel="stylesheet" href="css/style.css">
</head>
<body data-page="{name}" data-sec="{sec}">
<div class="stage">
<main class="page">
{content}
</main>
</div>
<script src="js/site.js"></script>
{extra}
</body>
</html>
'''

FAQ_JS = '''<script>
document.querySelectorAll('.qa button').forEach(function(b){b.addEventListener('click',function(){var q=b.parentNode,a=q.querySelector('.ans'),on=!q.classList.contains('on');q.classList.toggle('on',on);a.style.maxHeight=on?a.scrollHeight+'px':'0';});});
</script>'''

for name, (s, title, desc, content) in PAGES.items():
    html = TPL.format(title=title.replace('&amp;', '&'), desc=desc.replace('"', '&quot;'), name=name, sec=s, content=content,
                      extra=FAQ_JS if name == 'faq' else '')
    open(os.path.join(ROOT, name + '.html'), 'w', encoding='utf-8').write(html)
    print('ok', name)
