# 🦆 Module Maze - Guide Complet

## 📋 Vue d'ensemble

Le module `maze` est le cœur du programme. Il contient toute la logique pour créer, manipuler, générer et résoudre des labyrinthes. Le module est composé de trois fichiers principaux qui travaillent ensemble.

---

## 📁 Structure des fichiers

### 1. **maze.py** - Les fondations du labyrinthe

Ce fichier définit les classes et énumérations de base qui représentent un labyrinthe.

#### 🎨 Classe `Color` (Énumération)
Contient tous les codes couleur ANSI pour afficher le labyrinthe en couleur dans le terminal.
- **Couleurs simples** : ROUGE, VERT, JAUNE, BLEU, etc.
- **Couleurs avancées** : Orange, Corail, Chaux, Brun, etc.
- **Réinitialisation** : `RESET` pour revenir à la couleur par défaut

#### 🧱 Classe `Cell` (Énumération)
Représente chaque type de cellule possible dans le labyrinthe :
- `ENTRY` ("E") : Point d'entrée du labyrinthe
- `EXIT` ("X") : Point de sortie à atteindre
- `BLANK` (" ") : Chemin vide où on peut se déplacer
- `WALL` ("█") : Mur infranchissable
- `STRICT` ("▒") : Zone interdite/logo (ne peut pas être modifiée)
- `SOLVE` ("•") : Marque le chemin de la solution

#### 🎭 Classe `Maze` - Le cœur du système

C'est la classe principale qui représente un labyrinthe complet.

**Attributs principaux :**
- `width` et `height` : Dimensions du labyrinthe
- `entry` et `exit` : Coordonnées des points d'entrée et sortie
- `maze` : Dictionnaire qui stocke chaque cellule et son type
- `color` : Palette de couleurs utilisée pour l'affichage
- `key` : Le thème graphique actuel (comment afficher les cellules)

**Thèmes disponibles :**
- **Default** : Caractères simples (E, X, █, etc.)
- **Cubic** : Emojis de carrés colorés
- **Emojis** : Emojis variés (portes, briques, etc.)
- **Animal** : Animaux (phoque, dinosaure, etc.)

**Méthodes importantes :**

| Méthode | Description |
|---------|-------------|
| `change_cell(cell, val)` | Modifie le type d'une cellule (si éditable) |
| `is_editable(cell)` | Vérifie si une cellule peut être modifiée |
| `put_logo()` | Ajoute le logo "42" au centre du labyrinthe |
| `clean_maze()` | Réinitialise tous les chemins en murs |
| `clean_path()` | Efface la solution affichée |
| `show_maze()` | Affiche le labyrinthe formaté avec couleurs et bordures |
| `change_keys(key)` | Change le thème graphique |

**Exemple d'utilisation :**
```python
# Créer un labyrinthe 20x20
maze = Maze(20, 20, (1, 1), (18, 18), colors)

# Voir le labyrinthe
print(maze.show_maze())

# Changer le thème
maze.change_keys("Emojis")
```

---

### 2. **generation.py** - La création du labyrinthe

Ce fichier contient l'algorithme pour **générer automatiquement** un labyrinthe parfait.

#### 🎲 Fonction `hunt_and_kill(maze, config)`

C'est l'algorithme principal de génération. Il fonctionne en deux phases alternées :

**Phase 1 - "Kill" (Tuer le chemin)**
- Démarre d'une cellule actuelle
- Explore aléatoirement les cellules non visitées voisines
- Crée un chemin en cassant les murs
- S'arrête quand il n'y a plus de voisins à explorer (cul-de-sac)

**Phase 2 - "Hunt" (Chasser)**
- Scanne toute la grille pour trouver une cellule non visitée
- Qui est adjacente à une cellule déjà visitée
- Connecte ces deux cellules ensemble
- Relance la phase "Kill" depuis cette nouvelle cellule

Cet algorithme garantit que :
✅ Chaque cellule du labyrinthe est accessible
✅ Il n'existe qu'un seul chemin entre deux points quelconques
✅ Il n'y a pas de boucles ni de passages inutiles

**Configuration requise (config) :**
```python
config = {
    "WIDTH": 20,          # Largeur du labyrinthe
    "HEIGHT": 20,         # Hauteur du labyrinthe
    "ENTRY": (1, 1),      # Coordonnées d'entrée
    "EXIT": (18, 18),     # Coordonnées de sortie
    "PERFECT": True,      # Générer un labyrinthe parfait
    "SEED": 12345         # (Optionnel) Graine aléatoire
}
```

