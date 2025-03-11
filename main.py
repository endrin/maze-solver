from shapes import Cell, Line, Point, Walls
from window import Window


def main():
    win = Window(800, 600)
    win.draw_line(Line(Point(50, 50), Point(750, 550)), "black")
    win.draw_line(Line(Point(750, 50), Point(50, 550)), "blue")
    win.draw_cell(
        Cell(Point(100, 150), Point(150, 200), Walls(True, True, False, True)),
        "tomato2",
    )
    win.draw_cell(
        Cell(Point(100, 200), Point(150, 250), Walls(False, False, True, True)),
        "tomato3",
    )
    win.draw_cell(
        Cell(Point(150, 200), Point(200, 250), Walls(True, True, False, False)),
        "tomato4",
    )
    win.draw_cell(
        Cell(Point(150, 250), Point(200, 300), Walls(False, True, True, False)),
        "OrangeRed2",
    )
    win.draw_cell(
        Cell(Point(100, 250), Point(150, 300), Walls(True, False, True, True)),
        "OrangeRed3",
    )

    win.draw_cell_move(
        Cell(Point(100, 150), Point(150, 200), Walls(True, True, False, True)),
        Cell(Point(100, 200), Point(150, 250), Walls(False, False, True, True)),
    )
    win.draw_cell_move(
        Cell(Point(100, 200), Point(150, 250), Walls(False, False, True, True)),
        Cell(Point(150, 200), Point(200, 250), Walls(True, True, False, False)),
        undo=True,
    )

    win.wait_for_close()


if __name__ == "__main__":
    main()
