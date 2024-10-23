from tkinter import *
root=Tk()
root.geometry("600x500")

def submit():
    name = entryMsg.get()
    age = entryMsg2.get()
    result['text'] = f"Hello {name}, you are just {age} years old"

label1 = Label(root, text="Enter your name: ")
label1.place(relx=0.05,rely=0.08)
entryMsg = Entry(root)
entryMsg.place(relx=0.2, rely=0.08)

label2 = Label(root, text="Enter Age: ")
label2.place(relx=0.05,rely=0.19)
entryMsg2= Entry(root)
entryMsg2.place(relx=0.15, rely=0.2)
button = Button(root, text="Submit", command=submit)
button.place(relx=0.2, rely=0.3)
result = Label(root, text="")
result.place(relx=0.2, rely=0.4)

root.mainloop()