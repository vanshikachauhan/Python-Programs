
from tkinter import *

root=Tk()

def leftClick (event):
    print("left")
def rightClick(event):
    print("right")
def scroll(event):
    print("scrool")
def leftKey(event):
    print("left key pressed")
root.geometry("500x500")
root.bind("<Button-1>",leftClick)
root.bind("<Button-2>",rightClick)
root.bind("<Button-3>",scroll)
root.bind("<Left>",leftKey)


root.mainloop()#it does not let the window close
