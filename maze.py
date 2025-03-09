from cell import Cell
import random
import time

class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            _win=None,
            seed=None
    ):
        if not isinstance(num_rows, int) or not isinstance(num_cols, int):
            raise TypeError("Number of rows and columns must be integers.")
        if num_rows < 0 or num_cols < 0:
            raise ValueError("Number of rows and columns must be non-negative.")
        
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = _win
        if seed:
            random.seed(seed)

        self._generation_speed = 0.01  # faster speed for generation
        self._solving_speed = 0.05 # slower speed for solving
        self._create_cells()
        self._break_entrance_and_exit
        self._break_walls_r(0, 0)

    def _create_cells(self):
        for i in range(self._num_rows):
            row_cells = []
            for j in range(self._num_cols):
                row_cells.append(Cell(self._win))
            self._cells.append(row_cells)
        for i in range(self._num_rows):
            for j in range(self._num_cols):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        # Use different speeds for generation vs solving
        current_speed = self._solving_speed if hasattr(self, '_solving') else self._generation_speed
        time.sleep(current_speed)

    def _break_entrance_and_exit(self):
        # Break entrance
        self._cells[0][0].has_top_wall = False
        # Break exit
        self._cells[self._num_rows - 1][self._num_cols - 1].has_bottom_wall = False
        self._draw_cell(0, 0)
        self._draw_cell(self._num_rows - 1, self._num_cols - 1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        
        # Create list of unvisited neighbors
        next_index_list = []
        
        # Check right neighbor
        if i < self._num_cols - 1 and not self._cells[i + 1][j].visited:
            next_index_list.append((i + 1, j))
            
        # Check left neighbor
        if i > 0 and not self._cells[i - 1][j].visited:
            next_index_list.append((i - 1, j))
            
        # Check down neighbor
        if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:
            next_index_list.append((i, j + 1))
            
        # Check up neighbor
        if j > 0 and not self._cells[i][j - 1].visited:
            next_index_list.append((i, j - 1))
        
        # If no unvisited neighbors, we're done with this cell
        if len(next_index_list) == 0:
            return
            
        # Randomly choose the next cell to visit
        direction_index = random.randrange(len(next_index_list))
        next_index = next_index_list[direction_index]
        
        # Break walls between current cell and chosen next cell
        if next_index[0] == i + 1:  # right
            self._cells[i][j].has_right_wall = False
            self._cells[i + 1][j].has_left_wall = False
        elif next_index[0] == i - 1:  # left
            self._cells[i][j].has_left_wall = False
            self._cells[i - 1][j].has_right_wall = False
        elif next_index[1] == j + 1:  # down
            self._cells[i][j].has_bottom_wall = False
            self._cells[i][j + 1].has_top_wall = False
        elif next_index[1] == j - 1:  # up
            self._cells[i][j].has_top_wall = False
            self._cells[i][j - 1].has_bottom_wall = False
        
        # Recursively visit the next cell
        self._break_walls_r(next_index[0], next_index[1])

    def _reset_cells_visited(self):
        for i in range(self._num_rows):
            for j in range(self._num_cols):
                self._cells[i][j].visited = False

    def solve(self):
        self._reset_cells_visited()
        self._solving = True
        result = self._solve_r(0, 0)
        delattr(self, '_solving')  # Remove the flag when done
        if result:
            print("Maze solved!")
        else:
            print("Maze could not be solved")

    # Depth-first search algorithm
    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        
        # If we're at the end cell (bottom-right corner)
        if i == self._num_cols - 1 and j == self._num_rows - 1:
            return True
            
        # Try each direction: right, left, down, up
        # Check right
        if (i < self._num_cols - 1 and 
            not self._cells[i][j].has_right_wall and 
            not self._cells[i + 1][j].visited):
            self._cells[i][j].draw_move(self._cells[i + 1][j])
            if self._solve_r(i + 1, j):
                return True
            self._cells[i][j].draw_move(self._cells[i + 1][j], True)  # undo=True
        
        # Check left
        if (i > 0 and 
            not self._cells[i][j].has_left_wall and 
            not self._cells[i - 1][j].visited):
            self._cells[i][j].draw_move(self._cells[i - 1][j])
            if self._solve_r(i - 1, j):
                return True
            self._cells[i][j].draw_move(self._cells[i - 1][j], True)  # undo=True
        
        # Check down
        if (j < self._num_rows - 1 and 
            not self._cells[i][j].has_bottom_wall and 
            not self._cells[i][j + 1].visited):
            self._cells[i][j].draw_move(self._cells[i][j + 1])
            if self._solve_r(i, j + 1):
                return True
            self._cells[i][j].draw_move(self._cells[i][j + 1], True)  # undo=True
        
        # Check up
        if (j > 0 and 
            not self._cells[i][j].has_top_wall and 
            not self._cells[i][j - 1].visited):
            self._cells[i][j].draw_move(self._cells[i][j - 1])
            if self._solve_r(i, j - 1):
                return True
            self._cells[i][j].draw_move(self._cells[i][j - 1], True)  # undo=True
        
        return False
