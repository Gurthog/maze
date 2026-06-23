from time import sleep

from cell import Cell
from window import Window


class Maze:
    def __init__(
            self,
            cols: int,
            rows: int,
            cell_size: int,
            win: Window = None,
    ) -> None:
        self.win = win
        self.cols = cols
        self.rows = rows
        self.cells = self.create_cells(cols, rows, cell_size)
        self.break_entrance_and_exit()

    def break_entrance_and_exit(self):
        self.cells[0][0].top = False
        self.cells[0][0].draw()
        self.cells[-1][-1].bottom = False
        self.cells[-1][-1].draw()

        if not self.win:
            return

        self.win.redraw()

    def create_cells(self, cols, rows, cell_size) -> list[list[Cell]]:
        cells = []
        for x in range(cols):
            col = []
            for y in range(rows):
                cell = self.create_cell(x, y, cell_size)
                col.append(cell)
            cells.append(col)
        return cells

    def create_cell(self, col, row, size) -> Cell:
        col_x = col * size
        row_y = row * size
        top_left = (col_x, row_y)
        bottom_right = (col_x + size, row_y + size)

        cell = Cell(self.win)
        cell.set_location(*top_left, *bottom_right)
        cell.draw()
        self.animate()
        return cell

    def animate(self) -> None:
        if not self.win:
            return

        animation_seconds = 1
        frame_time = animation_seconds / (self.cols * self.rows)
        self.win.redraw()
        sleep(frame_time)

