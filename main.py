from tkinter import *
from constants import Colors
from constants import Dimensions
from constants import Paths
#order window
from order import order
# about window
from about import about

def handle_order():
    order(window=window,ordered=ordered)

# To set the background color of a button
button_color = Colors.GREEN
# To set the size of a button
btn0 = (Dimensions.BUTTON_WIDTH, Dimensions.BUTTON_HEIGHT)

ordered = dict()

#main window
window = Tk()
window.title("The Hideout")
window.geometry("1152x700")
window.configure(bg=Colors.WHITE)
canvas = Canvas(
    window,
    bg=Colors.WHITE,
    height=700,
    width=1152,
    bd=0,
    highlightthickness=0,
    relief="ridge")
canvas.place(x=0, y=0)

background_img = PhotoImage(file=Paths.IMAGE_DIRECTORY+ "main_bg.png")
background = canvas.create_image(
    576.0, 350.0,
    image=background_img)

img0 = PhotoImage(file=Paths.IMAGE_DIRECTORY+"img0.png")
b0 = Button(
    image=img0,
    borderwidth=0,
    highlightthickness=0,
    command=about,
    relief="flat")

b0.place(
    x=603, y=213,
    height=Dimensions.ABT_HEIGHT,
    width=Dimensions.ABT_WIDTH)

img1 = PhotoImage(file=Paths.IMAGE_DIRECTORY+"img1.png")
b1 = Button(
    image=img1,
    borderwidth=0,
    highlightthickness=0,
    command=handle_order,
    relief="flat")

b1.place(
    x=603, y=322,
    height=Dimensions.ORD_HEIGHT,
    width=Dimensions.ORD_WIDTH)

window.resizable(False, False)
window.mainloop()
