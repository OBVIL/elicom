#!/usr/bin/env/python
# -*- coding: utf-8 -*-

"""
Extraire le texte des 'xml' pour la partie Correspondances
Script différent pour les Works
"""

import glob
import re
from bs4 import BeautifulSoup, NavigableString, Tag

from lxml import etree
from lxml.builder import ElementMaker

RE_PROUDHON = re.compile(r"P\.-J\. PROUDHON")
RE_DEST = re.compile(r"A M\. [A-Z].+")
RE_DATE = re.compile(r"([^,]+), (.+)$")

#LE FILEPATH
filepath = "proudhon-cor-vol1.html"

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
	
	if RE_PROUDHON.search(text.upper()):
		lettres.append(lettre)

		lettre = []
		lettre.append(text)
	
	else:
		lettre.append(text)

E = ElementMaker(namespace="http://www.tei-c.org/ns/1.0", nsmap={None: "http://www.tei-c.org/ns/1.0"})
for i, lettre in enumerate(lettres[1:]):
	to, lieu, date = "", "", "" #l'ordre n'importe pas
	corps = []
	try:
		n, date, to, *corps = lettre
		if RE_DEST.findall(to):
			pass
				
		m = RE_DATE.search(date)
		if m :
			lieu = m.group(1)
			date = m.group(2)

	except ValueError:
		pass

	teifile = E.TEI (
		E.teiHeader (
			E.fileDesc (
				E.titleStmt(E.title("Correspondance Pierre-Joseph Proudhon"), 
					E.author("Pierre-Joseph Proudhon"), 
					E.respStmt(E.resp("Encodage réalisé pour Obvil dans le cadre d'un stage M2 TNAH de l'ENC, sous la direction d'Arthur Provenier"), 
						E.persName(E.forename("Lucie"), E.surname("Slavik")))),
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
						E.persName("Pierre-Joseph Proudhon", key="Proudhon, Pierre-Joseph (1809-1865)", ref="https://data.bnf.fr/fr/11920705/pierre-joseph_proudhon/"),
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
						E.placeName(lieu),
						E.date(date)
						),
					E.salute()
					),
				*[E.p(p) for p in corps],
				E.closer(
					E.salute(),
					E.signed("P.-J. PROUDHON."),
				), 
				E.postscript(
					E.p()), type="letter")
		)
	))

	f = "dump/proudhon-cor-vol1-%s.xml" %i
	with open(f, 'wb') as fout:
		fout.write(etree.tostring(teifile,
									xml_declaration=True,
									pretty_print=True,
									encoding='UTF-8'))
		
