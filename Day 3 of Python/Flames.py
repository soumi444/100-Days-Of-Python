from tkinter import *

root = Tk()
root.title("Flames Game")
root.configure(background="green")

label1 = Label(root, text="Player 1 Name:", fg="white", bg="pink").grid(row=0, column=0, columnspan=3)
label2 = Label(root, text="Player 2 Name:", fg="white", bg="pink").grid(row=2, column=0, columnspan=3)

text1 = Entry(root,relief="sunken", width=25).grid(row=0, column=5, columnspan=3)
text2 = Entry(root,relief="sunken", width=25).grid(row=2, column=5, columnspan=3)

button1 = Button(root, text="Submit", bg="pink", fg="white").grid(row=4, column=4)

label3 = Label(root, text="Relationship Status:", fg="white", bg="pink").grid(row=6, column=0, columnspan=3)
text3 = Entry(root,relief="sunken", width=25).grid(row=6, column=5, columnspan=3)

button2 = Button(root, text="Clear", bg="pink", fg="white").grid(row=8, column=4)

root.mainloop()