from tkinter import *
#A simple GUI for checking prime numbers
#version 1.0
#a large number can cause the app to beachball
#by William Brannock

#Basic Windows Setup
window = Tk() 
window.title("Prime Number Checker")
window.geometry('500x350')

#Creates Label
lbl = Label(window, text="Type in a number.", anchor = "w")
lbl.grid(column=0, row=0)

#Creates Text Box
txt = Entry(window,width=10)
txt.grid(column=1, row=0)

#Creates display label
lbl2 = Label(window, text="You have not yet entered a number.", anchor = "w")
lbl2.grid(column=0, row=1)
def clicked():
      res = int(txt.get())
      if res > 1:
            for i in range(2,res):
                  if (res % i) == 0:
                        lbl2.configure(text= "Not Prime", anchor = "w")
                        break
                  else:
                        lbl2.configure(text= "Prime", anchor = "w")
      else:
            lbl2.configure(text= "Not Prime", anchor = "w")
btn = Button(window, text="Check", command=clicked)
 
btn.grid(column=2, row=0)
window.mainloop()