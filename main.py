from geometry import Cell
from maze import Maze
from window import Window


def main():
    win = Window(900, 700)
    maze = Maze(50, 50, 12, 16, 50, 50, win, 4)
    maze.solve()
    win.await_for_close()

if __name__ == "__main__":
    main()