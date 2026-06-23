import unittest

from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        cols = 12
        rows = 10
        cell_size = 10
        maze = Maze(cols, rows, cell_size)

        self.assertEqual(
                len(maze.cells),
                cols,
        )
        self.assertEqual(
                len(maze.cells[0]),
                rows,
        )

    def test_maze_reset_visited(self):
        cols = 10
        rows = 10
        cell_size = 10
        maze = Maze(cols, rows, cell_size)

        any_visited = False
        for col in maze.cells:
            for cell in col:
                if cell.visited:
                    any_visited = True
        self.assertEqual(any_visited, False)


if __name__ == "__main__":
    unittest.main()

