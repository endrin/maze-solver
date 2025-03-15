import time
from maze import Maze
from window import Window


def main():
    win = Window(800, 600)
    maze = Maze(0, 0, 10, 10, 80, 60, win)
    maze.draw_cells()
    time.sleep(1)
    maze._break_entrance_and_exit()

    win.wait_for_close()


if __name__ == "__main__":
    main()
