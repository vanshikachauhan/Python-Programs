from tkinter import *
import random
root=Tk()

canvas=Canvas(root,width=700,height=700)
canvas.pack()

def rect(num):
    for i in range(0,num):
        x1=random.randrange(300)
        y1=random.randrange(300)
        x2=x1+random.randrange(300)
        y2=y1+random.randrange(300)

        canvas.create_rectangle(x1,x2,y1,y2)

rect(100)        
        
   





root.mainloop()
