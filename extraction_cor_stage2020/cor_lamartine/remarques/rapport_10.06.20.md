# Travail sur la correspondance de Lamartine

## Rapport du mercredi 10 juin 2020


- REGEX
	- Je matche les adieux pour les mettre dans une balise `<salute/>` dans le `<closer/>`
	- Je matche les post-scriptum pour les mettre ensuite dans une balise `<postcript/>`
	- Je crée une regex pour matcher les `<salute/>` de l'`<opener/>`
	- Je crée une regex pour matcher les `<dateline/>`. Je restreint la baliseles `<name/>` et les `<date/>` pour ne garder que la balise générale `<dateline/>`. En allant plus loin, je me dis que ce n'est pas forcément un bon choix, il faudra que je reprenne mon travail pour voir si je ne dois pas séparer le lieu et la date.
	Quoiqu'il en soit, j'arrive à 91 matches, dont 3 ne sont pas pertinents (ce sont des PS ou des développements matchés à tort) et d’autres matchent des phrases en plus. 
	- En général, il serait bon d'affiner les regex.


- Problèmes rencontrés :
	- la dernière lettre a totalement disparue, elle n'est pas prise en compte.
	- le corps de plusieurs lettres ne s'affiche pas, comme par exemple pour la lettre 
	- je n'arrive pas à intégrer la balise `<postcript/>` dans l'arborescence. Je rencontre un problème de syntaxe que je n'arrive pas à résoudre pour le moment, alors je commente l'endroit concerné (l.150)
	

- Je commence à extraire l'HTML du premier volume de correspondance de Lamennais. Il semble être bien moins propre que le précédent. 