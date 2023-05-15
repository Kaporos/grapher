# Grapher by Théo

Yoo! 

Tu veux utiliser cet outil trop cool ? normal c'est le meilleur.

Bref..

## Installation

1. Télécharge ce repo github en zip (y a un bouton vert en haut a droite, demande a qqn si tu sais pas comment faire)
2. Extrait pour avoir un dossier sur ton pc contenant les fichiers python
3. Ouvre un terminal (encore une fois, demande à quelqu'un si tu sais pas comment faire #vlad )
4. Lance "install.py" (ATTENTION ! Une fois lancé, ne déplace plus les fichiers python du dossier dans lequel ils sont, sinon ça marchera plus)
5. Si le programme t'affiche "Installé !" Alors c'est bon :)

(Si tu devais modifier l'emplacement des fichiers python, relance install.py au nouvel endroit et ça sera bon :) )

## Note

Si tu utilises le format tab delimited text file (fichiers en .txt), renomme les en .csv !

## Utilisation

C'est **TRES** simple d'utilisation.

Crée un dossier sur ton pc (ou tu veux) et met tes fichiers csv dedans. 

IL FAUT UN DOSSIER PAR GRAPHE (un dossier = un graphe )

Si tu veux superposer plusieurs csv, met en juste plusieurs dans le dossier

Ensuite ouvre un explorateur de fichier windows, fait un clic droit sur le dossier, et tu devrais voir une option "Build graph for this directory"

(eh oui, je fait de la magie moi :) )

Clique dessus, et choisis entre "View" et "Generate image". View t'affichera le graphe et "Generate Image" créera une image plot.png dans le dossier avec ton plot.

## Configuration des graphes

Lors du lancement du programme, il créera des fichiers ".toml" dans ton dossier (s'ils n'existent pas). Ces fichiers sont des fichiers de configuration. Edite les pour paramétrer ton graphe.

Fichiers créés: "config.toml" -> Configuration du graphe en tant que tel.

D'autres fichiers toml seront créés (un par csv) pour paramétrer chaque graphe individuellement.

## Conclusion 

Enjoy !
