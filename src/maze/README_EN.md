# 🌀 A Maze'ing - Maze Generator and Solver

## 📌 Overview

This project contains a complete suite for generating and solving mazes. It uses the **Hunt and Kill** algorithm to create perfect mazes and a **backtracking** algorithm to solve them.

---

## 📁 Project Structure

### `Maze.py` - Maze Class
Represents the structure of a maze with all its properties and methods.

**Main Elements:**
- **Cell (Enum):** Types of cells in the maze
  - `ENTRY (E)` - Entry point
  - `EXIT (X)` - Exit point
  - `BLANK ( )` - Empty passage
  - `WALL (█)` - Wall
  - `STRICT (▒)` - Restricted area (the "42" logo)
  - `SOLVE (•)` - Part of the solution path

- **Color (Enum):** ANSI colors for terminal display (16 colors + 256 palette)

**Essential Methods:**
| Method | Description |
|--------|-------------|
| `change_cell()` | Modifies the type of a cell |
| `is_editable()` | Checks if a cell can be edited |
| `show_maze()` | Returns the visual representation of the maze |
| `clean_maze()` | Resets all walls to zero |
| `clean_path()` | Erases the solution path |
| `put_logo()` | Places the "42" logo in the center of the maze |
| `change_keys()` | Changes the visual theme (4 available themes) |

**Available Themes:**
- Default (ASCII art)
- Cubic (colored squares 🟦🟥⬛)
- Emojis (🚪🏁🧱)
- Animal (animals 🦭🦕🦖)

---

### `Maze_Generator.py` - Maze_Generator Class
Generates a maze using the **Hunt and Kill** algorithm.

**How it works:**
1. **Kill Phase:** Random walk from a cell, carving passages until a dead end
2. **Hunt Phase:** Scans the grid to find an unvisited cell adjacent to a visited one
3. Repeats until all passages are visited

**Features:**
- Handles **parity** constraints to ensure "perfect" mazes
- Avoids the "42" logo during generation
- Real-time display with animation
- Support for random seeds for reproducibility
- Correctly connects entry and exit points

**Configuration Parameters:**
```python
config = {
    "WIDTH": 31,           # Maze width
    "HEIGHT": 17,          # Maze height
    "ENTRY": (0, 0),       # Entry coordinates
    "EXIT": (30, 16),      # Exit coordinates
    "PERFECT": True,       # Force a perfect maze
    "SEED": 12345          # Random seed (optional)
}
```

---

### `resolution.py` - resolution() Function
Solves the maze by finding the shortest path from entry to exit.

**Algorithm:**
- **Recursive Backtracking:** Explores the maze, marks visited paths
- **Heuristic:** Prioritizes directions that move toward the exit
- Backtracks if a dead end is reached

**Return:**
Direction string: `"NSEWNSEW..."` (North, South, East, West)

**Animations:**
- Displays exploration in real-time (unless `HIDE: True`)
- Marks visited path with `•`
- `HIDE` option to solve silently

---

## 🚀 Usage

### Generate a Maze
```python
from Maze import Maze, Color
from Maze_Generator import Maze_Generator

# Create a maze
maze = Maze(
    width=31, height=17,
    entry=(0, 0), exit=(30, 16),
    color={...}  # colors for each cell type
)

# Generate with Hunt and Kill
generator = Maze_Generator()
config = {
    "WIDTH": 31, "HEIGHT": 17,
    "ENTRY": (0, 0), "EXIT": (30, 16),
    "PERFECT": True, "SEED": 42
}
generator.hunt_and_kill(maze, config)

# Display
print(maze.show_maze())
```

### Solve a Maze
```python
from resolution import resolution

config = {
    "WIDTH": 31, "HEIGHT": 17,
    "EXIT": (30, 16), "ENTRY": (0, 0),
    "HIDE": False  # True for no animation
}

path = resolution(maze, config)
print(f"Solution: {path}")
```

---

## 🎨 Color Display

Mazes are displayed in color in the terminal using ANSI codes. Example:
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

## ⚙️ Technical Details

### Parity and Perfect Mazes
The algorithm handles **parity** (even/odd) of coordinates to ensure:
- No cell is isolated
- There is a unique path between any two points
- Geometric constraints are respected

### "42" Logo
If the maze is large enough (>9×7), a "42" logo is inserted in the center as a restricted area (impossible to traverse).

### Performance
- Real-time generation with 25 Hz refresh rate
- Animated solving with 0.05s steps
- Optimized for moderate-sized grids

---

## 📋 File Summary

| File | Role |
|------|------|
| `Maze.py` | Maze representation and manipulation |
| `Maze_Generator.py` | Generation by Hunt and Kill algorithm |
| `resolution.py` | Solving by backtracking |
| `__init__.py` | Package initialization |
