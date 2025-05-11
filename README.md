# Maze Solver

A Python application that generates and solves mazes using a depth-first search algorithm with visual representation.

## Features

- Random maze generation using recursive backtracking
- Visual representation of maze generation process
- Automatic maze solving with visual path finding
- Adjustable animation speeds for generation and solving
- Configurable maze dimensions

## Prerequisites

- Python 3.x
- Tkinter (pre-installed on Windows/macOS)
  - Linux users: See installation instructions below

### Installing Tkinter on Linux
Depending on your distribution:
- Ubuntu/Debian: `sudo apt-get install python3-tk`
- Fedora: `sudo dnf install python3-tkinter`
- Arch Linux: `sudo pacman -S tk`

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/maze-solver.git
cd maze-solver
```

2. No additional dependencies need to be installed as the project uses Python standard library.

## Usage

Run the main script:

```bash
python main.py
```

The application will:
1. Create a window showing the maze generation process
2. Generate a random maze with an entrance at the top-left and exit at the bottom-right
3. Solve the maze, displaying the solution path

### Configuration

You can modify the following parameters in the code:

- Maze dimensions: Adjust `num_rows` and `num_cols` in the Maze constructor
- Animation speed: 
  - Generation speed: Modify `self._generation_speed` (default: 0.01)
  - Solving speed: Modify `self._solving_speed` (default: 0.05)
- Cell size: Adjust `cell_size_x` and `cell_size_y` in the Maze constructor

## How It Works

1. **Maze Generation**: Uses a recursive backtracking algorithm to:
   - Start from the top-left cell
   - Randomly choose unvisited neighboring cells
   - Break walls between cells to create paths
   - Continue until all cells are visited

2. **Maze Solving**: Implements a depth-first search algorithm to:
   - Start from the entrance (top-left)
   - Explore possible paths until reaching the exit (bottom-right)
   - Backtrack from dead ends
   - Display the final solution path

## Contributing

Feel free to open issues or submit pull requests with improvements.

## License

This project is licensed under the MIT License - see the LICENSE file for details.