from line import Line
from point import Point
from window import Window


class Cell:
    def __init__(self, window: Window) -> None:
        self.left = True
        self.right = True
        self.top = True
        self.bottom = True
        self.__x1 = -1
        self.__y1 = -1
        self.__x2 = -1
        self.__y2 = -1
        self.__win = window

    def center(self) -> Point:
        return Point(
            abs(self.__x2 - self.__x1) / 2 + self.__x1,
            abs(self.__y2 - self.__y1) / 2 + self.__y1,
        )

    def draw(self, x1, y1, x2, y2) -> None:
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        top_left = Point(self.__x1, self.__y1)
        top_right = Point(self.__x2, self.__y1)
        bottom_left = Point(self.__x1, self.__y2)
        bottom_right = Point(self.__x2, self.__y2)

        if self.left:
            line = Line(top_left, bottom_left)
            self.__win.draw_line(line)
        if self.right:
            line = Line(top_right, bottom_right)
            self.__win.draw_line(line)
        if self.top:
            line = Line(top_left, top_right)
            self.__win.draw_line(line)
        if self.bottom:
            line = Line(bottom_left, bottom_right)
            self.__win.draw_line(line)

    def draw_move(self, to_cell, undo=False) -> None:
        line = Line(self.center(), to_cell.center())
        color = "gray" if undo else "red"
        self.__win.draw_line(line, color)
