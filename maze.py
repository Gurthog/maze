import random
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
            seed: int = None,
    ) -> None:
        self.win = win
        self.cols = cols
        self.rows = rows
        self.cells = self.create_cells(cols, rows, cell_size)
        self.break_entrance_and_exit()
        if seed:
            random.seed(seed)
        self.break_walls()
        self.reset_visited()

    def animate(self, duration=0.5) -> None:
        if not self.win:
            return

        frame_time = duration / (self.cols * self.rows)
        self.win.redraw()
        sleep(frame_time)

    def break_entrance_and_exit(self) -> None:
        self.cells[0][0].top = False
        self.cells[0][0].draw()
        self.cells[-1][-1].bottom = False
        self.cells[-1][-1].draw()

        if not self.win:
            return

        self.win.redraw()

    def break_walls(self, col=0, row=0) -> None:
        """recursive wall break"""
        current_cell = self.cells[col][row]
        current_cell.visited = True

        while True:
            unvisited = self.unvisited_neighbors(col, row)
            if len(unvisited) == 0:
                current_cell.draw()
                self.animate()
                break

            # pick random direction, knock down walls between this/that
            next_col, next_row = random.choice(unvisited)
            next_cell = self.cells[next_col][next_row]
            if next_col < col:
                current_cell.left = False
                next_cell.right = False
            if next_col > col:
                current_cell.right = False
                next_cell.left = False
            if next_row < row:
                current_cell.top = False
                next_cell.bottom = False
            if next_row > row:
                current_cell.bottom = False
                next_cell.top = False
            self.break_walls(next_col, next_row)

    def can_move(self, col, row, next_col, next_row) -> bool:
        current_cell = self.cells[col][row]
        next_cell = self.cells[next_col][next_row]
        if next_col < col and not current_cell.left and not next_cell.right:
            return True
        if next_col > col and not current_cell.right and not next_cell.left:
            return True
        if next_row < row and not current_cell.top and not next_cell.bottom:
            return True
        if next_row > row and not current_cell.bottom and not next_cell.top:
            return True
        return False

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
        col_x = col * size + 1
        row_y = row * size + 1
        top_left = (col_x, row_y)
        bottom_right = (col_x + size, row_y + size)

        cell = Cell(self.win)
        cell.set_location(*top_left, *bottom_right)
        cell.draw()
        self.animate()
        return cell

    def reset_visited(self) -> None:
        for col in self.cells:
            for cell in col:
                cell.visited = False

    def solve(self, col=0, row=0) -> bool:
        speed = 5
        current_cell = self.cells[col][row]
        current_cell.visited = True
        if current_cell is self.cells[-1][-1]:
            return True

        unvisited = self.unvisited_neighbors(col, row)
        for next_col, next_row in unvisited:
            next_cell = self.cells[next_col][next_row]
            if self.can_move(col, row, next_col, next_row):
                current_cell.draw_move(next_cell)
                self.animate(speed)
                solved = self.solve(next_col, next_row)
                if solved:
                    return True
                current_cell.draw_move(next_cell, undo=True)
                self.animate(speed)
        return False

    def unvisited_neighbors(self, col, row) -> list[tuple[int, int]]:
        unvisited = []
        # left
        if col > 0 and not self.cells[col-1][row].visited:
            unvisited.append((col - 1, row))
        # right
        if col < self.cols - 1 and not self.cells[col+1][row].visited:
            unvisited.append((col + 1, row))
        # top
        if row > 0 and not self.cells[col][row-1].visited:
            unvisited.append((col, row - 1))
        # bottom
        if row < self.rows - 1 and not self.cells[col][row+1].visited:
            unvisited.append((col, row + 1))
        return unvisited

