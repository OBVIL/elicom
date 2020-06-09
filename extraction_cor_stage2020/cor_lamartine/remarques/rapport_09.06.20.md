# Travail sur la correspondance de Lamartine

## Rapport du mercredi 9 juin 2020

- Tests avec l'utilisation des print() dans le terminal.

-  On règle la question des regex pour les chiffres romains. Les 97 sont matchés. (je mets une balise en plus dans le HTML, cela permettra de simplifier le code).

- Pour les destinataires, 96 sont matchés. RÉGLER LA QUESTION DU MANQUANT.

- Pour les signatures de Lamartine,
je crée une nouvelle regex plus universelle pour remplacer les précédentes que j’avais faites. 
(A\|AL.+(?:[DL].+))(?:$|(.+))?")  84 matches.
Je passe au peigne fin le HTML :  je recense 11 lettres non signées (XVII, XIX, LX, LXV, LXXII, LXXIII, LXXVI, LXXX, LXXXVI, XCV, XCVI) et deux lettres signées ainsi :
LXXXVII Signe Ton ami in aeternum !
LXXXVIII Signe Adieu, ton ami
Et une double signature LXVII. → ALPH.
97-13 = 84, donc c’est bon, le résultat est normal. 
MAIS en réalité, il manque une signature 
et il y a un match non pertinent : A. monsieur Prosper Guichard de Bienassis
Reste le problème des matches qui sont parfois trop étendus et qui prennent en compte des PS etc. J’ajoute quelques balises `<p>` dans le HTML ce qui permettra de simplifier le code Python. 
Tous les matches sont OK.
- Je me fais une petite fiche pour les regex en python et je consulte différents sites qui les expliquent afin d’être plus efficace à l’avenir et renforcer les bases.
- Mardi : Voir comment on peut exploiter les Adieu pour les `<salute>`.
Voir pour le code pour l’extraction des lettres. 
Voir pour le destinataire manquant. 
