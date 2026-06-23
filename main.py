from time import sleep

from cell import Cell
from maze import Maze
from window import Window


def main():
    COLS = 20
    ROWS = 15
    CELL_SIZE = 40

    win = Window(COLS * CELL_SIZE, ROWS * CELL_SIZE)
    while True:
        win.reset_canvas()
        maze = Maze(COLS, ROWS, CELL_SIZE, win)
        maze.solve()
        sleep(1)


if __name__ == "__main__":
    main()

