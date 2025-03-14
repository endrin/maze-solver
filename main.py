from maze import Maze
from window import Window


def main():
    win = Window(800, 600)
    maze = Maze(0, 0, 10, 10, 80, 60, win)
    maze.draw_cells()

    win.wait_for_close()


if __name__ == "__main__":
    main()
