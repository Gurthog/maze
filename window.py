from tkinter import Tk, BOTH, Canvas

from line import Line


class Window:
    def __init__(self, width, height) -> None:
        self.root = Tk()
        self.root.title = "Maze Buddy"
        self.canvas = Canvas(self.root, bg="white", width=width, height=height)
        self.canvas.pack()

    def draw_line(self, line: Line, fill_color: str="black") -> None:
        line.draw(self.canvas, fill_color)

    def redraw(self) -> None:
        self.root.update_idletasks()
        self.root.update()

    def reset_canvas(self) -> None:
        self.canvas.delete("all")

