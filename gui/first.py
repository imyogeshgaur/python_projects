from tkinter import *
yogesh_root = Tk()
yogesh_root.maxsize(733,434)
photo=PhotoImage("download.png")
photo2=PhotoImage("download1.png")
photo3=PhotoImage("download3.png")
i=Label(Image(image="photo"))
j=Label(Image(image="photo1"))
k=Label(Image(image="photo2"))
i.pack()
j.pack()
k.pack()
yogesh_root.minsize(733,434)
mukesh=Label(text="Welcome to pycharm")
mukesh.pack()
yogesh_root.mainloop()
