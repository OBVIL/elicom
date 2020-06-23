#!/usr/bin env python

"""
Extraire le texte des 'xml' pour la partie Correspondances
Script différent pour les Works
"""

# voir prudhon

import glob
import re
from bs4 import BeautifulSoup, NavigableString, Tag

from lxml import etree
from lxml.builder import ElementMaker

RE_CHIF_AR = re.compile(r"^[0-9]{1,3}\.") #pour matcher les débuts de lettres. 153 matches au lieu de 197
RE_DEST = re.compile(r"(A [A-Z][A-Z.]+)|^(?:A[A-Z.]+)")# 215 matches non complets
RE_NOTES = re.compile(r"^\d [A-Z].+")

#LE FILEPATH
filepath = "corpus/lamennais-cor-vol1.html"

def strip_spaces(text):
	return ' '.join(text.split())

with open(filepath, 'r', encoding="utf-8") as fhtml:
	soup = BeautifulSoup(fhtml, 'html.parser') #-> pour parser le html. Librairie en python. 

#La variable lettre contient 1 lettre, la variable lettres, plusieurs lettres. J'ajoute texte si chiffre arabe. 
#A chaque nouveau chiffre arabe, extrait lettres.

lettres = []
lettre = []
for p in soup.body.find_all('p'):
	text = strip_spaces(p.get_text())
	if RE_CHIF_AR.search(text.upper()):
		lettres.append(lettre)

		lettre = []
		lettre.append(text)
	elif RE_NOTES.search(text):
		pass
	else:
		lettre.append(text)


E = ElementMaker(namespace="http://www.tei-c.org/ns/1.0", nsmap={None: "http://www.tei-c.org/ns/1.0"})
for i, lettre in enumerate(lettres[1:]):
	n, to, date, signature = "", "", "", ""
	try:
		n, to, date, *corps, signature = lettre
		if RE_DEST.findall(to): 
			pass

	except ValueError:
		pass

	teifile = E.TEI (
		E.teiHeader (
			E.fileDesc (
				E.titleStmt(E.title("Correspondance Félicité de Lamennais"), E.author("Félicité de Lamennais"), E.respStmt(E.resp("Encodage réalisé pour Obvil dans le cadre d'un stage M2 TNAH de l'ENC, sous la direction d'Arthur Provenier"), E.persName(E.forname("Lucie"), E.surname("Slavik")))),
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
						E.persName("Félicité de Lamennais", key="de Lamennais, Félicité (1782-1854)", ref="https://data.bnf.fr/fr/11910852/felicite_de_la_mennais/"),
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
					E.dateline(
						E.placeName(),
						E.date()
						),
					E.salute()
					),
				*[E.p(p) for p in corps],
				E.closer(
					E.salute(),
					E.signed(),
				E.postscript()    
				), type="letter")
		)
	))

	f = "dump/lamennais-cor-vol1-%s.xml" %i
	with open(f, 'wb') as fout:
		fout.write(etree.tostring(teifile,
									xml_declaration=True,
									pretty_print=True,
									encoding='UTF-8'))
