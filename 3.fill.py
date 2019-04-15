from tkinter import *

root=Tk()


#FILL IS USED AS THE SIZE OF WINDOW CHANGES THE BUTTON SIZE ACCORDINGLY CHANGES

Butoon1=Button(None,text="click me",fg='blue')
Butoon1.pack()

Butoon2=Button(None,text="hellow",fg='red')

Butoon2.pack(fill=X)


Butoon3=Button(None,text="click me",fg='GREEN')
Butoon3.pack(side='left',fill=Y)

Butoon4=Button(None,text="hellow",fg='YELLOW')

Butoon4.pack()



root.mainloop()#it does not let the window close
