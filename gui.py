data=""
def printtext():
    global e
    string = e.get()
    data=string
    print string

from Tkinter import *
root = Tk()

root.title('Text To Image')
root.minsize(width=666, height=466)


e = Entry(root)
e.pack()
e.focus_set()

b = Button(root,text='Draw',command=printtext)

b.pack(side='bottom')

root.mainloop()