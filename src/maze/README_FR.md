# 🌀 A Maze'ing - Générateur et Solveur de Labyrinthes

## 📌 Vue d'ensemble

Ce projet contient une suite complète pour générer et résoudre des labyrinthes. Il utilise l'algorithme **Hunt and Kill** pour créer des labyrinthes parfaits et un algorithme de **backtracking** pour les résoudre.

---

## 📁 Structure du projet

### `Maze.py` - Classe Maze
Représente la structure d'un labyrinthe avec toutes ses propriétés et méthodes.

**Éléments principaux:**
- **Cell (Enum):** Types de cellules du labyrinthe
  - `ENTRY (E)` - Point d'entrée
  - `EXIT (X)` - Point de sortie
  - `BLANK ( )` - Passage vide
  - `WALL (█)` - Mur
  - `STRICT (▒)` - Zone restreinte (le logo "42")
  - `SOLVE (•)` - Partie de la solution

- **Color (Enum):** Couleurs ANSI pour l'affichage en terminal (16 couleurs + 256 palette)

**Méthodes essentielles:**
| Méthode | Description |
|---------|-------------|
| `change_cell()` | Modifie le type d'une cellule |
| `is_editable()` | Vérifie si une cellule peut être modifiée |
| `show_maze()` | Retourne la représentation visuelle du labyrinthe |
| `clean_maze()` | Remet tous les murs à zéro |
| `clean_path()` | Efface le chemin de la solution |
| `put_logo()` | Place le logo "42" au centre du labyrinthe |
| `change_keys()` | Change le thème visuel (4 thèmes disponibles) |

**Thèmes disponibles:**
- Default (ASCII art)
- Cubic (carrés colorés 🟦🟥⬛)
- Emojis (🚪🏁🧱)
- Animal (animaux 🦭🦕🦖)

---

### `Maze_Generator.py` - Classe Maze_Generator
Génère un labyrinthe en utilisant l'algorithme **Hunt and Kill**.

**Fonctionnement:**
1. **Phase de Chasse (Kill):** Parcours aléatoire depuis une cellule, creusant des passages jusqu'à une impasse
2. **Phase de Chasse (Hunt):** Scanne la grille pour trouver une cellule non visitée adjacente à une visitée
3. Répète jusqu'à visiter tous les passages

**Caractéristiques:**
- Gère les contraintes de **parité** pour assurer des labyrinthes "parfaits"
- Évite le logo "42" pendant la génération
- Affichage en temps réel avec animation
- Support des graines aléatoires pour reproductibilité
- Connecte correctement l'entrée et la sortie

**Paramètres de configuration:**
```python
config = {
    "WIDTH": 31,           # Largeur du labyrinthe
    "HEIGHT": 17,          # Hauteur du labyrinthe
    "ENTRY": (0, 0),       # Coordonnées d'entrée
    "EXIT": (30, 16),      # Coordonnées de sortie
    "PERFECT": True,       # Forcer un labyrinthe parfait
    "SEED": 12345          # Graine aléatoire (optionnel)
}
```

---

### `resolution.py` - Fonction resolution()
Résout le labyrinthe en trouvant le chemin le plus court de l'entrée à la sortie.

**Algorithme:**
- **Backtracking récursif:** Explore le labyrinthe, marque les chemins visités
- **Heuristique:** Priorise les directions qui rapprochent de la sortie
- Revient en arrière si une impasse est atteinte

**Retour:**
Chaîne de directions: `"NSEWNSEW..."` (Nord, Sud, Est, Ouest)

**Animations:**
- Affiche l'exploration en temps réel (sauf si `HIDE: True`)
- Marque le chemin visité avec `•`
- Option `HIDE` pour résoudre silencieusement

---

## 🚀 Utilisation

### Générer un labyrinthe
```python
from Maze import Maze, Color
from Maze_Generator import Maze_Generator

# Créer un labyrinthe
maze = Maze(
    width=31, height=17,
    entry=(0, 0), exit=(30, 16),
    color={...}  # couleurs pour chaque type de cellule
)

# Générer avec Hunt and Kill
generator = Maze_Generator()
config = {
    "WIDTH": 31, "HEIGHT": 17,
    "ENTRY": (0, 0), "EXIT": (30, 16),
    "PERFECT": True, "SEED": 42
}
generator.hunt_and_kill(maze, config)

# Afficher
print(maze.show_maze())
```

### Résoudre un labyrinthe
```python
from resolution import resolution

config = {
    "WIDTH": 31, "HEIGHT": 17,
    "EXIT": (30, 16), "ENTRY": (0, 0),
    "HIDE": False  # True pour pas d'animation
}

chemin = resolution(maze, config)
print(f"Solution: {chemin}")
```

---

## 🎨 Affichage en couleurs

Les labyrinthes s'affichent en couleur dans le terminal grâce aux codes ANSI. Exemple:
```
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒███████████████████▒
▒█E    █           █▒
▒█████ █ █████████ █▒
▒█ █X  █   █   █   █▒
▒█ ███ ███ █ █ █████▒
▒█     █     █     █▒
▒█ █████ █████████ █▒
▒█     ▒   ▒▒▒   █ █▒
▒█ ███ ▒██ ██▒ ███ █▒
▒█ █ █ ▒▒▒ ▒▒▒     █▒
▒█ █ █ ██▒ ▒██ █████▒
▒█   █ █ ▒ ▒▒▒     █▒
▒███ █ █ █ ███████ █▒
▒█   █ █       █   █▒
▒█████ █████ █ █ █ █▒
▒█     █     █ █ █ █▒
▒█ █████████████ █ █▒
▒█               █ █▒
▒███████████████████▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
```

---

## ⚙️ Détails techniques

### Parité et labyrinthes parfaits
L'algorithme gère la **parité** (paire/impaire) des coordonnées pour assurer que:
- Aucune cellule n'est isolée
- Il existe un chemin unique entre deux points
- Les contraintes géométriques sont respectées

### Logo "42"
Si le labyrinthe est assez grand (>9×7), un logo "42" est inséré au centre comme zone restreinte (impossible à traverser).

### Performances
- Génération en temps réel avec rafraîchissement 25 Hz
- Résolution animée avec pas de 0.05s
- Optimisé pour les grilles de taille modérée

---

## 📋 Résumé des fichiers

| Fichier | Rôle |
|---------|------|
| `Maze.py` | Représentation et manipulation du labyrinthe |
| `Maze_Generator.py` | Génération par algorithme Hunt and Kill |
| `resolution.py` | Résolution par backtracking |
| `__init__.py` | Initialisation du package |
