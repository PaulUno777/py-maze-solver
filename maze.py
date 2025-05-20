from asyncio import sleep
import random
from geometry import Cell


class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win = None,
        seed = None,
    ):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win

        # Create a grid of cells
        self.__cells = []
        self.__create_cells()
        self.__break_entrance_and_exit()
        if seed is not None:
           self.seed = random.seed(seed)
        self.__break_walls_r(0, 0)
        self.__reset_cells_visited()

    def __create_cells(self):
        # Create cells
        for col in range(self.__num_cols):
            col_cells = []
            for row in range(self.__num_rows):
                cell = Cell(self.__win)
                col_cells.append(cell)
            self.__cells.append(col_cells)

        # Draw each cell
        for col in range(self.__num_cols):
            for row in range(self.__num_rows):
                self.__draw_cell(col, row)

    def __draw_cell(self, i, j):
        x1 = self.__x1 + i * self.__cell_size_x
        y1 = self.__y1 + j * self.__cell_size_y
        x2 = x1 + self.__cell_size_x
        y2 = y1 + self.__cell_size_y
        cell = self.__cells[i][j]
        cell.draw(x1, y1, x2, y2)
        self.__animate()

    def __animate(self):
        if not self.__win:
            return
        # Animate the drawing of the cell
        self.__win.redraw()
        sleep(0.35)

    def __break_entrance_and_exit(self):
         # Entrance: top-left cell (0, 0)
        entrance = self.__cells[0][0]
        entrance.has_top_wall = False
        self.__draw_cell(0, 0)

        # Exit: bottom-right cell
        last_col = self.__num_cols - 1
        last_row = self.__num_rows - 1
        exit_cell = self.__cells[last_col][last_row]
        exit_cell.has_bottom_wall = False
        self.__draw_cell(last_col, last_row)
    
    def __break_walls_r(self, i, j):
        current = self.__cells[i][j]
        current.visited = True

        while True:
            directions = []
            # Check each direction
            if i > 0 and not self.__cells[i - 1][j].visited:
                directions.append(("left", i - 1, j))

            if i < self.__num_cols - 1 and not self.__cells[i + 1][j].visited:
                directions.append(("right", i + 1, j))

            if j > 0 and not self.__cells[i][j - 1].visited:
                directions.append(("up", i, j - 1))

            if j < self.__num_rows - 1 and not self.__cells[i][j + 1].visited:
                directions.append(("down", i, j + 1))

            if not directions:
                self.__draw_cell(i, j)
                return

            direction, ni, nj = random.choice(directions)
            next_cell = self.__cells[ni][nj]

            # Break wall between current and next
            if direction == "left":
                current.has_left_wall = False
                next_cell.has_right_wall = False
            elif direction == "right":
                current.has_right_wall = False
                next_cell.has_left_wall = False
            elif direction == "up":
                current.has_top_wall = False
                next_cell.has_bottom_wall = False
            elif direction == "down":
                current.has_bottom_wall = False
                next_cell.has_top_wall = False

            # Recurse
            self.__break_walls_r(ni, nj)

    def __reset_cells_visited(self):
        for col in range(self.__num_cols):
            for row in range(self.__num_rows):
                self.__cells[col][row].visited = False

    def solve(self):
        self.__solve_r(0, 0) # Start solving from the entrance cell (0, 0)

    def __solve_r(self, i, j):
        self.__animate()
        current = self.__cells[i][j]
        current.visited = True

        # Goal check
        if i == self.__num_cols - 1 and j == self.__num_rows - 1:
            return True

        # Try all 4 directions
        directions = [
            ("left", i - 1, j, current.has_left_wall),
            ("right", i + 1, j, current.has_right_wall),
            ("up", i, j - 1, current.has_top_wall),
            ("down", i, j + 1, current.has_bottom_wall),
        ]

        for direction, ni, nj, has_wall in directions:
            if 0 <= ni < self.__num_cols and 0 <= nj < self.__num_rows:
                next_cell = self.__cells[ni][nj]
                if not has_wall and not next_cell.visited:
                    current.draw_move(next_cell)
                    if self.__solve_r(ni, nj):
                        return True
                    current.draw_move(next_cell, undo=True)

        return False

    @property
    def cells(self):
        return self.__cells