# tests.py
import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1.cells),
            num_cols,
        )
        self.assertEqual(
            len(m1.cells[0]),
            num_rows,
        )
        num_cols = 30
        num_rows = 30
        m2 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m2.cells),
            num_cols,
        )
        self.assertEqual(
            len(m2.cells[0]),
            num_rows,
        )
    def test_entrance_and_exit_broken(self):
        m4 = Maze(0, 0, 4, 4, 10, 10)
        entrance = m4.cells[0][0]
        exit_cell = m4.cells[3][3]
        self.assertFalse(entrance.has_top_wall)
        self.assertFalse(exit_cell.has_bottom_wall)

    def test_cells_not_visited(self):
        m5 = Maze(0, 0, 15, 15, 10, 10)
        for col in range(len(m5.cells)):
            for row in range(len(m5.cells[col])):
                self.assertFalse(m5.cells[col][row].visited)

    

if __name__ == "__main__":
    unittest.main()