import random
import time
from cell import Cell
from shapes import Point
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
        seed=None,
    ):
        self.start = Point(x1, y1)
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win

        if seed is not None:
            random.seed(seed)

        self._create_cells()

    def _create_cells(self):
        self._cells = [
            [
                self._cell_at(col, row, self.cell_size_x, self.cell_size_y)
                for col in range(self.num_cols)
            ]
            for row in range(self.num_rows)
        ]

    def _draw_cell(self, i, j, update=False):
        wall_color = "SeaGreen3" if not update else "dark violet"
        self.win.draw_cell(self._cells[i][j], wall_color, update)

    def draw_cells(self):
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self._draw_cell(i, j)
        self._animate()

    def _animate(self):
        self.win.redraw()
        time.sleep(0.05)

    def _reset_cells_visited(self):
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self._cells[i][j].visited = False

    def _break_entrance_and_exit(self):
        self._cells[0][0].walls.top = False
        self._draw_cell(0, 0, update=True)
        self._cells[-1][-1].walls.bottom = False
        self._draw_cell(-1, -1, update=True)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            visit_next = []
            for di, dj in ((0, -1), (0, 1), (1, 0), (-1, 0)):
                i1 = i + di
                j1 = j + dj
                if i1 < 0 or i1 >= self.num_rows:
                    continue
                if j1 < 0 or j1 >= self.num_cols:
                    continue
                if self._cells[i1][j1].visited:
                    continue
                visit_next.append((i1, j1))

            if not visit_next:
                self._draw_cell(i, j, update=True)
                self._animate()
                return
            next_i, next_j = random.choice(visit_next)
            self._break_wall(i, j, next_i, next_j)
            self._break_walls_r(next_i, next_j)

    def _break_wall(self, from_i, from_j, to_i, to_j):
        match (to_i - from_i, to_j - from_j):
            case (-1, 0):
                self._cells[from_i][from_j].walls.top = False
                self._cells[to_i][to_j].walls.bottom = False
            case (1, 0):
                self._cells[from_i][from_j].walls.bottom = False
                self._cells[to_i][to_j].walls.top = False
            case (0, -1):
                self._cells[from_i][from_j].walls.left = False
                self._cells[to_i][to_j].walls.right = False
            case (0, 1):
                self._cells[from_i][from_j].walls.right = False
                self._cells[to_i][to_j].walls.left = False
            case _:
                raise RuntimeError(
                    f"attempt to break wall for incompatible cells: ({from_i}, {from_j}) -> ({to_i}, {to_j})"
                )

    def _cell_at(self, x_pos: int, y_pos: int, x_size: int, y_size: int) -> Cell:
        x = self.start.x + x_pos * x_size
        y = self.start.y + y_pos * y_size
        return Cell(Point(x, y), Point(x + x_size, y + y_size))
