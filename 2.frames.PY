from tkinter import *

root=Tk()#to initialize the window
#placement of button in proper layout,frames are laytout in which different wigits are placed.
#useing frames we put wigits in same row (not one after another)
topFrame=Frame(root)

topFrame.pack()
botFrame=Frame(root)

botFrame.pack(side=BOTTOM)



#wigits are added one after another.

Butoon1=Button(topFrame,text="click me",fg='blue')
Butoon1.pack(side='left')

Butoon2=Button(topFrame,text="hellow",fg='red')

Butoon2.pack()


Butoon3=Button(botFrame,text="click me",fg='blue')
Butoon3.pack(side='left')

Butoon4=Button(botFrame,text="hellow",fg='red')

Butoon4.pack()



root.mainloop()#it does not let the window close
##side='left'
