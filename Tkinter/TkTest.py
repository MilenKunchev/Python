from tkinter import *

distance = ' ' * 20
root = Tk()
root.title("Title is here")

# Create a label Widget
my_label = Label(root, text='Your email')
my_label.grid(row=0, column=0)

entry = Entry(root, width=20, bg="white", fg="gray", borderwidth=1)
entry.grid(row=0, column=1)
entry.insert(0, " Your email")


def on_click_button_one():
    second_label = Label(root, text=entry.get())
    second_label.grid(row=1, column=1)


first_button = Button(root, text="Submit", command=on_click_button_one)
first_button.grid(row=0, column=2)

root.mainloop()
