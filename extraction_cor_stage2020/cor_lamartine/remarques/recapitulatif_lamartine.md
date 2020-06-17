# Extraction des lettres de Lamartine
# Volume 1

## Récapitulatif sur le code python *extraction-elicom_lamartine.py*


- 96 lettres sur 97 sont matchées. La dernière a disparu, je ne me l'explique pas. Elle est pourtant bien présente dans le fichier HTML. Il faudra donc créer un fichier xml pour la lettre 97, qu'on intitulera lamartine-cor-vol1-96 (puisque la numérotation commence à 0), et que l'on construira selon l'arborescence utilisée pour les autres lettres. 

- Pour ce qui est de l'arborescence, dans le `<teiHeader>` :  
	- J'ai ajouté dans le `<teiHeader>` les balises `<respStmt/>`, après le `<titleStmt/>` ce qui donne : 
	```
	<respStmt>
          <resp>Encodage réalisé pour Obvil dans le cadre d'un stage M2 TNAH de l'ENC, sous la direction d'Arthur Provenier</resp>
          <persName>
            <forname>Lucie</forname>
            <surname>Slavik</surname>
          </persName>
        </respStmt>
	```
	Ce choix est à faire valider par mon tuteur, Arthur Provenier.

	- Dans le `<profileDesc/>` et `<correspAction/>`, la balise `<persName/>` a été modifiée selon les attentes d'Elicom, ce qui donne :
```
          <persName key="de Lamartine, Alphonse (1790-1869)" ref="https://data.bnf.fr/fr/11910800/alphonse_de_lamartine/">Alphonse de Lamartine</persName>
```

	- En revanche, certains problèmes subsistent : 
Ainsi, pour la `<date/>`, le lieu est également indiqué, ce qui est problématique. Soit il faut améliorer le code, soit il faudra tout corriger manuellement. 
Ce qui donne, toujours dans le `<correspAction/>`
```
			<date when="Mâcon, 1er septembre 1809." resp="">Mâcon, 1er septembre 1809.</date>
```
Dans d'autres correspondances, comme la lettre du 19 février 1809, lamartine-cor-vol1-25.xml, il n'y a aucun rapport, la date affiche simplement un lieu. 
```
           <date when="Au Grand-Lemps." resp="">Au Grand-Lemps.</date>
```

	- De même, toujours dans le `<correspAction/>`, le lieu est également matché avec le `<persName/>`. Par ailleurs, la valeur de l'attribut `key` ne s'affiche pas selon les normes de *data.bnf*, contrairement à Lamartine. Les dates de naissance et de mort ne sont pas indiquées, ce qui donne, pour la lettre du 1er septembre 1809, de Lamartine à Aymon de Virieu : 
```
		 <persName key="A monsieur Aymon de Virieu Au Grand-Lemps. (...-...)">A monsieur Aymon de Virieu Au Grand-Lemps.</persName>
```
	- Enfin, dans la balise `<creation/>`, la balise `<date/>` matche également le lieu. Il faudrait donc soit modifier le code, soit le corriger manuellement. 

- Toujours pour ce qui est de l'arborescence, dans le `<text>` cette fois :  
	- on rencontre le même problème que plus haut pour la date, que ce soit au sein du `<dateline/>` où la distinction n'est pas faite entre le lieu et la date :
	```
	    <dateline>
            <placeName></placeName>
            <date>Mâcon, 1er septembre 1809.</date>
        </dateline>
	```
	À ce propos, j'ai ajouté la balise `<placeName/>`. Ce choix est à faire valider par mon tuteur, Arthur Provenier.

	- Dans le `<body/>`, après l'`<opener/>` se trouve les séries de `<p/>`. A ce propos, parfois ceux-ci servent à des vers. Or, la balise utilisée habituellement pour les vers sont les `<lg/>` et les `<l/>`. Il faudra voir si on modifie ou non. C'est probablement secondaire. 
	- De même, les vers ou les phrases en latin ou en grec ne sont pas mentionnés comme telles.
	```
	<p>Hélas ! voyageurs que nous sommes,</p>
        <p>Nos jours seront bientôt passés,</p>
        <p>Et de la demeure des hommes</p>
        <p>Demain nos pas sont effacés !</p>
        <p>Qu'il est beau ce désir de l'âme</p>
        <p>Dont la noble fierté réclame</p>
        <p>Contre un ténébreux avenir,</p>
        <p>Dont l'orgueil aux races futures,</p>
        <p>Pour prix des vertus les plus pures,</p>
        <p>Ne demande qu'un souvenir !</p>
        <p>C'est une méchante strophe de ma méchante ode sur l'amour de la gloire. C'est à nous de dire comme Corinne : Oh! que j'aime l'inutile ! Mais, afin de pouvoir, le dire en toute tranquillité, il nous faut d'abord posséder ce qui est plus que l'utile, le nécessaire : un état, un métier, un art, non meliora piis !</p>
	```

	- Quant au `<closer/>`, le `<salute/>` est toujours vide car les 'Adieux' et autres expressions ne sont pas matchés de façon efficace.

	- En revanche, la signature apparaît bien dans le `<signed>`

- Nota Bene
	- De nombreux problèmes subsistent. Je ne les ai pas tous recensés. Ce commentaire a été fait pour la plupart d'après la lettre du 1er septembre 1809 lamartine-cor-vol1-36.xml. 
	- À titre d'exemple, on peut souligner les décalages entre les balises et leur contenu, comme pour la lettre lamartine-cor-vol1-51.xml, où la signature est au mauvais endroit, dans un `<p/>` avant le `<closer/>`, et le post-scriptum se trouve à la place de la signature
	```
	<p>Adieu. En voilà bien assez long. Je t'embrasse et suis pour la vie le meilleur de tes amis,</p>
        <p>ALPH. DE LAMARTINE.</p>
        <closer>
          <salute></salute>
          <signed>P.-S. Je vais passer ma soirée à la Comédie. On donne la Reine de Golconde.</signed>
          <postscript></postscript>
	```
	- De même pour la lettre lamartine-cor-vol1-58.xml, on lit :
	```
	<p>Adieu, écris-moi promptement.</p>
        <closer>
          <salute></salute>
          <signed>Même adresse.</signed>
          <postscript></postscript>
        </closer>
	```
=> En règle générale, une attentive correction sera malheureusement nécessaire, sauf si l'on arrive à résoudre les différents problèmes évoqués. 