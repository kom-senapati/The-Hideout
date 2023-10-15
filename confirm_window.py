from tkinter import *
from sqlite import add_order
# Confirm window
from constants import Colors
from constants import Dimensions
from constants import Paths


def confirm(window,ordered,order_window):

    def yes():
        phone = entry0.get()
        name = entry1.get()

        ordered["Total"] = int(ordered["Total"][2:])
        Ordered = dict(sorted(ordered.items()))
        ordered_nums = list(Ordered.values())

        add_order(name, phone, ordered_nums)

        confirm_window.destroy()
        order_window.destroy()
        window.destroy()

    def no():
        confirm_window.destroy()

    confirm_window = Toplevel()
    confirm_window.title("Confirm")
    confirm_window.geometry("821x525")
    confirm_window.configure(bg=Colors.WHITE)
    canvas = Canvas(
        confirm_window,
        bg=Colors.WHITE,
        height=525,
        width=821,
        bd=0,
        highlightthickness=0,
        relief="ridge")
    canvas.place(x=0, y=0)

    entry0 = Entry(confirm_window,
                   bd=0,
                   bg=Colors.CNFRMCOL,
                   font=("Fira Code", 20))
    entry0.place(
        x=416.5, y=173,
        width=200.0,
        height=47)

    entry1 = Entry(confirm_window,
                   bd=0,
                   bg=Colors.CNFRMCOL,
                   font=("Fira Code", 20))

    entry1.place(
        x=416.5, y=108,
        width=200.0,
        height=47)

    img0 = PhotoImage(file=Paths.IMAGE_DIRECTORY+"no.png")
    b0 = Button(confirm_window,
                image=img0,
                command=no,
                relief="flat")

    b0.place(
        x=488, y=385,
        width=Dimensions.BUTTON_WIDTH,
        height=Dimensions.BUTTON_HEIGHT)

    img1 = PhotoImage(file=Paths.IMAGE_DIRECTORY+"yes.png")
    b1 = Button(confirm_window,
                image=img1,
                command=yes,
                relief="flat")

    b1.place(
        x=207, y=385,
        width=Dimensions.BUTTON_WIDTH,
        height=Dimensions.BUTTON_HEIGHT)

    background_img = PhotoImage(file=Paths.IMAGE_DIRECTORY+"background.png")
    background = canvas.create_image(320.0, 179.5, image=background_img)

    confirm_window.resizable(False, False)
    confirm_window.mainloop()
