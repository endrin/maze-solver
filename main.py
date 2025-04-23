import time

from maze import Maze
from window import Window


def main():
    win = Window(800, 600)
    maze = Maze(10, 10, 20, 20, 39, 29, win)
    maze.draw_cells()
    maze._break_entrance_and_exit()
    maze._break_walls_r(0, 0)
    maze._reset_cells_visited()

    time.sleep(1)
    maze.solve()

    win.wait_for_close()


if __name__ == "__main__":
    main()
