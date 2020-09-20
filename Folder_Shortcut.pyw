from tkinter import *
import os
window = Tk()
window.geometry('300x200')
#frame = Frame(master = window, width = 300, height = 200, bg = 'red')
#frame.pack()
#---------------------------------------------------------------------------------------------------------------------------------------
window.title('Different Folders path Shortcut')
lbl1 = Label (text = 'Folder Name', font = ("Arial Bold", 20))
lbl1.grid(row = 0, column = 0)
lbl2 = Label (text = 'Action', font = ("Arial Bold", 20))
lbl2.grid(row = 0, column = 1)
#---------------------------------------------------------------------------------------------------------------------------------------

lbl3 = Label (text = 'downloads:', font = ("Arial Bold", 15))
lbl3.grid(row = 1, column = 0)
def downloads():
   fd = os.startfile(r'C:\Users\dppalai\Downloads')
   
button1 = Button(window, text = 'OPEN', 
                 command = downloads, 
				 font = 15, 
				 activebackground = 'green', 
				 activeforeground = 'orange',
				 foreground = 'white',
				 background = 'black')
button1.grid(row = 1, column = 1)
#---------------------------------------------------------------------------------------------------------------------------------------

lbl4 = Label (text = 'WORKDOC:', font = ("Arial Bold", 15))
lbl4.grid(row = 2, column = 0)

def workdoc():
   fd = os.startfile(r'C:\WORKDOC')
   
button2 = Button(window, text = 'OPEN', 
                 command = workdoc, 
				 font = 15, 
				 activebackground = 'green', 
				 activeforeground = 'orange',
				 foreground = 'white',
				 background = 'black')
button2.grid(row = 2, column = 1)
#----------------------------------------------------------------------------------------------------------------------------------------
lbl5 = Label (text = 'Software CD:', font = ("Arial Bold", 15))
lbl5.grid(row = 3, column = 0)

def Software_CD():
   fd = os.startfile(r'C:\Software CD')
   
button3 = Button(window, text = 'OPEN', 
                 command = Software_CD, 
				 font = 15, 
				 activebackground = 'green', 
				 activeforeground = 'orange',
				 foreground = 'white',
				 background = 'black')
button3.grid(row = 3, column = 1)
#-----------------------------------------------------------------------------------------------------------------------------------------

lbl6 = Label (text = 'My Documents:', font = ("Arial Bold", 15))
lbl6.grid(row = 4, column = 0)

def My_Documents():
   fd = os.startfile(r'C:\My_Documents')
   
button4 = Button(window, text = 'OPEN', 
                 command = My_Documents, 
				 font = 15, 
				 activebackground = 'green', 
				 activeforeground = 'orange',
				 foreground = 'white',
				 background = 'black')
button4.grid(row = 4, column = 1)
window.mainloop()