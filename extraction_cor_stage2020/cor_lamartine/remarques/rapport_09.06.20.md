#Travail sur la correspondance de Lamartine

###Rapport du mardi 9 juin 2020


- j’ai résolu la question du destinataire manquant : 
un point suivait le A. ce qui changeait la donne. 
J’ai donc changé l’expression régulière en fonction, ce qui fait : 
`RE_DEST = re.compile(r"(A\. monsieur |A monsieur.+(?:[BV].+))(?:$|(.+))?")`
Désormais, tous les destinataires sont matchés.

- J’ai pu extraire les lettres et les mettre dans un fichier dump, comme cela avait été fait pour la correspondance de Sand, après avoir résolu un problème de boucle qui venait d’une mauvaise indentation et m'a fait perdre du temps.

- Ainsi, j’ai pu mieux constater dans les fichiers XML tous les changements qu’il reste à faire :
	- les noms de lieux sont dans une balise `<date/>`
	- le lieu et la date qui commencent les lettres sont dans une même balise `<p/>` et ne se trouvent pas dans le `<opener/>`.

- Pour l’instant
	- j’ai ajouté une balise `<respsStmt/>` dans la TEI pour plus de précision dans le projet. Voir si cela est pertinent ou non. 
	- je suis en train de chercher des solutions de regex pour les `<salute/>` qui comprennent pour la plupart du temps le terme « Adieu ». Je rencontre des difficultés à le matcher. 	
	- je cherche également une regex pour les post-scriptum. Il faudra matcher tout ce qui se trouve entre la signature et la lettre suivante (donc le chiffre romain). 
	- Il faudra voir si le fait qu’il y a un `<p/>` après le `<closer/>` pose ou non problème, ou si je les mets dans le `<closer/>` , et à quel endroit, sous quelle balise.

Trouver les bonnes regex me demande encore dans l’ensemble pas mal de temps. 