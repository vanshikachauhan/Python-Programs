
from tkinter import *
root=Tk()

canvas=Canvas(root,width=700,height=700)
canvas.pack()

def rect(x1,x2,y1,y2,colour):
    
   canvas.create_rectangle(x1,x2,y1,y2,fill=colour)
   
rect(100,100,400,400,"red")
rect(100,20,80,300,"green")
   





root.mainloop()
