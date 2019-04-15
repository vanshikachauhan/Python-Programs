from tkinter import *
import time
root=Tk()

canvas=Canvas(root,width=700,height=700)
canvas.pack()

    
canvas.create_polygon(50,10,65,65,500,500,fill="red")
canvas.pack()

for i in range(0,60):
    canvas.move(1,5,0)
    root.update()
    time.sleep(0.1)
    
root.mainloop()
