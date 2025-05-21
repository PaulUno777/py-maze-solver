from maze import Maze
from window import Window

# Constants
WINDOW_WIDTH = 900
WINDOW_HEIGHT = 700
CELL_SIZE = 50
SPACING = 50
COLS = 16
ROWS = 12


def main():
    win = Window(WINDOW_WIDTH, WINDOW_HEIGHT)
    maze = Maze(SPACING, SPACING, ROWS, COLS, CELL_SIZE, CELL_SIZE, win, 5)
    maze.solve()
    win.await_for_close()

if __name__ == "__main__":
    main()