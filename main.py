import webbrowser
import tkinter as tk
from PIL import ImageTk, Image

width, height = 240, 240
x_offset, y_offset = 12, 12
timeout = 4 * 1000

class Popup():
    def __init__(self, url, text, imagepath):
        self.url = url
        img = Image.open(imagepath)
        img.thumbnail((width, height))

        self.root = tk.Tk()
        self.root.overrideredirect(1)

        self.img = ImageTk.PhotoImage(img)
        self.canvas = tk.Canvas(self.root, width=width, height=height)
        self.canvas.create_image(0, 0, image=self.img, anchor=tk.NW)
        self.canvas.bind("<Button-1>", self.quit) # left click
        self.canvas.bind("<Button-3>", self.open) # right click
        self.canvas.pack()

        self.label = tk.Label(self.canvas,
                          text=text,
                          font=('Helvetica', 9),
                          anchor=tk.SW,
                          justify=tk.LEFT,
                          wraplength=width)
        self.label.place(x=1, y=height-1, anchor=tk.SW)

        ws = self.root.winfo_screenwidth()  # screen width
        hs = self.root.winfo_screenheight() # screen height
        x = ws - width - x_offset
        y = hs - height - y_offset
        self.root.geometry('%dx%d+%d+%d' % (width, height, x, y))

    def quit(self, event):
        self.root.quit()

    def open(self, event):
        webbrowser.open(self.url)
        self.root.quit()

    def show(self):
        self.root.after(timeout, self.root.quit)
        self.root.mainloop()


if __name__ == '__main__':
    p = Popup('http://frnsys.com/', 'hi there', 'test.jpg')
    p.show()