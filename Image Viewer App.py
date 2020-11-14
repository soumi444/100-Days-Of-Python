from tkinter import *
from PIL import Image, ImageTk

def forward(img_no):
    global label1
    global button2
    global button1
    global button3
    label1.grid_forget()

    label1 = Label(root, image=img_list[img_no-1])
    label1.grid(row=0, column=0, columnspan=3)

    button1 = Button(root, text=">>", command=lambda: forward(img_no+1))
    button1.grid(row=1, column=2)

    if img_no==4:
        button1 = Button(root, text=">>",state=DISABLED)
        button1.grid(row=1, column=2)

    button3 = Button(root, text="<<", command=lambda :back(img_no-1))
    button3.grid(row=1, column=0)

def back(img_no):
    global label1
    global button2
    global button1
    global button3
    label1.grid_forget()

    label1 = Label(root, image=img_list[img_no - 1])
    label1.grid(row=0, column=0, columnspan=3)

    button1 = Button(root, text=">>", command=lambda: forward(img_no + 1))
    button1.grid(row=1, column=2)

    button3 = Button(root, text="<<", command=lambda: back(img_no-1))
    button3.grid(row=1, column=0)

    if img_no==1:
        button1 = Button(root, text="<<",state=DISABLED)
        button1.grid(row=1, column=0)


root=Tk()
root.title("Image Viewer App")

img_1 = ImageTk.PhotoImage(Image.open(r"C:\Users\91700\OneDrive\Desktop\images\download (1).jpg"))
img_2 = ImageTk.PhotoImage(Image.open(r"C:\Users\91700\OneDrive\Desktop\images\download (2).jpg"))
img_3 = ImageTk.PhotoImage(Image.open(r"C:\Users\91700\OneDrive\Desktop\images\images (1).jpg"))
img_4 = ImageTk.PhotoImage(Image.open(r"C:\Users\91700\OneDrive\Desktop\images\images.jpg"))

img_list=[img_1, img_2, img_3, img_4]

label1 = Label(root, image=img_1)
label1.grid(row=0, column=0, columnspan=3)

button1 = Button(root, text=">>", command= lambda: forward(2))
button1.grid(row=1, column=2)
button2 = Button(root, text="Exit program", command=root.quit)
button2.grid(row=1, column=1)
button3 = Button(root, text="<<", command=back, state=DISABLED)
button3.grid(row=1, column=0)

root.mainloop()