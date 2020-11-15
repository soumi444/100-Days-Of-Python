from tkinter import *
from tkinter import messagebox

counter=1
tasks_list=[]


def inputError():
    # check for enter task field is empty or not
    if taskEntry.get(1.0,END) == "":
        # show the error message
        messagebox.showerror("Input Error")

        return 0

    return 1

def submit():
    value=inputError()
    if value==0:
        return
    content=taskEntry.get() + "\n"
    tasks_list.append(content)
    textArea.insert('end -1 chars', "[ " + str(counter) + " ] " + content)

    # incremented
    counter += 1
    taskEntry.delete(0,END)

def delete():
    global counter

    if len(tasks_list)==0:
        messagebox.showerror("No task")
        return

    number=tasknumberEntry.get(1.0,END)

    if number=="\n" or number!=int(number):
        messagebox.showerror("Not a Number")

    tasknumberEntry.delete(0,END)
    tasks_list.pop(number-1)
    textArea.delete(0,END)
    counter-=1
    for i in range(len(tasks_list)):
        TextArea.insert('end -1 chars', "[ " + str(i + 1) + " ] " + tasks_list[i])

root=Tk()
root.title("To-Do List")
root.config(bg="black")


label1 = Label(root, text="Enter You Task:").pack()
taskEntry = Entry(root, width=25).pack()
submitButton= Button(root, text="Submit",command=submit).pack()
textArea = Text(root, height = 5, width = 25, font = "lucida 13").pack()
taskLabel = Label(root, text="Delete Task Number").pack()
tasknumberEntry = Entry(root, width=2, font="lucida 13").pack()
deleteButton=Button(root, text="Delete", command=delete).pack()
exitButton=Button(root,text="Exit",command=exit).pack()

root.mainloop()