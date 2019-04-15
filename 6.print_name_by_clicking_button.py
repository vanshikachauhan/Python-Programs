from tkinter import *

root=Tk()

def printname():
    print("vanshika")

button=Button(root,text="clickme",command=printname)
button.pack()



root.mainloop()#it does not let the window close
