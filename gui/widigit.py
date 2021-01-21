import tkinter
from tkinter.constants import *
root = tkinter.Tk()
root.geometry("655x333")
def getval():
    print(userentry.get())
    print(passentry.get())
user=tkinter.Label(root,text="Username")
password=tkinter.Label(root,text="Password")
user.grid()
password.grid(row=1)
uservalue=tkinter.StringVar()
passvalue=tkinter.StringVar()
userentry=tkinter.Entry(root,textvariable=uservalue).grid(row=0,column=1)
passentry=tkinter.Entry(root,textvariable=passvalue).grid(row=1,column=1)
b1=tkinter.Button(root,text="SUBMIT",command=getval).grid(side=LEFT)
b2=tkinter.Button(root,text="Exit",command=root.destroy).pack(side=BOTTOM)
root.mainloop()