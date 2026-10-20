# Génère les pages intérieures du site PSS (python3 _build/build.py depuis la racine du dépôt).
# Le gabarit commun (en-tête, menu, carrousel du bas, avatar, pied de page) est ajouté par js/site.js.
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AR = '<svg viewBox="0 0 14 14"><path d="M3 11 11 3M5 3h6v6"/></svg>'
BK = '<svg viewBox="0 0 12 12"><path d="M8 2 4 6l4 4"/></svg>'
WA = 'https://wa.me/213555372345'
MAIL = 'men-ay_pro-managment@outlook.fr'
HORIZON = 'credit.html?r=niveau-1'   # plateforme crédit intégrée au site


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
             [('Accéder à Crédit Logement', HORIZON)])


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

    'divisions': ('cabinet', 'Nos domaines d\'expertise · Quatre pôles d\'excellence', 'Des expertises combinées pour piloter un projet de bout en bout en Algérie.',
                  head('Le cabinet · Nos domaines d\'expertise', 'Quatre pôles d\'excellence', 'Des expertises combinées pour piloter un projet de bout en bout en Algérie.', ('Le cabinet', 'cabinet.html')) +
                  sec('3.1 / Réglementaire &amp; investissement', p('Cadre légal &amp; autorisations.'), [('Découvrir ce pôle', 'division-2.html'), ('Crédit logement depuis l\'étranger', HORIZON)], first=True) +
                  sec('3.2 / Maîtrise d\'ouvrage', p('Pilotage opérationnel.'), [('Découvrir ce pôle', 'division-3.html')]) +
                  sec('3.3 / Ingénierie financière', p('Montages &amp; banques.'), [('Découvrir ce pôle', 'division-4.html'), ('Crédit logement depuis l\'étranger', HORIZON)]) +
                  sec('3.4 / Architecture intelligente augmentée', p('Assistants &amp; automatisation.'), [('Découvrir ce pôle', 'division-1.html')])),

    'division-2': ('cabinet', 'Réglementaire & investissement', 'Foncier, autorisations et montages juridiques pour votre projet en Algérie.',
                   head('3.1 · Réglementaire', 'Réglementaire &amp; investissement', 'Foncier, autorisations et montages juridiques pour votre projet en Algérie.', ('Nos domaines d\'expertise', 'divisions.html')) +
                   sec('Cadre légal &amp; autorisations', p('Foncier, autorisations et montages juridiques pour votre projet en Algérie.'), DIAG_CONTACT, first=True) + CREDIT),

    'division-3': ('cabinet', 'Maîtrise d\'ouvrage', 'Un accompagnement du cahier des charges à la réception des travaux.',
                   head('3.2 · Chantier', 'Maîtrise d\'ouvrage', 'Un accompagnement du cahier des charges à la réception des travaux.', ('Nos domaines d\'expertise', 'divisions.html')) +
                   sec('Pilotage opérationnel', p('Un accompagnement du cahier des charges à la réception des travaux.'), DIAG_CONTACT, first=True) + HUD),

    'division-4': ('cabinet', 'Ingénierie financière', 'Structuration de votre société, montages financiers et préparation des échanges avec les banques.',
                   head('3.3 · Finance', 'Ingénierie financière', 'Structuration de votre société, montages financiers et préparation des échanges avec les banques.', ('Nos domaines d\'expertise', 'divisions.html')) +
                   sec('Montages &amp; banques', p('Structuration de votre société, montages financiers et préparation des échanges avec les banques.'), DIAG_CONTACT, first=True) + CREDIT),

    'division-1': ('cabinet', 'Architecture intelligente augmentée', 'Des assistants et des automatisations adaptés à votre activité.',
                   head('3.4 · IA augmentée', 'Architecture intelligente augmentée', 'Des assistants et des automatisations adaptés à votre activité.', ('Nos domaines d\'expertise', 'divisions.html')) +
                   sec('Assistants &amp; automatisation', p('Des assistants et des automatisations adaptés à votre activité.'), DIAG_CONTACT, first=True)),

    'academie': ('academie', 'Académie PSS · Apprendre et progresser', 'Formations et accompagnement métier avec Praetorian Sentinel Smart.',
                 head('04 · Académie PSS', 'Apprendre et progresser', 'Des formations et un accompagnement métier.') +
                 sec('Formation', p('Formations et accompagnement métier.'), [('Parlons de vos besoins', 'contact.html')], first=True) +
                 sec('Veille', p('Suivi des évolutions de votre métier.'), [('Parlons de vos besoins', 'contact.html')]) +
                 sec('Mise en pratique', p('Application des connaissances à votre projet.'), [('Parlons de vos besoins', 'contact.html')]) + HUD),

    'toutes-les-offres': ('parcours', 'Nos offres · Un accompagnement adapté', 'Diagnostic, conseil et pilotage.',
                          head('Votre parcours · Nos offres', 'Un accompagnement adapté', 'Diagnostic, conseil et pilotage.', ('Votre parcours', 'parcours.html')) +
                          sec('5.1 / Diagnostic', p('Clarifier le besoin et choisir la première étape.'), [('Demander un diagnostic', 'diagnostic.html')], first=True) +
                          sec('5.2 / Formules d\'accompagnement', p('Deux volets : Conseil et Pilotage.'), [('Parlons de votre projet', 'contact.html')]) +
                          sec('Les trois étapes', steps([('01', 'Diagnostic', 'Clarifier le besoin.'), ('02', 'Conseil', 'Définir les priorités.'), ('03', 'Pilotage', 'Accompagner la réalisation.')]),
                              [('Commencer', 'diagnostic.html')])),

    'diagnostic': ('parcours', 'Diagnostic · Faire le point sur votre projet', 'Clarifiez vos besoins et votre première étape avec le cabinet PSS.',
                   head('Votre parcours · Diagnostic', 'Faire le point sur votre projet', 'Clarifiez vos besoins et votre première étape avec le cabinet PSS.', ('Votre parcours', 'parcours.html')) +
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


# ---- Votre parcours · À qui nous adressons-nous ? ----
INV = 'diagnostic-initial.html'   # plateforme investissement intégrée au site


def card(href, icon, title, text):
    return f'<a class="dcard" href="{href}">{ico(icon)}<span><b>{title}</b><i>{text}</i></span>{AR}</a>'


I_HOME = '<path d="M3 11l9-7 9 7"/><path d="M5 10v10h14V10M10 20v-5h4v5"/>'
I_BARS = '<path d="M4 20h16M6 20v-6h3v6M11 20V9h3v11M16 20V5h3v15"/>'
I_SHIELD = '<path d="M12 2.5l7 3v5.5c0 4.4-3 7.6-7 9-4-1.4-7-4.6-7-9V5.5z"/><path d="M8.8 11.5l2.2 2.2 4.2-4.4"/>'
I_CHIP = '<rect x="7" y="7" width="10" height="10" rx="1.5"/><path d="M10 3v4M14 3v4M10 17v4M14 17v4M3 10h4M3 14h4M17 10h4M17 14h4"/>'
I_DOC = '<path d="M6 3h9l4 4v14H6z"/><path d="M15 3v4h4M9 12h7M9 16h5"/>'
I_EYE = '<circle cx="11" cy="11" r="6.5"/><path d="M16 16l5 5M11 7.5v3.5l2.2 1.4"/>'

PARCOURS = (head('Votre parcours', 'À qui nous adressons-nous ?', 'Quatre profils, un livrable concret pour chacun. Repérez le vôtre, ou laissez le filtre en bas de page vous guider.') +
            '<div class="dgrid" style="margin-top:18px">' +
            card('#particuliers', I_HOME, 'Particuliers de la diaspora', 'Logement et crédit en Algérie depuis l\'étranger') +
            card('#investisseurs', I_BARS, 'Investisseurs', 'Fonds disponibles ou projet identifié') +
            card('#porteurs', I_SHIELD, 'Porteurs de projet', 'Pré-lancement ou activité en développement') +
            card('#professionnels', I_CHIP, 'Professionnels et entreprises', 'L\'IA adaptée à votre métier') + '</div>' +
            '<section class="sec" id="particuliers"><div class="sub">Particuliers · crédit depuis l\'étranger</div>' +
            p('Vous vivez en France, en Espagne, en Allemagne, en Belgique ou au Québec et vous voulez acheter un logement en Algérie avec un crédit bancaire.') +
            p('La plateforme crédit vous accompagne en quatre niveaux :', True) +
            steps([('01', 'Gratuit', 'Faisabilité réglementaire, fiche de synthèse et liste des banques ouvertes aux non-résidents.'),
                   ('02', 'Diagnostic', 'Consultation en visioconférence et rapport écrit : documents à réunir, plan d\'action.'),
                   ('03', 'Pré-dépôt', 'Dossier complet selon votre pays : pièces, revenus, apostilles, traductions.'),
                   ('04', 'Banque', 'Dépôt du dossier jusqu\'à l\'accord de principe écrit. La décision revient à la banque.')]) +
            '<div class="row">' + lnk('Commencer gratuitement · niveau 1', HORIZON) + '</div></section>' +
            '<section class="sec" id="investisseurs"><div class="sub">Investisseurs · diagnostic initial</div>' +
            p('Vous disposez de fonds sans projet arrêté, ou vous avez un projet identifié et voulez savoir comment le réaliser en Algérie.') +
            '<div class="cadre"><div class="ct">Le diagnostic initial couvre</div><div class="c4"><span>Cadre légal et autorisations</span><span>Institutions : AAPI, banques, CNRC, impôts, douanes</span><span>Structure de la société</span><span>Pistes de financement</span></div></div>' +
            p('AAPI : Agence algérienne de promotion de l\'investissement. CNRC : Centre national du registre du commerce.', True) +
            '<div class="row">' + lnk('Obtenir ma fiche de diagnostic initial (PDF)', INV + '?profil=investNat') + '</div></section>' +
            '<section class="sec" id="porteurs"><div class="sub">Porteurs de projet · diagnostic de lancement</div>' +
            p('Vous préparez le lancement d\'une activité, ou votre activité existe et doit franchir une étape.') +
            steps([('01', 'Pré-lancement', 'Faisabilité, démarches légales avec lien direct vers l\'institution, budget et calendrier.'),
                   ('02', 'Développement', 'Points bloquants, organisation, financement de l\'étape suivante.')]) +
            '<div class="row">' + lnk('Obtenir mon diagnostic de lancement (PDF)', INV + '?profil=entrepreneur') + '</div></section>' +
            '<section class="sec" id="professionnels"><div class="sub">Professionnels et entreprises · IA métier</div>' +
            p('Vous voulez que l\'intelligence artificielle travaille pour votre métier : documenter, surveiller les évolutions, automatiser les tâches répétitives.') +
            '<div class="row">' + lnk('Découvrir IA métier', 'ia-metier.html') + '</div></section>' +
            '<section class="sec flt" id="filtre"><div class="sub">Pas sûr de votre profil ? · trouver mon offre en 3 étapes</div>' +
            '<div class="fld"><div class="lb">1 · Vous êtes</div><div class="chips" id="f1">' +
            ''.join(f'<button type="button" class="chip" data-v="{v}">{t}</button>' for v, t in [('particulier', 'Particulier'), ('investisseur', 'Investisseur'), ('porteur', 'Porteur de projet'), ('pro', 'Professionnel')]) + '</div></div>' +
            '<div class="fld"><div class="lb">2 · Où en êtes-vous ?</div><div class="chips" id="f2"></div></div>' +
            '<div class="fld"><div class="lb">3 · Que cherchez-vous ?</div><div class="chips" id="f3"></div></div>' +
            '<div class="hint" id="fh">Commencez par votre profil : les choix suivants s\'adaptent.</div>' +
            '<div class="res" id="fr"></div></section>' +
            '<section class="sec" id="devis"><div class="sub">Ensuite · accompagnement sur devis</div>' +
            steps([('01', 'Orientation gratuite', 'Avec AIT (Artificial Intelligence Talk), notre agent conversationnel.'),
                   ('02', 'Diagnostic', 'Le livrable de votre profil.'),
                   ('03', 'Accompagnement sur devis', 'Cahier des charges, consultation des intervenants, pilotage jusqu\'à la réalisation.'),
                   ('04', 'Suivi après réalisation', 'Selon votre projet.')]) + '</section>')

PARCOURS_JS = """<script>
(function(){
var S2={particulier:['Je vis à l\\u2019étranger','Je vis en Algérie'],investisseur:['Fonds disponibles, sans projet arrêté','Projet identifié'],porteur:['Pré-lancement','Activité en développement'],pro:['Professionnel indépendant','Entreprise en développement']};
var S3={particulier:['Acheter un logement avec un crédit','Démarches et autorisations'],investisseur:['Connaître le cadre légal','Structurer la société','Préparer le financement'],porteur:['Valider la faisabilité','Monter le dossier','Piloter le projet'],pro:['Documenter','Surveiller les évolutions','Automatiser']};
var PRIO=['documenter','surveiller','automatiser'];
var f1=document.getElementById('f1'),f2=document.getElementById('f2'),f3=document.getElementById('f3'),fh=document.getElementById('fh'),fr=document.getElementById('fr'),st={p:null,a:null,b:null};
function chips(el,list,cur){el.innerHTML=list.map(function(t,i){return '<button type="button" class="chip'+(i===cur?' on':'')+'" data-i="'+i+'">'+t+'</button>';}).join('');}
function L(t,h,x){return '<a class="lnk" href="'+h+'"'+(x?' target="_blank" rel="noopener"':'')+'>'+t+' '+PSS.ARROW+'</a>';}
function result(){var p=st.p,a=st.a,b=st.b,r;
  if(p==='particulier'){r=(a===0)?['Plateforme crédit · 5 pays','Depuis la France, l\\u2019Espagne, l\\u2019Allemagne, la Belgique ou le Québec : quatre niveaux, le premier gratuit, jusqu\\u2019à l\\u2019accord de principe de la banque.',L(b===0?'Commencer gratuitement · niveau 1':'Ouvrir la plateforme crédit',b===0?'credit.html?r=niveau-1':'credit.html')+L('Voir les quatre niveaux','#particuliers')]
    :['Diagnostic gratuit (PDF)','Notre plateforme réglementaire identifie les démarches, les institutions concernées et les documents à préparer, puis génère votre rapport en PDF.',L('Obtenir mon diagnostic gratuit (PDF)','diagnostic-initial.html')];}
  else if(p==='investisseur')r=['Diagnostic initial investisseur (PDF)','Cadre légal, institutions, structure de la société et financement : votre rapport gratuit, généré par notre plateforme investissement.',L('Obtenir ma fiche de diagnostic initial (PDF)','diagnostic-initial.html?profil='+(a===0?'holding':'investNat'))+L('Ce que couvre le diagnostic','#investisseurs')];
  else if(p==='porteur')r=['Diagnostic de lancement (PDF)',(a===0?'Faisabilité, démarches légales, budget et calendrier.':'Points bloquants, organisation et financement de l\\u2019étape suivante.')+' Gratuit, généré par notre plateforme ; il précède l\\u2019accompagnement sur devis.',L('Obtenir mon diagnostic de lancement (PDF)','diagnostic-initial.html?profil='+(a===0?'entrepreneur':'entrepriseDev'))+L('Voir l\\u2019accompagnement sur devis','#devis')];
  else r=['IA métier','Votre priorité : '+S3.pro[b].toLowerCase()+'. Le schéma de principe de votre dispositif se prépare sur la page IA métier.',L('Préparer mon schéma de principe','ia-metier.html#'+PRIO[b])];
  fr.innerHTML='<h3>'+r[0]+'</h3><p>'+r[1]+'</p><div class="row">'+r[2]+'</div>';fr.classList.remove('on');void fr.offsetWidth;fr.classList.add('on');fh.textContent='';}
function draw(){chips(f2,st.p?S2[st.p]:[],st.a);chips(f3,st.p&&st.a!==null?S3[st.p]:[],st.b);
  if(!st.p)fh.textContent='Commencez par votre profil : les choix suivants s\\u2019adaptent.';else if(st.a===null)fh.textContent='Où en êtes-vous ?';else if(st.b===null)fh.textContent='Que cherchez-vous ?';
  if(st.b===null){fr.classList.remove('on');fr.innerHTML='';}else result();}
f1.addEventListener('click',function(e){var b=e.target.closest('.chip');if(!b)return;st={p:b.getAttribute('data-v'),a:null,b:null};f1.querySelectorAll('.chip').forEach(function(c){c.classList.toggle('on',c===b);});draw();});
f2.addEventListener('click',function(e){var b=e.target.closest('.chip');if(!b)return;st.a=+b.getAttribute('data-i');st.b=null;draw();});
f3.addEventListener('click',function(e){var b=e.target.closest('.chip');if(!b)return;st.b=+b.getAttribute('data-i');draw();});
draw();
})();
</script>"""

# ---- IA métier ----
IA = (head('IA métier', 'L\'intelligence artificielle, adaptée à votre métier', 'Un même socle, des options selon votre activité : documenter, surveiller les évolutions, automatiser.') +
      '<section class="sec first"><div class="sub">Ce que nous mettons en place</div><div class="dgrid">' +
      card('#filtre-ia" id="documenter" data-prio="0', I_DOC, 'Documentaire interactif', 'Votre base de documents interrogée en langage courant : modèles, textes, procédures.') +
      card('#filtre-ia" id="surveiller" data-prio="1', I_EYE, 'Veille métier', 'Un agent qui suit en continu les évolutions de votre secteur et vous signale ce qui change.') +
      card('#filtre-ia" id="automatiser" data-prio="2', I_CHIP, 'Assistants et automatisation', 'Les tâches répétitives de vos circuits de travail prises en charge.') + '</div></section>' +
      '<section class="sec"><div class="sub">Le socle commun</div>' +
      p('Toutes nos solutions reposent sur les mêmes fondations : un serveur et sa base de données, un agent qui actualise les informations en arrière-plan, un orchestrateur qui coordonne les agents, et une interface qui génère et régénère vos documents. Les options s\'ajoutent selon votre métier.') + '</section>' +
      '<section class="sec flt" id="filtre-ia"><div class="sub">Préparer mon schéma de principe</div>' +
      '<div class="fld"><div class="lb">1 · Votre profil</div><div class="chips" data-g="profil">' + ''.join(f'<button type="button" class="chip">{t}</button>' for t in ['Professionnel', 'Entreprise en développement', 'Investisseur']) + '</div></div>' +
      '<div class="fld"><div class="lb">2 · Votre métier</div><div class="chips" data-g="metier">' + ''.join(f'<button type="button" class="chip">{t}</button>' for t in ['Juridique', 'BTP et marchés', 'Commerce extérieur', 'Santé', 'Immobilier', 'Autre']) + '</div></div>' +
      '<div class="fld"><div class="lb">3 · Votre priorité</div><div class="chips" data-g="prio">' + ''.join(f'<button type="button" class="chip">{t}</button>' for t in ['Documenter', 'Surveiller', 'Automatiser']) + '</div></div>' +
      '<div class="hint" id="ih">Trois choix, puis votre schéma de principe se télécharge en PDF.</div>' +
      '<div class="res" id="ir"></div></section>')

IA_JS = """<script>
(function(){
var OPT=[['Documentaire interactif','agent conversationnel relié à votre base de documents'],['Veille métier','agent qui surveille les textes et les évolutions de votre secteur'],['Assistants et automatisation','agents qui prennent en charge vos tâches répétitives']];
var sel={profil:null,metier:null,prio:null},ih=document.getElementById('ih'),ir=document.getElementById('ir');
var groups=[].slice.call(document.querySelectorAll('#filtre-ia [data-g]'));
function txt(g){var c=document.querySelector('#filtre-ia [data-g="'+g+'"] .chip.on');return c?c.textContent:null;}
function update(){sel.profil=txt('profil');sel.metier=txt('metier');sel.prio=txt('prio');
  var miss=['profil','metier','prio'].filter(function(k){return !sel[k];});
  if(miss.length){ih.textContent=miss.length===3?'Trois choix, puis votre schéma de principe se télécharge en PDF.':'Encore '+miss.length+' choix.';ir.classList.remove('on');return;}
  ih.textContent='';var i=['Documenter','Surveiller','Automatiser'].indexOf(sel.prio);
  ir.innerHTML='<h3>Votre schéma de principe</h3><p>Socle commun + '+OPT[i][0].toLowerCase()+' ('+OPT[i][1]+'), pour le métier : '+sel.metier.toLowerCase()+'.</p><div class="row"><button type="button" class="lnk" id="ipdf">Télécharger mon schéma de principe (PDF) '+PSS.ARROW+'</button></div>';
  ir.classList.remove('on');void ir.offsetWidth;ir.classList.add('on');}
groups.forEach(function(g){g.addEventListener('click',function(e){var b=e.target.closest('.chip');if(!b)return;g.querySelectorAll('.chip').forEach(function(c){c.classList.toggle('on',c===b);});update();});});
function pick(i){var g=document.querySelector('#filtre-ia [data-g="prio"]');g.querySelectorAll('.chip').forEach(function(c,j){c.classList.toggle('on',j===i);});update();}
document.querySelectorAll('[data-prio]').forEach(function(a){a.addEventListener('click',function(){pick(+a.getAttribute('data-prio'));});});
var hm={documenter:0,surveiller:1,automatiser:2};if(location.hash.slice(1) in hm)pick(hm[location.hash.slice(1)]);
/* ---- schéma de principe : dessin dans la charte puis PDF d'une page ---- */
function img(src){return new Promise(function(r){var i=new Image();i.onload=function(){r(i);};i.onerror=function(){r(null);};i.src=src;});}
function wrap(g,t,x,y,w,lh){var ws=t.split(' '),l='';ws.forEach(function(m){var k=l?l+' '+m:m;if(g.measureText(k).width>w&&l){g.fillText(l,x,y);y+=lh;l=m;}else l=k;});if(l)g.fillText(l,x,y);return y+lh;}
function node(g,x,y,w,h,t1,t2,on){g.fillStyle=on?'rgba(57,195,255,.16)':'rgba(6,14,24,.9)';g.strokeStyle=on?'#39c3ff':'rgba(90,190,240,.45)';g.lineWidth=on?3:2;g.beginPath();g.rect(x,y,w,h);g.fill();g.stroke();
  g.fillStyle=on?'#eaf7fd':'#cfe0ea';g.font='500 23px PSS, sans-serif';g.textAlign='center';g.fillText(t1,x+w/2,y+h/2-(t2?6:-9));if(t2){g.fillStyle=on?'#8fe0ff':'#7f93a3';g.font='300 19px PSS, sans-serif';g.fillText(t2,x+w/2,y+h/2+26);}g.textAlign='left';}
function track(g,pts,on){g.strokeStyle=on?'#5fd4ff':'rgba(90,170,210,.5)';g.lineWidth=on?3:2;g.beginPath();pts.forEach(function(p,i){i?g.lineTo(p[0],p[1]):g.moveTo(p[0],p[1]);});g.stroke();
  [pts[0],pts[pts.length-1]].forEach(function(p){g.fillStyle='#02060b';g.beginPath();g.arc(p[0],p[1],7,0,6.283);g.fill();g.strokeStyle=on?'#8fe0ff':'rgba(120,200,240,.7)';g.lineWidth=2;g.stroke();});}
async function schema(){var W=1240,H=1754,c=document.createElement('canvas');c.width=W;c.height=H;var g=c.getContext('2d');
  var bg=await img('assets/fond-profond.jpg'),em=await img('assets/emblem-cadre.png'),wm=await img('assets/praetorian.png');
  g.fillStyle='#02060b';g.fillRect(0,0,W,H);if(bg){g.globalAlpha=.22;var s=Math.max(W/bg.width,H/bg.height);g.drawImage(bg,(W-bg.width*s)/2,(H-bg.height*s)/2,bg.width*s,bg.height*s);g.globalAlpha=1;}
  if(em)g.drawImage(em,70,60,146,138);if(wm)g.drawImage(wm,240,88,385,82);
  g.strokeStyle='rgba(90,170,210,.35)';g.lineWidth=2;g.beginPath();g.moveTo(70,230);g.lineTo(W-70,230);g.stroke();
  g.fillStyle='#5baacb';g.font='400 22px PSS, sans-serif';g.fillText('SCHÉMA DE PRINCIPE · IA MÉTIER',70,290);
  g.fillStyle='#f2f5f7';g.font='300 52px PSS, sans-serif';g.fillText(sel.metier,70,360);
  g.fillStyle='#a9b8c4';g.font='300 24px PSS, sans-serif';g.fillText('Profil : '+sel.profil+'  ·  Priorité : '+sel.prio,70,405);
  var i=['Documenter','Surveiller','Automatiser'].indexOf(sel.prio);
  /* socle */
  g.fillStyle='#5acef6';g.font='400 22px PSS, sans-serif';g.fillText('LE SOCLE COMMUN',70,490);
  g.strokeStyle='rgba(90,190,240,.25)';g.lineWidth=2;g.strokeRect(70,515,W-140,560);
  node(g,470,740,300,110,'Orchestrateur','coordonne les agents',true);
  node(g,120,560,300,110,'Serveur','et base de données');node(g,820,560,300,110,'Agent arrière-plan','actualisation');
  node(g,120,920,300,110,'Interface','génération, régénération');node(g,820,920,300,110,'API','échanges entre agents');
  track(g,[[420,615],[520,615],[560,655],[560,740]]);track(g,[[820,615],[720,615],[680,655],[680,740]]);
  track(g,[[420,975],[520,975],[560,935],[560,850]]);track(g,[[820,975],[720,975],[680,935],[680,850]]);
  /* options */
  g.fillStyle='#5acef6';g.font='400 22px PSS, sans-serif';g.fillText('LES OPTIONS POUR VOTRE MÉTIER',70,1150);
  for(var k=0;k<3;k++){var y=1180+k*120,on=k===i;node(g,70,y,W-140,96,'','',on);
    g.fillStyle=on?'#eaf7fd':'#7f93a3';g.font='500 27px PSS, sans-serif';g.fillText((on?'Retenue · ':'En option · ')+OPT[k][0],100,y+42);
    g.fillStyle=on?'#8fe0ff':'#5f7383';g.font='300 21px PSS, sans-serif';g.fillText(OPT[k][1],100,y+76);}
  track(g,[[620,1075],[620,1180]],true);
  g.fillStyle='#a9b8c4';g.font='300 21px PSS, sans-serif';wrap(g,'Document indicatif, établi à partir de vos réponses. Il est précisé lors du diagnostic, puis chiffré sur devis.',70,1580,W-140,30);
  g.fillStyle='#5a8fe0';g.font='500 22px PSS, sans-serif';g.fillText('WhatsApp Business',70,1665);g.fillStyle='#e6eef4';g.fillText('+213 555 37 23 45',90+g.measureText('WhatsApp Business').width,1665);
  g.fillStyle='#5a8fe0';g.fillText('Email',70,1700);g.fillStyle='#e6eef4';g.fillText(PSS.MAIL,90+g.measureText('Email').width,1700);
  return c;}
function pdf(jpeg,w,h){var b=atob(jpeg.split(',')[1]),im=new Uint8Array(b.length);for(var i=0;i<b.length;i++)im[i]=b.charCodeAt(i);
  var enc=new TextEncoder(),parts=[],off=[],len=0;function add(x){if(typeof x==='string')x=enc.encode(x);parts.push(x);len+=x.length;}
  var PW=595.28,PH=841.89;add('%PDF-1.4\\n');
  off[1]=len;add('1 0 obj<</Type/Catalog/Pages 2 0 R>>endobj\\n');off[2]=len;add('2 0 obj<</Type/Pages/Kids[3 0 R]/Count 1>>endobj\\n');
  off[3]=len;add('3 0 obj<</Type/Page/Parent 2 0 R/MediaBox[0 0 '+PW+' '+PH+']/Resources<</XObject<</Im0 4 0 R>>>>/Contents 5 0 R>>endobj\\n');
  off[4]=len;add('4 0 obj<</Type/XObject/Subtype/Image/Width '+w+'/Height '+h+'/ColorSpace/DeviceRGB/BitsPerComponent 8/Filter/DCTDecode/Length '+im.length+'>>stream\\n');add(im);add('\\nendstream endobj\\n');
  var cs='q '+PW+' 0 0 '+PH+' 0 0 cm /Im0 Do Q';off[5]=len;add('5 0 obj<</Length '+cs.length+'>>stream\\n'+cs+'\\nendstream endobj\\n');
  var x=len,t='xref\\n0 6\\n0000000000 65535 f \\n';for(var k=1;k<=5;k++)t+=String(off[k]).padStart(10,'0')+' 00000 n \\n';
  add(t+'trailer<</Size 6/Root 1 0 R>>\\nstartxref\\n'+x+'\\n%%EOF');return new Blob(parts,{type:'application/pdf'});}
ir.addEventListener('click',async function(e){
  if(!e.target.closest('#ipdf'))return;
  var c=await schema(),blob=pdf(c.toDataURL('image/jpeg',.92),c.width,c.height),a=document.createElement('a');
  a.href=URL.createObjectURL(blob);a.download='PSS-schema-de-principe-'+sel.metier.toLowerCase().normalize('NFD').replace(/[\\u0300-\\u036f]/g,'').replace(/[^a-z0-9]+/g,'-')+'.pdf';document.body.appendChild(a);a.click();
  setTimeout(function(){URL.revokeObjectURL(a.href);a.remove();},4000);});
})();
</script>"""

PAGES['parcours'] = ('parcours', 'Votre parcours · À qui nous adressons-nous ?', 'Particuliers, investisseurs, porteurs de projet, professionnels : votre profil, votre livrable.', PARCOURS)
PAGES['ia-metier'] = ('ia', 'IA métier · L\'intelligence artificielle adaptée à votre métier', 'Documentaire interactif, veille métier, assistants et automatisation : un socle commun et des options selon votre métier.', IA)
EXTRA_JS = {'parcours': PARCOURS_JS, 'ia-metier': IA_JS}



# ---- plateformes intégrées (crédit, investissement) : elles s'ouvrent dans le site, dans la charte PSS ----
def app(kind, src, title, back):
    return (f'<div class="apphead"><a class="back" href="{back[1]}">{BK} {back[0]}</a><span class="appt">{title}</span></div>'
            f'<iframe class="appframe" id="app" data-kind="{kind}" data-src="{src}" title="{title}"></iframe>')


APP_JS = """<script>
(function(){var f=document.getElementById('app'),q=new URLSearchParams(location.search),src=f.getAttribute('data-src');
if(f.getAttribute('data-kind')==='credit'){var r=(q.get('r')||'').replace(/[^a-z0-9-]/g,'');if(r)src+='#/'+r;}
else{var p=(q.get('profil')||'').replace(/[^A-Za-z]/g,'');if(p)src+='?profil='+p;}
f.src=src;})();
</script>"""

PAGES['credit'] = ('parcours', 'Crédit depuis l\'étranger · Plateforme crédit', 'Logement et crédit en Algérie depuis la France, l\'Espagne, l\'Allemagne, la Belgique ou le Québec : quatre niveaux, le premier gratuit.',
                   app('credit', 'plateformes/credit.html', 'Crédit · 5 pays', ('Votre parcours', 'parcours.html#particuliers')))
PAGES['diagnostic-initial'] = ('parcours', 'Diagnostic initial · Plateforme investissement', 'Votre diagnostic gratuit en PDF : cadre légal, institutions, structure et financement de votre projet en Algérie.',
                               app('invest', 'plateformes/investissement.html', 'Diagnostic gratuit · PDF', ('Votre parcours', 'parcours.html#investisseurs')))
EXTRA_JS['credit'] = APP_JS
EXTRA_JS['diagnostic-initial'] = APP_JS
APP_PAGES = ('credit', 'diagnostic-initial')

FAQ = [('Où intervenez-vous ?', 'Le cabinet accompagne les projets liés à l\'Algérie, depuis l\'Algérie et depuis l\'étranger : France, Espagne, Allemagne, Belgique, Québec.'),
       ('Faut-il créer un compte ?', 'Non. Le parcours d\'avis fonctionne sans inscription.'),
       ('Ma photo est-elle envoyée au cabinet ?', 'Non. La photo reste sur votre appareil et est intégrée à votre fiche en image (PNG).'),
       ('Comment partager mon avis ?', 'Vous préparez votre fiche, puis vous la téléchargez ou choisissez le partage proposé par votre téléphone. Vous confirmez vous-même la publication.'),
       ('Comment accéder à la plateforme crédit ?', 'Dans Votre parcours, section Particuliers · crédit depuis l\'étranger : quatre niveaux, le premier gratuit, pour la France, l\'Espagne, l\'Allemagne, la Belgique et le Québec.')]

PAGES['faq'] = ('contact', 'Questions fréquentes · Vos questions, nos réponses', 'Questions fréquentes sur le cabinet Praetorian Sentinel Smart.',
                head('Questions fréquentes', 'Vos questions, nos réponses', None, ('Contactez-nous', 'contact.html')) +
                '<section class="sec first">' + ''.join(f'<div class="qa"><button type="button">{q}<i>+</i></button><div class="ans"><p>{a}</p></div></div>' for q, a in FAQ) +
                '<div class="row">' + lnk('Poser une autre question', 'contact.html') + '</div></section>')

PLAN_EXTRA = [('·', 'Espace client', 'espace.html', [('Base documentaire', 'documentation.html')])]
SECS = [('01', 'Accueil', 'index.html', [('Vous êtes ?', 'index.html#pour-qui'), ('Nos solutions', 'index.html#services'), ('AIT', 'index.html#agent')]),
        ('02', 'Le cabinet', 'cabinet.html', [('Notre méthode', 'methode.html'), ('Nos domaines d\'expertise', 'divisions.html'), ('Nos références', 'references.html'), ('Notre conformité', 'notreconformite.html'), ('Nous rejoindre', 'carrieres.html')]),
        ('03', 'Votre parcours · À qui nous adressons-nous ?', 'parcours.html', [('Particuliers · crédit depuis l\'étranger (5 pays)', 'parcours.html#particuliers'), ('Investisseurs · diagnostic initial (PDF)', 'parcours.html#investisseurs'), ('Porteurs de projet · diagnostic de lancement (PDF)', 'parcours.html#porteurs'), ('Professionnels et entreprises · IA métier', 'parcours.html#professionnels'), ('Trouver mon offre en 3 étapes', 'parcours.html#filtre'), ('Accompagnement sur devis', 'parcours.html#devis')]),
        ('04', 'IA métier', 'ia-metier.html', [('Documentaire interactif', 'ia-metier.html#documenter'), ('Veille métier', 'ia-metier.html#surveiller'), ('Assistants et automatisation', 'ia-metier.html#automatiser')]),
        ('05', 'Académie PSS', 'academie.html', [('Nos formations', 'academie.html')]),
        ('06', 'Avis clients', 'avis.html', [('Références professionnelles', 'references.html'), ('Donner votre avis', 'donner-mon-avis.html')]),
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
<main class="page{mcls}">
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
    html = TPL.format(title=title.replace('&amp;', '&'), desc=desc.replace('"', '&quot;'), name=name, sec=s, content=content, mcls=' app' if name in APP_PAGES else '',
                      extra=FAQ_JS if name == 'faq' else EXTRA_JS.get(name, ''))
    open(os.path.join(ROOT, name + '.html'), 'w', encoding='utf-8').write(html)
    print('ok', name)
