# Create a program that asks the user to submit a string or number through a graphical user interface (GUI),
# and that string or number is stored as a new line in an existing text file.
# Please have three buttons: Add Line , Save Changes , and Save and Close .

from tkinter import *

# List for words typed by user in "text box"
words = []

"""---App logic---"""


# "Add line" button logic
def add_line():
    get_input = text_box.get()
    words.append(get_input)
    text_box.delete(0, "end")


# "Save changes" button logic
def save():
    with open("user_data_GUI.txt", "a") as file:
        for x in words:
            file.write(x + "\n")
    words.clear()


# "Save and close" button logic
def save_and_close():
    with open("user_data_GUI.txt", "a") as file:
        for x in words:
            file.write(x + "\n")
    window.destroy()


"""---GUI---"""

# Our GUI window
window = Tk()

# Text box
text_box = Entry(window)
text_box.pack(side=LEFT)

# "Add line" button
add_line_button = Button(window, text="Add line", command=add_line)
add_line_button.pack(side=LEFT)

# "Save changes" button
save_button = Button(window, text="Save changes", command=save)
save_button.pack(side=LEFT)

# "Save and close" button
save_close_button = Button(window, text="Save and close", command=save_and_close)
save_close_button.pack(side=LEFT)

window.mainloop()
