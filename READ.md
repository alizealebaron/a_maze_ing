*This project has been created as part of the 42 curriculum by alebaron, tcolson.*

# A_maze_ing

## 🔮 Comment utiliser a_maze_ing ?

Afin de faciliter l'utilisation de notre programme a_maze_ing, un Makefile vous est fourni et comprend un certains nombre de commande utile pour installer le projet :

```bash

# Créer un nouvel environnement et installer les packages python nécessaires.
make all

# Créer uniquement un nouvel environnement virtuel .venv
make venv

# Installer uniquement les packages python
make install

# Lancer le programme principal avec le fichier de configuration default_config.txt
make run

# Nettoyer tous les dossiers créer par python
make clean

# Compresser le dossier de génération de labyrinthe
make package
```

## 📋 Description

A-Maze-ing est un programme en Python dédié à la génération et à la visualisation de labyrinthes. L'objectif principal est de créer un outil capable de transformer un fichier de configuration textuel en un labyrinthe structuré, tout en proposant une interface visuelle pour l'utilisateur. 

Le projet se divise en trois grandes fonctionnalités :

1. **Génération de labyrinthes** : Le programme génère des labyrinthes de tailles variées. Il peut créer des "labyrinthes parfaits" (possédant un chemin unique entre l'entrée et la sortie). La génération du labyrinthe se fait à partir des données présentes dans le fichier de configuration.

2. **Visualisation interactive** : Le programme propose un affichage visuel en mode texte. L'utilisateur peut régénérer un labyrinthe, changer les couleurs et afficher ou masquer le chemin le plus court pour résoudre le casse-tête.

3. **Export de données** : Le résultat est sauvegardé dans un fichier texte. Chaque cellule est représentée par un chiffre hexadécimal codant la position des murs (Nord, Est, Sud, Ouest).

Enfin, le moteur de génération est conçu comme un module Python réutilisable, permettant d'intégrer facilement cette logique dans d'autres projets.

## 📜 Instructions

Premièrement, commençons par créer notre environnement virtuel et installer tous nos packages dessus :
```bash
make all
```

Ensuite, une fois notre environnement initialisé, on entre dedans en utilisant :
```bash
source .venv/bin/activate
```

Puis on exécute notre programme en donnant un fichier de configuration en second argument.
```bash
python3 a_maze_ing.py default_config.txt
```

Vous pouvez aussi utiliser la commande `make run` qui exécutera le programme avec le fichier `default_config.txt`.

## 📝 Fichier de configuration

Le labyrinthe sera entièrement généré à partir des données envoyées dans le fichier de configuration. Les données obligatoire sont les suivantes :

|Clé|Description|Example|
|:---|:---:|:---:|
|WIDTH| La largueur du labyrinthe| WIDTH=15
|HEIGHT| La hauteur du labyrinthe| HEIGHT=10
|ENTRY| Coordonnées de l'entrée (x,y)|ENTRY=0,0
|EXIT| Coordonnées de la sortie (x,y)|EXIT=4,4
|OUTPUT_FILE| Nom du fichier de sortie|OUTPUT_FILE=output.txt
|PERFECT| Le labyrinthe est-il parfait ?|PERFECT=True
|SEED| (Optionnel) La seed à utiliser|SEED=42|

Par défault, le fichier de configuration est `default_config.txt`.

## 🩹 Algorithme de génération

**Description de l'algorithme**

L'algorithme Hunt and Kill est une méthode de génération de labyrinthes qui garantit un résultat "parfait" (un seul chemin possible entre deux points). Il fonctionne en deux phases alternées :

1. Phase "Kill" (Marche aléatoire) :

    - On part d'une cellule initiale choisie au hasard.
    - On se déplace de cellule en cellule vers un voisin non visité, en cassant le mur entre les deux.
    - On continue jusqu'à ce que la cellule actuelle n'ait plus aucun voisin non visité (on est dans un cul-de-sac).

2. Phase "Hunt" (Chasse) :

    - L'algorithme scanne le labyrinthe (ligne par ligne) pour trouver une cellule non visitée qui possède au moins un voisin déjà visité.
    - Si une telle cellule est trouvée, on casse le mur pour la relier à son voisin visité.
    - Cette nouvelle cellule devient le point de départ d'une nouvelle phase "Kill".

L'algorithme s'arrête lorsque toutes les cellules ont été visitées, garantissant ainsi qu'il n'y a aucune zone isolée.

**Pourquoi avoir choisi cet algorithme ?**

Le choix de l'algorithme Hunt and Kill repose sur plusieurs critères techniques:

- Simplicité d'implémentation : L'algorithme hunt and kill repose principalement sur deux fonctions simples à comprendre et à implémenter. 

- Structure du labyrinthe : Il produit des labyrinthes avec des passages longs et sinueux, ce qui les rend plus difficiles et esthétiques que d'autres méthodes comme l'algorithme de Prim.

- Connectivité parfaite : Il assure par conception que chaque cellule est connectée au reste du réseau, respectant la contrainte de "labyrinthe parfait".

## 🗂️ Architecture des dossiers

- a_maze_ing.py : Fichier racine du programme et point d'entrée.
- src/configuration/* : Gestion et récupération de la configuration depuis le fichier passé en paramètre.
- src/maze/* : Génération et gestion du labyrinthe dans son ensemble.
- src/menu/* : Affichage du menu et gestion des inputs de l'utilisateur
- src/output/* : Génération du fichier d'output
- src/utils/* : Tout fichier utile utilisé dans divers autres fichiers (ex: erreur, enum, ...)

## 👥 Organisation au sein de l'équipe

### Les rôles de chacuns des membres de l'équipe

- alebaron :
    - Algorithme Hunt and Kill
    - Ecriture du Makefile
    - Ecriture des README
    - Parsing du fichier de configuration
    - Ecriture de la docstring

- tcolson :
    - Gestions des couleurs et des thèmes
    - Mise à la norme flake8 et mypy
    - Algorithme de résolution du labyrinthe
    - Création de la classe labyrinthe
    - Génération de l'output

### Organisation au sein de l'équipe

Pour nous organiser efficacement, nous avons suivi une méthode structurée:


- Planification : Nous avons commencé par lister toutes les tâches obligatoires du projet.
- Priorisation : Ces tâches ont été classées par priorité et regroupées par catégories techniques (génération, affichage, export).
- Suivi du travail : Nous avons utilisé un tableau de suivi pour répartir les tâches entre les membres de l'équipe au fur et à mesure de l'avancement du projet a_maze_ing.

Cette méthode nous a permis de visualiser notre progression en temps réel et de collaborer facilement, même lors des sessions de travail à distance. Nous avons principalement utilisé **github**, **google sheet** ainsi que **discord** pour facilité la communication entre nous.

## ✨ Bonus

Pour prétendre à la note maximale, notre projet doit avoir 5 bonus. Ces bonus sont libres et doivent être un plus dans l'implémentation. Voici donc une liste des additions de notre a_maze_ing:

1. **Couleurs aleatoires** : à chaque exécution, une couleur aléatoire est définie pour chaque élément du labyrinthe.

2. **Thème de caractère** : depuis le menu, en appelant la 3e option, vous pourrez choisir parmi les 4 thèmes ASCII disponibles.

3. **Compteur de pas**: en affichant le chemin, le programme précise le nombre de pas nécessaires pour aller de l'entrée a la sortie.

4. **Gestion de thème de couleurs** : différents thèmes de couleurs sont disponibles et peuvent être définis depuis l'option 4 du menu.

5. **Affichage de la seed** : la seed d'aléatoire permet de s'assurer de retrouver la même génération a l'exécution du programme, elle est affichée à chaque affichage du labyrinthe afin de pouvoir la récupérer au besoin.

6. **Un petit truc en plus** : un dernier bonus est caché, ne nous quittez pas trop vite...

## 📚 Ressources

**Ressources générales**

- [github.com/Overtekk/A_Maze_ing](https://github.com/Overtekk/A_Maze_ing)

**Génération du labyrinthe**

- [info.blaisepascal.fr/nsi-labyrinthes](https://info.blaisepascal.fr/nsi-labyrinthes/)
- [8 Maze Generating Algorithms in 3 Minutes](https://www.youtube.com/watch?v=sVcB8vUFlmU)
- [Maze Generation Algorithms - An Exploration](https://professor-l.github.io/mazes/)
- [weblog.jamisbuck.org/maze-generation-hunt-and-kill-algorithm](https://weblog.jamisbuck.org/2011/1/24/maze-generation-hunt-and-kill-algorithm)
- [www.cs.cmu.edu/student-tp-guides/Mazes.pdf](https://www.cs.cmu.edu/~112-n23/notes/student-tp-guides/Mazes.pdf)

**Création du package mazegen**

- [packaging.python.org/en/latest/guides/writing-pyproject-toml](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/)

**Utilisation de l'IA**

- Aide au débuggage du code.
- Aide à l'écriture de certains points du Makefile (make install).
- Reformulation de phrases (README)