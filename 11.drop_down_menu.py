from tkinter import *

root=Tk()

mainMenu=Menu(root)
root.configure(menu=mainMenu)

subMenu=Menu(mainMenu)
subMenu1=Menu(mainMenu)
def printf():
    print("print it")
def randomf():
    print("random it")    


mainMenu.add_cascade(label="File1",menu=subMenu)
subMenu.add_command(label="new file",command=printf)
subMenu.add_command(label="random file",command=randomf)
subMenu.add_separator()
                    
subMenu.add_command(label="open",command=randomf)

mainMenu.add_cascade(label="File2",menu=subMenu1)
root.mainloop()
