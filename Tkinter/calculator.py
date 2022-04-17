from tkinter import *

root = Tk()
root.title("Calculator")

entry = Entry(root, width=45, bd=4)
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
entry.insert(0, "")


def button_click():
    return


number_button = {
    "padx": "40",
    "pady": "20",
    "command": button_click,

}

buttons_pad_x = 40
buttons_pad_y = 20

# define buttons
# TODO this is must be other Class in other file
button_1 = Button(root, text="1", **number_button)
button_2 = Button(root, text="2", **number_button)
button_3 = Button(root, text="3", **number_button)
button_4 = Button(root, text="4", **number_button)
button_5 = Button(root, text="5", **number_button)
button_6 = Button(root, text="6", **number_button)
button_7 = Button(root, text="7", **number_button)
button_8 = Button(root, text="8", **number_button)
button_9 = Button(root, text="9", **number_button)
button_0 = Button(root, text="0", **number_button)
button_add = Button(root, text="+", padx=buttons_pad_x - 1, pady=buttons_pad_y, command=button_click)
button_subtract = Button(root, text="- ", padx=buttons_pad_x - 1, pady=buttons_pad_y, command=button_click)
button_equal = Button(root, text=" = ", padx=buttons_pad_x + 46, pady=buttons_pad_y, command=button_click)
button_clear = Button(root, text="clr ", padx=buttons_pad_x - 5, pady=buttons_pad_y, command=button_click)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=1)

button_add.grid(row=4, column=0)
button_subtract.grid(row=4, column=2)
button_equal.grid(row=5, column=0, columnspan=2)
button_clear.grid(row=5, column=2)

root.mainloop()

print('Boyko1 ')