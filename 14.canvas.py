from tkinter import *
root=Tk()

canvas=Canvas(root,width=700,height=700)
canvas.pack()
canvas.create_rectangle(10,10,100,500,fill="blue")


canvas.create_arc(300,10,500,500,extent=45,style=ARC)

canvas.create_text(350,350,text="hello",font=("Times",30))



root.mainloop()
