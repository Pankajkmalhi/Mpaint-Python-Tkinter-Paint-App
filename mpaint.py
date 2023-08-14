from tkinter import *
from tkinter import filedialog, messagebox
from tkinter.ttk import Scale
from PIL import Image, ImageDraw
import PIL

CANVAS_HEIGHT, CANVAS_WIDTH = 400, 600

class Mpaint:

    def __init__(self):
        self.root = Tk()
        self.pen_color = "black"

        # window
        self.root.title("Paint")
        self.root.geometry("700x500")
        self.root.configure(background='white')
        self.root.resizable(0, 0)

        self.image = PIL.Image.new("RGB", (CANVAS_WIDTH, CANVAS_HEIGHT), "white")
        self.draw = ImageDraw.Draw(self.image)

        # widgets
        self.color_frame = LabelFrame(self.root, text='Color', font=('arial', 15), bd=3, relief=RIDGE, bg='white')
        self.color_frame.place(x=0, y=0, width=70, height=130)

        colors = ['#FF0000', '#0000FF', '#FFFF00']
        i = j = 0
        for color in colors:
            Button(self.color_frame, bg=color, bd=1, relief=RIDGE, width=3, command=lambda col=color: self.select_color(col)).grid(row=i, column=j)
            i += 1
            if i == 2:
                i = 0
                j = 1

        self.current_color = '#FF0000'  # Default color set to red

        self.eraser_button = Button(self.root, text="ERASER", bd=5, bg='white', command=self.eraser, width=7, relief=RIDGE)
        self.eraser_button.place(x=0, y=170)

        self.clear_button = Button(self.root, text="CLEAR", bd=5, bg='white', command=lambda: self.canvas.delete("all"), width=7, relief=RIDGE)
        self.clear_button.place(x=0, y=200)

        self.save_button = Button(self.root, text="SAVE", bd=5, bg='white', command=self.save, width=7, relief=RIDGE)
        self.save_button.place(x=0, y=230)

        # scale
        self.pen_size_frame = LabelFrame(self.root, text="Size", bd=5, bg='white', font=('arial', 15), relief=RIDGE)
        self.pen_size_frame.place(x=0, y=290, height=200, width=70)

        self.pen_size = Scale(self.pen_size_frame, orient=VERTICAL, from_=50, to=0, length=170)
        self.pen_size.set(1)
        self.pen_size.grid(row=0, column=1, padx=15)

        self.brush_width = self.pen_size.get()

        # canvas
        self.canvas = Canvas(self.root, bg='white', bd=5, relief=GROOVE, height=CANVAS_HEIGHT, width=CANVAS_WIDTH)
        self.canvas.place(x=80, y=50)

        # bind
        self.canvas.bind("<B1-Motion>", self.paint)

        self.root.mainloop()

    def paint(self, event):
        x1, y1 = (event.x - 2), (event.y - 2)
        x2, y2 = (event.x + 2), (event.y + 2)

        self.canvas.create_oval(x1, y1, x2, y2, fill=self.pen_color, outline=self.pen_color, width=self.pen_size.get())
        self.draw.rectangle([x1, y1, x2 + self.brush_width, y2 + self.brush_width], outline=self.pen_color, fill=self.pen_color, width=self.brush_width)

    def select_color(self, col):
        self.pen_color = col

    def eraser(self):
        self.pen_color = "white"

    def save(self):
        filename = filedialog.asksaveasfilename(initialfile="untitled.png", defaultextension="png", filetypes=[("PNG", "JPG"), (".png", ".jpg")])

        if filename != "":
            self.image.save(filename)

Mpaint()
