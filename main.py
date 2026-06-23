from cell import Cell
from maze import Maze
from window import Window


def main():
    COLS = 20
    ROWS = 15
    CELL_SIZE = 40

    win = Window(COLS * CELL_SIZE, ROWS * CELL_SIZE)
    maze = Maze(COLS, ROWS, CELL_SIZE, win)
    # start = maze.cells[2][2]
    # end = maze.cells[8][8]
    # start.draw_move(end)

    win.wait_for_close()


if __name__ == "__main__":
    main()

