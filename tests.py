import unittest

from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        cols = 12
        rows = 10
        cell_size = 10
        m1 = Maze(cols, rows, cell_size)
        self.assertEqual(
                len(m1.cells),
                cols,
        )
        self.assertEqual(
                len(m1.cells[0]),
                rows,
        )


if __name__ == "__main__":
    unittest.main()

