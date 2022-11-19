#kids math game (add prize: pic, sound or something else (negative/positive)) 
#Two numbers are shown on labels User adds the sum to a textbox With a button sum is checked 
# Then new values are generated to labels Right and wrong answers are shown

import random
import os
from tkinter import *   

img_dir = os.getcwd()
print(img_dir)

root = Tk()
root.geometry("201x251")
bg = PhotoImage(file = f'{img_dir}\image1.png')

# Show image using label
label1 = Label( root, image = bg)
label1.place(x = 0, y = 0)
label2 = Label( root, text = "ADDITION GAME")
label2.pack(pady = 50)

frameB= Frame(root)
frameB.pack(pady = 20)

#initiat two variables for calculation and operator(could be + and - or others)
x = IntVar()
y = IntVar()
operator = StringVar()
#BUTTONS for variables
n1=Button(frameB,textvariable = x).grid(row = 0,column = 0,sticky=W)
o1=Button(frameB,textvariable = operator,width = 1).grid(row = 0,column = 1,sticky=W)
n2=Button(frameB,textvariable = y).grid(row = 0,column = 2,sticky=W)
o2=Button(frameB,text = '=').grid(row = 0,column = 3,sticky=W)
e = Entry(frameB)
e.grid(row = 0, column = 4)

def newGame():
    x.set(random.randint(5,10))
    y.set(random.randint(0,5))
    operator.set('+')


Button(frameB,text = 'Easy!', width = 18,height = 1,background = 'pink', command = newGame).grid(row = 1,column = 4,sticky=W)

result = StringVar()
def checkResult(event):
    c = str(x.get())+operator.get()+str(y.get())
    if len(e.get()) !=0:
        if int(e.get()) == eval(c):
            newGame()
            result.set("AWSOME!")
            e.delete(0,'end')
        else:
            result.set("OOOPS!")
            e.delete(0, 'end')
    else:
        result.set("STILL WAITING...")

root.bind('<Return>', checkResult)
button2 = Button(frameB,text="Check your Answer!",width = 18,height = 1,background = 'purple')
button2.grid(row = 2,column = 4,sticky=W)
button2.bind('<Button-1>',checkResult)
Label(frameB,textvariable =result).grid(row = 1,column = 0,sticky=W)

root.mainloop()



