from tkinter import *
import tkinter


from tkinter import messagebox
root=Tk()
answer=tkinter.messagebox.askquestion("question"," are you mad?")

if answer=="yes":
    tkinter.messagebox.showinfo("yes","i knew it")
if answer=="no":
    tkinter.messagebox.showinfo("no","dont lie")
    


  
root.mainloop()

 
