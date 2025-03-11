from tkinter import Tk, BOTH, Canvas

from shapes import Cell, Line


class Window:
    def __init__(self, width, height):
        self.root = Tk()
        self.root.title = "Maze Solver"
        self.canvas = Canvas(
            master=self.root, bg="lemon chiffon", width=width, height=height
        )
        self.canvas.pack(fill=BOTH, expand=1)
        self.running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    def close(self):
        self.running = False

    def draw_line(self, line: Line, fill_color: str):
        line.draw(self.canvas, fill_color)

    def draw_cell(self, cell: Cell, fill_color: str):
        cell.draw(self.canvas, fill_color)

    def draw_cell_move(self, from_cell: Cell, to_cell, *, undo=False):
        fill_color = "red" if undo else "black"  # TODO: un-hardcode the values
        from_cell.get_move(to_cell).draw(self.canvas, fill_color)
