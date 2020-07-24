from tkinter import *

root = Tk()
root.title("test")

btn1 = Button(root, padx=10, pady=10, text="버튼1")
btn1.pack()

btn2 = Button(root, padx=10, pady=10, text="버튼2")
btn2.pack()

btn3 = Button(root, padx=10, pady=10,fg="red",bg="yellow", text="버튼3")
btn3.pack()

def btncmd():
    print("펑~~!!")

btn4 = Button(root,text="누르지마시오",padx=10,pady=10,command=btncmd)
btn4.pack()

root.mainloop()