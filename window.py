from tkinter import Tk, BOTH, Canvas

from line import Line


class Window:
    def __init__(self, width, height) -> None:
        self.root = Tk()
        self.root.title = "Maze Buddy"
        self.canvas = Canvas(self.root, width=width, height=height)
        self.canvas.pack()
        self.running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self) -> None:
        self.root.update_idletasks()
        self.root.update()
    
    def wait_for_close(self) -> None:
        self.running = True
        while self.running:
            self.redraw()
    
    def close(self) -> None:
        self.running = False

    def draw_line(self, line: Line, fill_color: str="black") -> None:
        line.draw(self.canvas, fill_color)
