#GRID BASED LAYOUT WE WILL NOT USE PACK NOW

from tkinter import *

root=Tk()

theLabel=Label(root,text=" window1",fg='blue')
theLabel.grid(row=0,column=0)

theLabe2=Button(root,text=" window2")
theLabe2.grid(row=0,column=1)
theLabe3= Label(root,text=" window3")
theLabe3.grid(row=1,column=0)

#entry is used for used to add text
theentry=Entry(root,width=30,fg='red')
theentry.grid(row=1,column=1)






root.mainloop()#it does not let the window close
