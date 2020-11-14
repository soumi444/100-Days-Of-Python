from tkinter import *

def matching_char(list1,list2):
    for i in range (len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                c=list1[i]
                list1.remove(c)
                list2.remove(c)
                list3=list1 + list2
                return [list3,True]
    list3=list1+list2
    return [list3, False]

def submit():
    player1 = entry1.get()
    player1.lower
    player1.replace(" ", "")
    player1 = list(player1)

    player2 = entry1.get()
    player2.lower
    player2.replace(" ", "")
    player2 = list(player2)

    proceed=True

    while proceed:
        ret_list = matching_char(player1,player2)
        con_list = ret_list[0]
        proceed = ret_list[1]

    count=len(con_list)
    result = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]
    while len(result) > 1:

        split_index = (count % len(result) - 1)

        # this steps is done for performing
        # anticlock-wise circular fashion counting.
        if split_index >= 0:

            # list slicing
            right = result[split_index + 1:]
            left = result[: split_index]

            # list concatenation
            result = right + left

        else:
            result = result[: len(result) - 1]

            # insert method inserting the
        # value in the text entry box.


    entry3.insert(10, result[0])


# Function for clearing the
# contents of all text entry boxes
def clearAll():
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)

    # set focus on the Player1_field entry box
    entry1.focus_set()




root=Tk()
root.title("Flames Game")
root.configure(bg="blue")

label1 = Label(root, text="Player 1 Name:")
label1.grid(row=0, column=0)
entry1 = Entry(root)
entry1.grid(row=2, column=0)

label2 = Label(root, text="Player 2 Name:")
label2.grid(row=0, column=3)
entry2= Entry(root)
entry2.grid(row=2, column=3)

button1 = Button(root, text="Submit", command=submit)
button1.grid(row=3, column=2)

label3 = Label(root, text="Relationship Status:")
label3.grid(row=4, column=0)
entry3= Entry(root)
entry3.grid(row=4, column=3)

button2 = Button(root, text="Clear All", command=clearAll)
button2.grid(row=5, column=2)

root.mainloop()
