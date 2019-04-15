

from tkinter import *

root=Tk()#to initialize the window

theLabel=Label(root,text="this is tkinter window")#adding text to our window,root is where you put text
theLabel.pack()#pack in our root(main window)

theLabel=Label(root,text="this is our second sentance")#adding text to our window,root is where you put text
theLabel.pack()#pack in our root(main window)

#wigits are added one after another.

theButoon=Button(None,text="click me",fg='blue')#button are wigits, first parameter tells in which layout you are putting it in,for now take it none,fg is for TEXT colour

theButoon.pack()

thButoon=Button(None,text="hellow",fg='red')

thButoon.pack()

#placement of button in proper layout,frames are laytout in which different wigits are placed.
#useing frames we put wigits in same row (not one after another)



root.mainloop()#it does not let the window close






