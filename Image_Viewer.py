from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Image Viewer")
root.iconbitmap("Image.ico")

my_image1 = ImageTk.PhotoImage(Image.open("Image_1.jpg"))
my_image2 = ImageTk.PhotoImage(Image.open("Image_2.jpg"))
my_image3 = ImageTk.PhotoImage(Image.open("Image_3.jpg"))

image_list = [my_image1, my_image2, my_image3]

status = Label(root, text = "Image 1 of 3", border = 1, relief = "solid", anchor = "e")

my_label = Label(image = my_image1)
my_label.grid(row = 0, column = 0, columnspan = 3)

def next_image(index):
    global my_label
    global button_next
    global button_prev
    global status

    my_label.grid_forget()
    my_label = Label(image = image_list[index - 1])
    button_next = Button(root, text = ">>", command = lambda: next_image(index + 1))
    button_prev = Button(root, text = "<<", command = lambda: previous_image(index - 1))

    if index == 3:
        button_next = Button(root, text = ">>", state = "disabled")

    my_label.grid(row = 0, column = 0, columnspan = 3)
    button_next.grid(row = 1, column = 2)
    button_prev.grid(row = 1, column = 0)

    status = Label(root, text = "Image " + str(index) + " of 3", border = 1, relief = "solid", anchor = "e")
    status.grid(row = 2, column = 0, columnspan = 3, sticky = "w" + "e")


def previous_image(index):
    global my_label
    global button_next
    global button_prev
    global status

    my_label.grid_forget()
    my_label = Label(image = image_list[index - 1])
    button_next = Button(root, text = ">>", command = lambda: next_image(index + 1))
    button_prev = Button(root, text = "<<", command = lambda: previous_image(index - 1))

    if index == 1:
        button_prev = Button(root, text = "<<", state = "disabled")

    my_label.grid(row = 0, column = 0, columnspan = 3)
    button_next.grid(row = 1, column = 2)
    button_prev.grid(row = 1, column = 0)

    status = Label(root, text = "Image " + str(index) + " of 3", border = 1, relief = "solid", anchor = "e")
    status.grid(row = 2, column = 0, columnspan = 3, sticky = "w" + "e")

button_prev = Button(root, text = "<<", state = "disabled")
button_exit = Button(root, text = "Exit Program", command = root.quit)
button_next = Button(root, text = ">>", command = lambda: next_image(2))

button_prev.grid(row = 1, column = 0)
button_exit.grid(row = 1, column = 1, pady = 10)
button_next.grid(row = 1, column = 2)

status.grid(row = 2, column = 0, columnspan = 3, sticky = "w" + "e")

root.mainloop()