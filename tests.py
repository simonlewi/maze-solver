import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells), 
            num_rows,
        )
        self.assertEqual(
            len(m1._cells[0]), 
            num_cols,
        )


    def test_empty_maze(self):
        # Test zero rows
        m1 = Maze(0, 0, 0, 0, 10, 10)
        self.assertEqual(
            len(m1._cells), 0)
        
        # Test zero columns
        m2 = Maze(0, 0, 0, 5, 10, 10)
        self.assertEqual(len(m2._cells), 0)
        for row in m2._cells:
            self.assertEqual(len(row), 0)


    def test_non_integer_dimensions_should_raise_error(self):
        # Rows as a float
        with self.assertRaises(TypeError):
            Maze(0, 0, 5.5, 10, 10, 10)
    
        # Columns as a string
        with self.assertRaises(TypeError):
            Maze(0, 0, 5, "10", 10, 10)


    def test_maze_break_entrance_and_exit(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            m1._cells[0][0].has_top_wall,
            False,
        )
        self.assertEqual(
            m1._cells[num_cols - 1][num_rows - 1].has_bottom_wall,
            False,
        )

    
    def test_maze_reset_cells_visited(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        for col in m1._cells:
            for cell in col:
                self.assertEqual(
                    cell.visited,
                    False,
                )

    
if __name__ == "__main__":
    unittest.main()