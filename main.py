from shapes import Line, Point
from window import Window


def main():
    win = Window(800, 600)
    win.draw_line(Line(Point(50, 50), Point(750, 550)), "black")
    win.draw_line(Line(Point(750, 50), Point(50, 550)), "blue")
    win.wait_for_close()


if __name__ == "__main__":
    main()
