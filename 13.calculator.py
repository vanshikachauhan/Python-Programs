from tkinter import *

root=Tk()

equa=""
equation=StringVar()#it udates the variable with each update


    
def EqualPress():
    global equa
    total=eval(equa)
    equation.set(total)
    equa=""


calculation=Label(root,textvariable=equation)


calculation.grid(columnspan=4)

def btnpress(num):
    global equa
    equa=equa+str(num)
    equation.set(equa)
    
def Clear():
    global equa
    equa=""
    equation.set("")
     
    
    


button0=Button(root,text="0",command=lambda:btnpress(0))
button0.grid(row=4,column=2)

button1=Button(root,text="1",command=lambda:btnpress(1))
button1.grid(row=1,column=1)

button2=Button(root,text="2",command=lambda:btnpress(2))
button2.grid(row=1,column=2)

button3=Button(root,text="3",command=lambda:btnpress(3))
button3.grid(row=1,column=3)

button4=Button(root,text="4",command=lambda:btnpress(4))
button4.grid(row=2,column=1)
button5=Button(root,text="5",command=lambda:btnpress(5))
button5.grid(row=2,column=2)

button6=Button(root,text="6",command=lambda:btnpress(6))
button6.grid(row=2,column=3)

button7=Button(root,text="7",command=lambda:btnpress(7))
button7.grid(row=3,column=1)

button8=Button(root,text="8",command=lambda:btnpress(8))
button8.grid(row=3,column=2)

button9=Button(root,text="9",command=lambda:btnpress(9))
button9.grid(row=3,column=3)

plus=Button(root,text="+",command=lambda:btnpress("+"))
plus.grid(row=1,column=4)

minus=Button(root,text="-",command=lambda:btnpress("-"))
minus.grid(row=2,column=4)

mul=Button(root,text="*",command=lambda:btnpress("*"))
mul.grid(row=3,column=4)

div=Button(root,text="/",command=lambda:btnpress("/"))
div.grid(row=4,column=4)

equal=Button(root,text="=",command=EqualPress)
equal.grid(row=4,column=3)

clear=Button(root,text="c",command=Clear)
clear.grid(row=4,column=1)

root.mainloop()











