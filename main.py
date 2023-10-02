from tkinter import *
from sqlite import add_order
# Confirm window

# Constants for Colors
WHITE = "#FFFFFF"
BLACK = "#000000"
RED = "#FF0000"
GREEN = "#00FF00"
BLUE = "#0000FF"
CNFRMCOL = "#F6D6B1"
ORDCOL="#B47950"
ORDENTRY="#C4C4C4"
CONCOL="#f4fbfd"

# Directory path where the images are located
IMAGE_DIRECTORY = r"Images\\"

#constants for Home page buttons
#About us button
ABT_WIDTH = 219
ABT_HEIGHT = 62

#ORDER NOW button
ORD_HEIGHT = 62
ORD_WIDTH = 267

# Constants for Other Button Sizes
BUTTON_WIDTH = 153
BUTTON_HEIGHT = 53

# Constants for Image Paths

# To set the background color of a button
button_color = GREEN

# To set the size of a button
btn0 = (BUTTON_WIDTH, BUTTON_HEIGHT)





def confirm():

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
    confirm_window.configure(bg=WHITE)
    canvas = Canvas(
        confirm_window,
        bg=WHITE,
        height=525,
        width=821,
        bd=0,
        highlightthickness=0,
        relief="ridge")
    canvas.place(x=0, y=0)

    entry0 = Entry(confirm_window,
                   bd=0,
                   bg=CNFRMCOL,
                   font=("Fira Code", 20))
    entry0.place(
        x=416.5, y=173,
        width=200.0,
        height=47)

    entry1 = Entry(confirm_window,
                   bd=0,
                   bg=CNFRMCOL,
                   font=("Fira Code", 20))

    entry1.place(
        x=416.5, y=108,
        width=200.0,
        height=47)

    img0 = PhotoImage(file=IMAGE_DIRECTORY+"no.png")
    b0 = Button(confirm_window,
                image=img0,
                command=no,
                relief="flat")

    b0.place(
        x=488, y=385,
        width=BUTTON_WIDTH,
        height=BUTTON_HEIGHT)

    img1 = PhotoImage(file=IMAGE_DIRECTORY+"yes.png")
    b1 = Button(confirm_window,
                image=img1,
                command=yes,
                relief="flat")

    b1.place(
        x=207, y=385,
        width=BUTTON_WIDTH,
        height=BUTTON_HEIGHT)

    background_img = PhotoImage(file=IMAGE_DIRECTORY+"background.png")
    background = canvas.create_image(320.0, 179.5, image=background_img)

    confirm_window.resizable(False, False)
    confirm_window.mainloop()

# Order window


def order():
    global order_window

    def calculate():
        global ordered
        ordered = dict()
        menu = {'Frozen Frappe': [entry5, 250],
                'Hot chocolate': [entry4, 180],
                'Instant coffee': [entry3, 100],
                'Ice Latte': [entry2, 220],
                'Cappucino': [entry1, 140],
                'Coffee with ice cream': [entry0, 275]}
        total = 0
        for item, l in menu.items():
            if l[0].get() != "":
                total += int(l[0].get()) * l[1]
                ordered.update({item: l[0].get()})
        ordered.update({key: 0 for key in menu if key not in ordered})
        ordered.update({"Total": total})
        labelbill = Label(order_window,
                          bg=ORDCOL,
                          fg='#F5EEE9',
                          text="Rs" + str(total) + "/-",
                          font=("Cascadia Code", 30, "bold"))
        ordered.update({"Total": f"Rs{str(total)}"})

        labelbill.place(x=940, y=605)
        labelbill.after(1000, labelbill.destroy)
        order_window.after(1000, calculate)

    order_window = Toplevel()
    order_window.title("Billing Page")
    order_window.geometry("1152x700")
    order_window.configure(bg=ORDCOL)

    canvas = Canvas(
        order_window,
        bg=ORDCOL,
        height=700,
        width=1152,
        bd=0,
        highlightthickness=0,
        relief="ridge")
    canvas.place(x=0, y=0)

    entry0 = Entry(order_window, bd=0, bg=ORDENTRY, highlightthickness=0)
    entry0.place(x=1030, y=533, width=85, height=32)

    entry1 = Entry(order_window, bd=0, bg=ORDENTRY, highlightthickness=0)
    entry1.place(x=1030, y=393, width=85, height=33)

    entry2 = Entry(order_window, bd=0, bg=ORDENTRY, highlightthickness=0)
    entry2.place(x=1032, y=273, width=85, height=32)

    entry3 = Entry(order_window, bd=0, bg=ORDENTRY, highlightthickness=0)
    entry3.place(x=467, y=522, width=76, height=30)

    entry4 = Entry(order_window, bd=0, bg=ORDENTRY, highlightthickness=0)
    entry4.place(x=467, y=402, width=76, height=30)

    entry5 = Entry(order_window, bd=0, bg=ORDENTRY, highlightthickness=0)
    entry5.place(x=467, y=274, width=76, height=31)

    btn = Button(order_window, text="Order", font=(
        "Cascadia Code", 14, "bold"), command=confirm)
    btn.place(x=940, y=665,height=BUTTON_HEIGHT,width=BUTTON_WIDTH)
    background_img = PhotoImage(file=IMAGE_DIRECTORY+"order_bg.png")
    background = canvas.create_image(576.0, 523.5, image=background_img)

    order_window.after(1000, calculate)
    order_window.resizable(False, False)
    order_window.mainloop()

# About window


def about():
    about_window = Toplevel()
    about_window.title("About")
    about_window.geometry("1152x700")
    about_window.configure(bg=CONCOL)
    canvas = Canvas(
        about_window,
        bg=CONCOL,
        height=700,
        width=1152,
        bd=0,
        highlightthickness=0,
        relief="ridge")
    canvas.place(x=0, y=0)

    background_img = PhotoImage(file=IMAGE_DIRECTORY+"about_bg.png")
    background = canvas.create_image(
        586.5, 334.0,
        image=background_img)

    about_window.resizable(False, False)
    about_window.mainloop()

# Main window


window = Tk()
window.title("The Hideout")
window.geometry("1152x700")
window.configure(bg=WHITE)
canvas = Canvas(
    window,
    bg=WHITE,
    height=700,
    width=1152,
    bd=0,
    highlightthickness=0,
    relief="ridge")
canvas.place(x=0, y=0)

background_img = PhotoImage(file=IMAGE_DIRECTORY + "main_bg.png")
background = canvas.create_image(
    576.0, 350.0,
    image=background_img)

img0 = PhotoImage(file=IMAGE_DIRECTORY+"img0.png")
b0 = Button(
    image=img0,
    borderwidth=0,
    highlightthickness=0,
    command=about,
    relief="flat")

b0.place(
    x=603, y=213,
    height=ABT_HEIGHT,
    width=ABT_WIDTH)

img1 = PhotoImage(file=IMAGE_DIRECTORY+"img1.png")
b1 = Button(
    image=img1,
    borderwidth=0,
    highlightthickness=0,
    command=order,
    relief="flat")

b1.place(
    x=603, y=322,
    height=ORD_HEIGHT,
    width=ORD_WIDTH)

window.resizable(False, False)
window.mainloop()
