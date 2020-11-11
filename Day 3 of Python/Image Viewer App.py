from tkinter import *
from PIL import ImageTk, Image

def forward(img_no):
    global label
    global button_forward
    global button_back
    global button_exit
    label.grid_forget()

    label=Label(image=list_images[img_no-1]).grid(row=0, column=0, columnspan=3)

    button_forward=Button(root, text=">>", command= lambda: forward(img_no+1)).grid(row=1, column=2)
    button_back=Button(root, text="<<", command=lambda:back(img_no-1)).grid(row=1, column=0)
    button_exit.grid(row=1, column=1)

    if img_no == 4:
        button_forward = Button(root, text="Forward",state=DISABLED)

def back():
    global label
    global button_forward
    global button_back
    global button_exit
    label.grid_forget()

    label = Label(image=List_images[img_no - 1])
    label.grid(row=1, column=0, columnspan=3)
    button_forward = Button(root, text="forward",command=lambda: forward(img_no + 1))
    button_back = Button(root, text="Back",command=lambda: back(img_no - 1))

    if img_no == 1:
        button_back = Button(root, Text="Back", state=DISABLED)

    label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_exit.grid(row=1, column=1)
    button_forward.grid(row=1, column=2)


root=Tk()
root.title("Image Viewer")

image_no_1 = ImageTk.PhotoImage(Image.open(r"C:\Users\91700\OneDrive\Desktop\images\download (2).jpg"))
image_no_2 = ImageTk.PhotoImage(Image.open(r"C:\Users\91700\OneDrive\Desktop\images\images (1).jpg"))
image_no_3 = ImageTk.PhotoImage(Image.open(r"C:\Users\91700\OneDrive\Desktop\images\images.jpg"))
image_no_4 = ImageTk.PhotoImage(Image.open(r"C:\Users\91700\OneDrive\Desktop\images\download (1).jpg"))

# List of the images so that we traverse the list
list_images = [image_no_1, image_no_2, image_no_3, image_no_4]

label = Label(image=image_no_1).grid(row=0, column=0, columnspan=3)
button_forward = Button(root, text=">>",command=lambda: forward(1)).grid(row=1, column=2)
button_exit = Button(root, text="Exit Program", command=root.quit).grid(row=1, column=1)
button_back = Button(root, text="<<", command=back, state=DISABLED).grid(row=1, column=0)

root.mainloop()