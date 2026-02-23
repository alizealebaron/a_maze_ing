*This project has been created as part of the 42 curriculum by alebaron, tcolson.*

# A_maze_ing

## Comment utiliser a_maze_ing ?

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

Premièrement commencons par creer notre environnement virtuel et installer tout nos packages dessus:
```bash
make all
```

Ensuite, une fois notre environnement initialisé, on entre dedans en utilisant:
```bash
source .venv/bin/activate
```

Puis on execute notre programme en donnant un fichier de configuration en second argument.
```bash
python3 a_maze_ing.py default_config.txt
```

## Bonus

Pour prétendre a la note maximale, notre projet doit avoir 5 bonus. Ces bonus sont libres et doivent être un plus dans l'implémentation. Voici donc une liste des additions de notre a_maze_ing:

1. **Couleurs aleatoires** : A chaque exécution, une couleur aleatoire est défini pour chaque élément du labyrinthe.

2. **Thème de caractère** : Depuis le menu, en appelant la 3eme option, vous pourrez choisir parmis les 4 themes ASCII disponible.

3. **Compteur de pas**: En affichant le chemin, le programme precise le nombre de pas necessaires pour aller de l'entrée a la sortie.

4. **Gestion de thème de couleurs** : Différents themes de couleurs sont disponibles et peuvent être défini depuis l'option 4 du menu.

5. **Affichage de la seed** : La seed d'aléatoire permet de s'assurer de retrouver la meme génération a l'execution du programme, elle est affichée a chaque affichage du labyrinthe afin de pouvoir la récuperer au besoin.

6. **Un petit truc en plus** : Un dernier bonus est caché, ne nous quittez pas trop vite...
