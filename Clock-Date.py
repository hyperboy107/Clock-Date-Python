from tkinter import * 
from tkinter.ttk import *
from time import strftime
root = Tk()
root.title('RP Clock')
def time():
    string = strftime('%Y/%m/%d %I:%M:%S')
    lbl.config(text = string)
    lbl.after(1000, time)
lbl = Label(root, font = ('Radioland', 40, 'bold'),
            background = 'black',
            foreground = 'white')
lbl.pack(anchor = 'center')
time()
  
mainloop()