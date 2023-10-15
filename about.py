from tkinter import *
from constants import Colors
from constants import Paths

def about():
    about_window = Toplevel()
    about_window.title("About")
    about_window.geometry("1152x700")
    about_window.configure(bg=Colors.CONCOL)
    canvas = Canvas(
        about_window,
        bg=Colors.CONCOL,
        height=700,
        width=1152,
        bd=0,
        highlightthickness=0,
        relief="ridge")
    canvas.place(x=0, y=0)

    background_img = PhotoImage(file=Paths.IMAGE_DIRECTORY+"about_bg.png")
    background = canvas.create_image(
        586.5, 334.0,
        image=background_img)

    about_window.resizable(False, False)
    about_window.mainloop()
