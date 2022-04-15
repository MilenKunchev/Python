from tkinter import *

distance = ' ' * 20
root = Tk()

# Create a label Widget
# my_label = Label(root, text='Click the button')
# my_label.grid(row=0, column=0)


def on_click():
    on_click_label = Label(root, text='Click the button')
    on_click_label.grid(row=0, column=0)


first_button = Button(root, text="BUTTON", command=on_click)
first_button.grid(row=0, column=2)

root.mainloop()
