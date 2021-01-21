import tkinter
from tkinter.constants import *
tk = tkinter.Tk()
def hny():
    print("Happy New Year 2020")
tk.minsize(300,600)
f1 = tkinter.Frame(tk, relief=RIDGE, borderwidth=2)
f1.pack(fill=BOTH,expand=1)
l1 = tkinter.Label(f1, text="Hello, I Want To Say Something")
l1.pack(fill=X, expand=1)
b1=tkinter.Button(f1,text="Click Here",command=hny)
b1.pack(side=LEFT)
b2 = tkinter.Button(f1,text="Exit",command=tk.destroy)
b2.pack(side=BOTTOM)
tk.mainloop()