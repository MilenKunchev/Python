from tkinter import *

distance = ' ' * 20
root = Tk()

# Create a label Widget
my_label = Label(root, text='Your email')
my_label.grid(row=0, column=0)

entry = Entry(root, width=20, bg="white", fg="red", borderwidth=1)
entry.grid(row=0, column=1)


def on_click_button_one():
    second_label = Label(root, text=entry.get())
    second_label.grid(row=1, column=1)


first_button = Button(root, text="Submit", command=on_click_button_one)
first_button.grid(row=0, column=2)

root.mainloop()
