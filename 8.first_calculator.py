from tkinter import *

root=Tk()


label=Label(root,text="enter expression")
label.pack()



def evaluate(event):
    data=e.get()
    ans.configure(text="ANSWER--"+str(eval(data)))


e=Entry(root)
e.bind("<Return>",evaluate)
e.pack()


ans=Label(root)

                  
ans.pack()
                  
root.mainloop()
