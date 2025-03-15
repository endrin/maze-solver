import time
from shapes import Cell, Point
from window import Window


class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win: Window,
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._create_cells()

    def _create_cells(self):
        self._cells = [
            [
                _cell_at(row, col, self.cell_size_x, self.cell_size_y)
                for col in range(self.num_cols)
            ]
            for row in range(self.num_rows)
        ]

    def _draw_cell(self, i, j, update=False):
        self.win.draw_cell(self._cells[i][j], "SeaGreen3", update)

    def draw_cells(self):
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self._draw_cell(i, j)
        self._animate()

    def _animate(self):
        self.win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].walls.top = False
        self._draw_cell(0, 0, update=True)
        self._cells[-1][-1].walls.bottom = False
        self._draw_cell(-1, -1, update=True)


def _cell_at(x_pos: int, y_pos: int, x_size: int, y_size: int) -> Cell:
    x = x_pos * x_size
    y = y_pos * y_size
    return Cell(Point(max(x, 2), max(y, 2)), Point(x + x_size, y + y_size))
