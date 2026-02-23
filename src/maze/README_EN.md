# 🦆 Maze Module - Complete Guide

## 📋 Overview

The `maze` module is the heart of the program. It contains all the logic to create, manipulate, generate and solve mazes. The module consists of three main files that work together.

---

## 📁 File Structure

### 1. **maze.py** - The Foundations of the Maze

This file defines the base classes and enumerations that represent a maze.

#### 🎨 Class `Color` (Enumeration)
Contains all ANSI color codes for displaying the maze in color in the terminal.
- **Simple colors** : RED, GREEN, YELLOW, BLUE, etc.
- **Advanced colors** : Orange, Coral, Lime, Brown, etc.
- **Reset** : `RESET` to return to default color

#### 🧱 Class `Cell` (Enumeration)
Represents each possible type of cell in the maze:
- `ENTRY` ("E") : Maze entry point
- `EXIT` ("X") : Exit point to reach
- `BLANK` (" ") : Empty path where you can move
- `WALL` ("█") : Impassable barrier
- `STRICT` ("▒") : Restricted/logo area (cannot be modified)
- `SOLVE` ("•") : Marks the solution path

#### 🎭 Class `Maze` - The Heart of the System

This is the main class that represents a complete maze.

**Main Attributes:**
- `width` and `height` : Maze dimensions
- `entry` and `exit` : Coordinates of entry and exit points
- `maze` : Dictionary storing each cell and its type
- `color` : Color palette used for display
- `key` : Current graphical theme (how to display cells)

**Available Themes:**
- **Default** : Simple characters (E, X, █, etc.)
- **Cubic** : Colored square emojis
- **Emojis** : Varied emojis (doors, bricks, etc.)
- **Animal** : Animals (seal, dinosaur, etc.)

**Important Methods:**

| Method | Description |
|--------|-------------|
| `change_cell(cell, val)` | Modifies the type of a cell (if editable) |
| `is_editable(cell)` | Checks if a cell can be modified |
| `put_logo()` | Adds the "42" logo to the center of the maze |
| `clean_maze()` | Resets all paths to walls |
| `clean_path()` | Erases the displayed solution |
| `show_maze()` | Displays the maze formatted with colors and borders |
| `change_keys(key)` | Changes the graphical theme |

**Usage Example:**
```python
# Create a 20x20 maze
maze = Maze(20, 20, (1, 1), (18, 18), colors)

# View the maze
print(maze.show_maze())

# Change the theme
maze.change_keys("Emojis")
```

---

### 2. **generation.py** - Maze Creation

This file contains the algorithm to **automatically generate** a perfect maze.

#### 🎲 Function `hunt_and_kill(maze, config)`

This is the main generation algorithm. It works in two alternating phases:

**Phase 1 - "Kill" (Kill the Path)**
- Starts from the current cell
- Randomly explores unvisited neighboring cells
- Creates a path by breaking walls
- Stops when there are no more neighbors to explore (dead end)

**Phase 2 - "Hunt" (Hunt)**
- Scans the entire grid to find an unvisited cell
- That is adjacent to an already visited cell
- Connects these two cells together
- Restarts the "Kill" phase from this new cell

This algorithm guarantees that:
✅ Every cell in the maze is accessible
✅ There is only one path between any two points
✅ There are no loops or unnecessary passages

**Required Configuration (config):**
```python
config = {
    "WIDTH": 20,          # Maze width
    "HEIGHT": 20,         # Maze height
    "ENTRY": (1, 1),      # Entry coordinates
    "EXIT": (18, 18),     # Exit coordinates
    "PERFECT": True,      # Generate a perfect maze
    "SEED": 12345         # (Optional) Random seed
}
```

**Special Features:**
- 🎬 **Real-time Display** : Watch the maze generate step by step
- 🔒 **Parity Logic** : Ensures the exit is always reachable
- 🎨 **Smooth Animation** : Uses `Live` from the `rich` library for display

**Usage Example:**
```python
from src.maze.generation import hunt_and_kill

hunt_and_kill(maze, config)
# The maze is modified in-place
```

---

### 3. **resolution.py** - Maze Solving

This file contains the algorithm to **find the path** from start to finish.

#### 🧭 Function `resolution(maze, config)`

Uses a **recursive backtracking** algorithm to explore the maze.

**How It Works:**
1. Starts from the entry point (`ENTRY`)
2. Tries each possible direction (intelligently ordered)
3. Marks visited cells with the "•" symbol (`SOLVE`)
4. If a direction leads nowhere (dead end), backtracks and tries another
5. Stops when the exit (`EXIT`) is found

**Smart Optimization - The `get_directions(pos)` Function:**
- Instead of exploring randomly, it **prioritizes directions toward the exit**
- Calculates remaining distance to the target
- Explores directions that reduce this distance first
- Greatly speeds up the solving process

**Required Configuration (config):**
```python
config = {
    "WIDTH": 20,        # Maze width
    "HEIGHT": 20,       # Maze height
    "ENTRY": (1, 1),    # Starting point
    "EXIT": (18, 18),   # Exit point
    "HIDE": False       # False = animation, True = fast without display
}
```

**Return Value:**
Returns a string representing the path:
- `"N"` = North (up, y-1)
- `"S"` = South (down, y+1)
- `"E"` = East (right, x+1)
- `"W"` = West (left, x-1)

Example: `"EESSWWNNEE"` = Right, Right, Down, Down, Left, Left, Up, Up, Right, Right

**Usage Example:**
```python
from src.maze.resolution import resolution

path = resolution(maze, config)
print(f"Path found: {path}")
```

---

## 🔄 Complete Workflow

Here's how the three files work together:

```
1. Create a Maze object (maze.py)
   ↓
2. Generate the maze with hunt_and_kill (generation.py)
   ↓
3. Solve the maze with resolution (resolution.py)
   ↓
4. Display the solved maze (maze.py)
```

**Complete Example:**
```python
from src.maze.maze import Maze
from src.maze.generation import hunt_and_kill
from src.maze.resolution import resolution

# Step 1: Creation
config = {
    "WIDTH": 25,
    "HEIGHT": 25,
    "ENTRY": (1, 1),
    "EXIT": (23, 23),
    "PERFECT": True
}

maze = Maze(25, 25, (1, 1), (23, 23), colors)

# Step 2: Generation
hunt_and_kill(maze, config)

# Step 3: Resolution
path = resolution(maze, config)

# Step 4: Display
print(maze.show_maze())
print(f"Solution: {path}")
```

---

## 🎯 Key Points to Remember

| Aspect | Explanation |
|--------|------------|
| **Cells** | Each point in the maze is a cell with a type (wall, path, etc.) |
| **Grid** | The maze is stored in a dictionary of (x, y) coordinates |
| **Generation** | The "Hunt and Kill" algorithm creates perfect mazes (always has a solution) |
| **Resolution** | Recursive backtracking finds the shortest path |
| **Optimization** | Heuristics (prioritizing directions) make everything faster |
| **Display** | Each cell has a color and symbol configurable via themes |
| **Logo** | The famous "42" logo is automatically placed in the center if space allows |

