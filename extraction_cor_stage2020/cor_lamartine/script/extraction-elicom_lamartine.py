#!/usr/bin/env/python
# -*- coding: utf-8 -*-


"""
Extraire le texte des 'xml' pour la partie Correspondances
Script différent pour les Works
"""

# voir prudhon

### SCRIPT POUR LAMARTINE ###
#Importation des librairies
import glob #-> pas utilisé. Module qui permet d'itérer à travers une arborescence de dossiers.
import re #-> regex
from bs4 import BeautifulSoup, NavigableString, Tag #-> pour utiliser beautifulsoup qui est le parseur html (voir documentation sur internet)

from lxml import etree
from lxml.builder import ElementMaker  

RE_ROMAN_NUMERALS = re.compile(r"^[CDILMVX]+$") #récupérer les chiffres romains (attention à bien laisser l'espace après le -> PIPE
#Matche les 97 chiffres romains qui signalent l'ouverture des lettres. 

RE_LAMARTINE = re.compile(r"(A\.|AL.+(?:[DL].+))(?:$|(.+))?")
#récupérer la signature d'ALPHONSE DE LAMARTINE.84 matches (il ne signe pas toujours)

RE_DEST = re.compile(r"(A\. monsieur |A monsieur.+(?:[BV].+))(?:$|(.+))?") 
#matche les destinataires. 

RE_SALUT = re.compile(r"Mon cher ami")

RE_SALUTE = re.compile(r"Adieu")

RE_PS = re.compile(r"P\.-S\..*")

RE_DATELINE = re.compile(r"[Milly|Mâcon|Lyon|Saint\-Point|Péronne|Dijon|Bologne|Livorno|Florence|Napoli|Naples|Lausanne].+[0-9]{4}")

#LE FILEPATH
filepath = "lamartine-cor-vol1.html"

def strip_spaces(text):
	return ' '.join(text.split())

with open(filepath, 'r', encoding="utf-8") as fhtml:
	soup = BeautifulSoup(fhtml, 'html.parser') #-> pour parser le html. Librairie en python. 

#La variable lettre contient 1 lettre, la variable lettres, plusieurs lettres. J'ajoute texte si chiffre romain. 
#A chaque nouveau chiffre romain, extrait lettres.

lettres = []
lettre = []
for p in soup.body.find_all('p'):
	text = strip_spaces(p.get_text())
	if RE_ROMAN_NUMERALS.search(text.upper()):
		lettres.append(lettre)

		lettre = []
		lettre.append(text)
	else:
		lettre.append(text)


E = ElementMaker(namespace="http://www.tei-c.org/ns/1.0", nsmap={None: "http://www.tei-c.org/ns/1.0"})
for i, lettre in enumerate(lettres[1:]):
	n, to, date, dateline, salut, salute, signature, ps = "", "", "", "", "", "", "", ""
	try:
		n, to, date, dateline, salut, *corps, salute, signature, ps = lettre
		#print(signature, signature.isupper())
		#print("Lamartine %s" %to)
		if RE_DATELINE.findall(dateline):
			pass 
		#if not RE_DATELINE.search(' '.join(corps)):
			#pass
		if RE_LAMARTINE.findall(signature):
			pass
		#if RE_DEST.findall(to):
			#print(to)
			pass
			#print(RE_LAMARTINE.findall(signature)) N'en matche que 60 ?!
		if RE_SALUT.findall(salut):
			#print(salut)
			pass
		#if not RE_SALUT.search(' '.join(corps)):
			#pass
		#if not RE_DEST.search(' '.join(corps)):
			#pass
			#print('-',corps) PB : le corps matche tout, signature comprise...
		if RE_SALUTE.findall(salute):
			#print(salut)
			pass
		#if not RE_SALUTE.search(' '.join(corps)):
			pass
		if RE_PS.findall(ps):
			#print(ps)
			pass
		#if not RE_PS.search(' '.join(corps)):
			#pass
	except ValueError:
		pass

	teifile = E.TEI (
		E.teiHeader (
			E.fileDesc (
				E.titleStmt(E.title("Correspondance Alphonse de Lamartine"), E.author("Alphonse de Lamartine"), E.respStmt(E.resp("Encodage réalisé pour Obvil dans le cadre d'un stage M2 TNAH de l'ENC, sous la direction d'Arthur Provenier"), E.persName(E.forname("Lucie"), E.surname("Slavik")))),
				E.editionStmt(E.edition()),
				E.publicationStmt(
					E.publisher("Obvil"),
					E.date(when='2020'),
					E.idno(),
					E.availability(E.licence(E.p, target="http://creativecommons.org/licenses/by-nc-nd/3.0/fr/"), status="restricted")
				),
				E.sourceDesc(E.bibl()),
			),
			E.profileDesc (
				E.correspDesc(
					E.correspAction(
						E.persName("Alphonse de Lamartine", key="Alphonse de Lamartine (...-...)"),
						E.date(date, when="%s" %date, resp=""),
						type="sent"
					),
					E.correspAction(
						E.persName(to, key="%s (...-...)" %to),
						type="received"
					),
					E.correspContext(
						E.ref(type="prev", target="foo.xml"),
						E.ref(type="next", target="bar.xml"),
					)
				),
				E.creation(E.date(when='%s' %date)),
				E.langUsage(E.language(ident="fre"))
			)
		),

		E.text(
			E.body(E.div(
				E.opener(
					E.dateline(date),
					E.salute(),
					),
				*[E.p(p) for p in corps],
				E.closer(
					E.salute(),
					E.signed(
						E.name(
							E.signature()
							)
						
					),
                                # Il manquait la virgule surement
				E.postscript(ps)	
				), type="letter")
		)
	))

	f = "dump/lamartine-cor-vol1-%s.xml" %i
	with open(f, 'wb') as fout:
		fout.write(etree.tostring(teifile,
									xml_declaration=True,
									pretty_print=True,
									encoding='UTF-8'))
