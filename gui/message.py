from tkinter import messagebox
from tkinter import Tk

win = Tk()

res1 = messagebox.askokcancel(" Title1 "," Do you Really ? ")
print(res1) #Yes = True,No = False

res2 = messagebox.askyesno(" Title2 "," Do you Really ? ")
print(res2) 

res3 = messagebox.askyesnocancel(" Title2 "," Do you Really ? ")
print(res3)

messagebox.showinfo("Title","a Tk MessageBox")
messagebox.showwarning("warning","a Tk error")
messagebox.showerror("error","a Tk error ")

win.mainloop()