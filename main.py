from cell import Cell
from maze import Maze
from window import Window


def main():
    win = Window(800, 600)
    maze = Maze(win, 15, 10, 45)
    start = maze.cells[2][2]
    end = maze.cells[8][8]
    start.draw_move(end)

    win.wait_for_close()


if __name__ == "__main__":
    main()
