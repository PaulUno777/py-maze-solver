from tkinter import Tk, BOTH, Canvas

from geometry import Line

class Window:
    def __init__(self, width: int, height: int):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.canvas = Canvas(self.__root, width=width, height=height)
        self.canvas.pack(fill=BOTH, expand=True)
        self.running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def await_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
        print("Window closed") 
       

    def close(self):
        self.running = False

    def draw_line(self, line: Line, fill="black", width=2):
        # Draw the line on the canvas
        line.draw(self.canvas, fill, width)
        self.redraw()