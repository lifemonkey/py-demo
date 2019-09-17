from tkinter import *
from tkinter.messagebox import showinfo


def submit():
    showinfo("Infos", "Username/Password is not correct!!!")


def add_login(main_frame):

    # Add content to GUI
    # Add label/textbox
    Label(main_frame, text="User").grid(row=0, column=0)
    Entry(main_frame).grid(row=0, column=1)
    Label(main_frame, text="Password").grid(row=1, column=0)
    Entry(main_frame).grid(row=1, column=1)

    # Add button
    Button(main_frame, text="Submit", command=submit, activeforeground="blue", activebackground="grey").grid(row=2, column=0)
    # btn_submit.pack(side=BOTTOM)
    # btn_submit.pack(expand=TRUE)


def select(v, label):
    sel = "Value = " + str(v.get())
    label.config(text=sel)


def scale_box(main_frame):
    v = DoubleVar()
    scale = Scale(main_frame, variable=v, from_=1, to=50, orient=HORIZONTAL)
    scale.pack(anchor=CENTER)

    btn = Button(main_frame, text="Value", command=lambda: select(v, label))
    btn.pack(anchor=CENTER)

    label = Label(main_frame)
    label.pack()


# Create the application main window
main_frame = Tk()
main_frame.geometry("400x250")
# canvas = Canvas(main_frame, bg="pink", width="400", height="250")
# canvas.pack()

# add_login(main_frame)
scale_box(main_frame)

# Entering the event main loop
main_frame.mainloop()