**Fonctionnalités spéciales :**
- 🎬 **Affichage en temps réel** : Vous voyez le labyrinthe se générer étape par étape
- 🔒 **Logique de parité** : S'assure que la sortie est toujours atteignable
- 🎨 **Animation fluide** : Utilise `Live` de la bibliothèque `rich` pour l'affichage

**Exemple d'utilisation :**
```python
from src.maze.generation import hunt_and_kill

hunt_and_kill(maze, config)
# Le labyrinthe est modifié en place
```

---

### 3. **resolution.py** - La résolution du labyrinthe

Ce fichier contient l'algorithme pour **trouver le chemin** du début à la fin.

#### 🧭 Fonction `resolution(maze, config)`

Utilise un algorithme de **backtracking récursif** pour explorer le labyrinthe.

**Comment ça marche :**
1. Démarre du point d'entrée (`ENTRY`)
2. Essaie chaque direction possible (intelligemment ordonnées)
3. Marque les cellules visitées avec le symbole "•" (`SOLVE`)
4. Si une direction ne mène nulle part (cul-de-sac), recule et essaie une autre
5. S'arrête quand la sortie (`EXIT`) est trouvée

**Optimisation intelligente - La fonction `get_directions(pos)` :**
- Au lieu d'explorer au hasard, elle **priorise les directions vers la sortie**
- Calcule la distance restante vers la cible
- Explore d'abord les directions qui réduisent cette distance
- Accélère très fortement la résolution

**Configuration requise (config) :**
```python
config = {
    "WIDTH": 20,        # Largeur du labyrinthe
    "HEIGHT": 20,       # Hauteur du labyrinthe
    "ENTRY": (1, 1),    # Point de départ
    "EXIT": (18, 18),   # Point d'arrivée
    "HIDE": False       # False = animation, True = rapide sans affichage
}
```

**Valeur de retour :**
Retourne une chaîne de caractères représentant le chemin :
- `"N"` = Nord (haut, y-1)
- `"S"` = Sud (bas, y+1)
- `"E"` = Est (droite, x+1)
- `"W"` = Ouest (gauche, x-1)

Exemple : `"EESSWWNNEE"` = Droite, Droite, Bas, Bas, Gauche, Gauche, Haut, Haut, Droite, Droite

**Exemple d'utilisation :**
```python
from src.maze.resolution import resolution

chemin = resolution(maze, config)
print(f"Chemin trouvé: {chemin}")
```

---

## 🔄 Workflow complet

Voici comment les trois fichiers travaillent ensemble :

```
1. Créer un objet Maze (maze.py)
   ↓
2. Générer le labyrinthe avec hunt_and_kill (generation.py)
   ↓
3. Résoudre le labyrinthe avec resolution (resolution.py)
   ↓
4. Afficher le labyrinthe résolu (maze.py)
```

**Exemple complet :**
```python
from src.maze.maze import Maze
from src.maze.generation import hunt_and_kill
from src.maze.resolution import resolution

# Étape 1 : Création
config = {
    "WIDTH": 25,
    "HEIGHT": 25,
    "ENTRY": (1, 1),
    "EXIT": (23, 23),
    "PERFECT": True
}

maze = Maze(25, 25, (1, 1), (23, 23), colors)

# Étape 2 : Génération
hunt_and_kill(maze, config)

# Étape 3 : Résolution
chemin = resolution(maze, config)

# Étape 4 : Affichage
print(maze.show_maze())
print(f"Solution: {chemin}")
```

---

## 🎯 Points clés à retenir

| Aspect | Explication |
|--------|------------|
| **Cellules** | Chaque point du labyrinthe est une cellule avec un type (mur, chemin, etc.) |
| **Grille** | Le labyrinthe est stocké dans un dictionnaire de coordonnées (x, y) |
| **Génération** | L'algorithme "Hunt and Kill" crée des labyrinthes parfaits (toujours une solution) |
| **Résolution** | Le backtracking récursif trouve le chemin le plus court |
| **Optimisation** | Les heuristiques (prioriser les directions) rendent tout plus rapide |
| **Affichage** | Chaque cellule a une couleur et un symbole configurable via les thèmes |
| **Logo** | Le célèbre logo "42" est automatiquement placé au centre si l'espace le permet |
