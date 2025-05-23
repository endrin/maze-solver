from dataclasses import astuple, dataclass, field
from tkinter import Canvas
from typing import Self

from shapes import Line, Point


@dataclass
class Walls:
    top: bool = True
    right: bool = True
    bottom: bool = True
    left: bool = True


@dataclass
class Cell:
    top_left: Point
    bottom_right: Point
    walls: Walls = field(default_factory=Walls)
    visited: bool = False

    @property
    def center(self) -> Point:
        return Point(
            (self.top_left.x + self.bottom_right.x) // 2,
            (self.top_left.y + self.bottom_right.y) // 2,
        )

    @property
    def has_left_wall(self) -> bool:
        return self.walls.left

    @property
    def has_right_wall(self) -> bool:
        return self.walls.right

    @property
    def has_top_wall(self) -> bool:
        return self.walls.top

    @property
    def has_bottom_wall(self) -> bool:
        return self.walls.bottom

    @property
    def __top_wall(self) -> tuple[int, int, int, int] | None:
        if self.has_top_wall:
            return (
                self.top_left.x,
                self.top_left.y,
                self.bottom_right.x,
                self.top_left.y,
            )

    @property
    def __right_wall(self) -> tuple[int, int, int, int] | None:
        if self.has_right_wall:
            return (
                self.bottom_right.x,
                self.top_left.y,
                self.bottom_right.x,
                self.bottom_right.y,
            )

    @property
    def __bottom_wall(self) -> tuple[int, int, int, int] | None:
        if self.has_bottom_wall:
            return (
                self.top_left.x,
                self.bottom_right.y,
                self.bottom_right.x,
                self.bottom_right.y,
            )

    @property
    def __left_wall(self) -> tuple[int, int, int, int] | None:
        if self.has_left_wall:
            return (
                self.top_left.x,
                self.top_left.y,
                self.top_left.x,
                self.bottom_right.y,
            )

    def has_wall_at(self, di, dj):
        match (di, dj):
            case (1, 0):
                return self.has_bottom_wall
            case (0, 1):
                return self.has_right_wall
            case (-1, 0):
                return self.has_top_wall
            case (0, -1):
                return self.has_left_wall
            case _:
                f"attempt to get wall in wrong direction: ({di}, {dj})"

    def draw(self, canvas: Canvas, fill_color: str, update=False):
        walls = (
            w
            for w in (
                self.__top_wall,
                self.__right_wall,
                self.__bottom_wall,
                self.__left_wall,
            )
            if w is not None
        )
        for wall in walls:
            canvas.create_line(*wall, fill=fill_color, width=2)

        if update:
            missing_walls = tuple((not w) for w in astuple(self.walls))
            inverted = Cell(
                self.top_left,
                self.bottom_right,
                Walls(*missing_walls),
            )
            inverted.draw(canvas, fill_color=canvas["background"], update=False)

    def get_move(
        self,
        to_cell: Self,
    ) -> Line:
        return Line(self.center, to_cell.center)
