
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Point(self.x * scalar, self.y * scalar)

    def __truediv__(self, scalar):
        return Point(self.x / scalar, self.y / scalar)
    
class Line:
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end

    def draw(self, canvas, fill="black", width=2):
        canvas.create_line(self.start.x, self.start.y, self.end.x, self.end.y, fill=fill, width=width)

    def __repr__(self):
        return f"Line({self.start}, {self.end})"

    def length(self):
        return ((self.end.x - self.start.x) ** 2 + (self.end.y - self.start.y) ** 2) ** 0.5
    
class Cell:
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_top_wall = True
        self.has_right_wall = True
        self.has_bottom_wall = True
        self.__x1 = -1
        self.__y1 = -1
        self.__x2 = -1
        self.__y2 = -1
        self.__win = win
        self.visited = False

    def draw(self, x1, y1, x2, y2, color="black"):
        # Update coordinates
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

        if not self.__win:
            return
        
        canvas_bg = self.__win.canvas["background"]

        # Drawing or "erasing" each wall
        if self.has_left_wall:
            self.__win.draw_line(Line(Point(x1, y1), Point(x1, y2)), "black")
        else:
            self.__win.draw_line(Line(Point(x1, y1), Point(x1, y2)), canvas_bg)

        if self.has_top_wall:
            self.__win.draw_line(Line(Point(x1, y1), Point(x2, y1)), "black")
        else:
            self.__win.draw_line(Line(Point(x1, y1), Point(x2, y1)), canvas_bg)

        if self.has_right_wall:
            self.__win.draw_line(Line(Point(x2, y1), Point(x2, y2)), "black")
        else:
            self.__win.draw_line(Line(Point(x2, y1), Point(x2, y2)), canvas_bg)

        if self.has_bottom_wall:
            self.__win.draw_line(Line(Point(x1, y2), Point(x2, y2)), "black")
        else:
            self.__win.draw_line(Line(Point(x1, y2), Point(x2, y2)), canvas_bg)
    
    def draw_move(self, to_cell, undo=False):
        color = "gray" if undo else "red"

        # Current cell center
        from_x = (self.__x1 + self.__x2) // 2
        from_y = (self.__y1 + self.__y2) // 2

        # Target cell center
        to_x = (to_cell.__x1 + to_cell.__x2) // 2
        to_y = (to_cell.__y1 + to_cell.__y2) // 2
        self.__win.draw_line(Line(Point(from_x, from_y), Point(to_x, to_y)), color)