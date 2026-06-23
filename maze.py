from time import sleep

from cell import Cell
from window import Window


class Maze:
    def __init__(
            self,
            win: Window,
            cols: int,
            rows: int,
            cell_size: int,
    ) -> None:
        self.win = win
        self.cells = self.create_cells(cols, rows, cell_size)
    
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
        cell.draw(*top_left, *bottom_right)
        self.animate()
        return cell
    
    def animate(self) -> None:
        self.win.redraw()
        sleep(0.02)
