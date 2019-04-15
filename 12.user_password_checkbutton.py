from tkinter import *

root=Tk()

theLabel=Label(root,text=" username:",fg='black')
theLabel.grid(row=0,column=0,sticky="E")

theEntry1=Entry(root,width=30,fg='red')
theEntry1.grid(row=0,column=1)

theLabe2=Label(root,text="password:")
theLabe2.grid(row=1,column=0,sticky="E")


theEntry2=Entry(root,width=30,fg='red')
theEntry2.grid(row=1,column=1)

CHECK=Checkbutton(root,text=" remember password")
CHECK.grid(columnspan=2)





root.mainloop()#it does not let the window close
