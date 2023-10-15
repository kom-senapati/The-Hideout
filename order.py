from tkinter import *
from constants import Colors
from constants import Dimensions
from constants import Paths
#confirm window
from confirm_window import confirm

def order(window,ordered):
    
    def handle_confirm():
        confirm(window=window,ordered=ordered,order_window=order_window);
    def calculate():
        
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
                          bg=Colors.ORDCOL,
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
    order_window.configure(bg=Colors.ORDCOL)

    canvas = Canvas(
        order_window,
        bg=Colors.ORDCOL,
        height=700,
        width=1152,
        bd=0,
        highlightthickness=0,
        relief="ridge")
    canvas.place(x=0, y=0)

    entry0 = Entry(order_window, bd=0, bg=Colors.ORDENTRY, highlightthickness=0)
    entry0.place(x=1030, y=533, width=85, height=32)

    entry1 = Entry(order_window, bd=0, bg=Colors.ORDENTRY, highlightthickness=0)
    entry1.place(x=1030, y=393, width=85, height=33)

    entry2 = Entry(order_window, bd=0, bg=Colors.ORDENTRY, highlightthickness=0)
    entry2.place(x=1032, y=273, width=85, height=32)

    entry3 = Entry(order_window, bd=0, bg=Colors.ORDENTRY, highlightthickness=0)
    entry3.place(x=467, y=522, width=76, height=30)

    entry4 = Entry(order_window, bd=0, bg=Colors.ORDENTRY, highlightthickness=0)
    entry4.place(x=467, y=402, width=76, height=30)

    entry5 = Entry(order_window, bd=0, bg=Colors.ORDENTRY, highlightthickness=0)
    entry5.place(x=467, y=274, width=76, height=31)

    btn = Button(order_window, text="Order", font=(
        "Cascadia Code", 14, "bold"), command=handle_confirm)
    btn.place(x=940, y=665,height=Dimensions.BUTTON_HEIGHT,width=Dimensions.BUTTON_WIDTH)
    background_img = PhotoImage(file=Paths.IMAGE_DIRECTORY+"order_bg.png")
    background = canvas.create_image(576.0, 523.5, image=background_img)

    order_window.after(1000, calculate)
    order_window.resizable(False, False)
    order_window.mainloop()
