#Check 4 different fields of a feedback form before it can be submitted. 
#E.g user has to give age, telephone number, homepage url, email and/or other information and those values are checked (contents cannot be empty, either).

from tkinter import *
import tkinter.messagebox

root = Tk()
root.geometry('200x500')


label1=Label(root,text="Name")
label1.pack(anchor=W,padx=10,pady=10)
entry1 = Entry(root, width=180)
entry1.pack(anchor=W, padx=10,)

label2=Label(root,text="Age")
label2.pack(anchor=W,padx=10,pady=10)
entry2 = Entry(root, width=180)
entry2.pack(anchor=W, padx=10,)


label3 = Label(root, text="Telephone Number")
label3.pack(anchor=W, padx=10, pady=10)
entry3 = Entry(root, width=180)
entry3.pack(anchor=W, padx=10,)

label4 = Label(root, text="Homepage url")
label4.pack(anchor=W, padx=10, pady=10)
entry4 = Entry(root, width=180)
entry4.pack(anchor=W, padx=10,)

label5 = Label(root, text="Email")
label5.pack(anchor=W, padx=10, pady=10)
entry5 = Entry(root, width=180)
entry5.pack(anchor=W, padx=10,)
label6 = Label(root, text="Other information")
label6.pack(anchor=W, padx=10, pady=10)

text = Text(root, width=180, height=5)
text.pack(anchor=W, padx=10,)


def send_info():
    entry_text1=entry1.get()
    entry_text2=entry2.get()
    entry_text3=entry3.get()
    entry_text4=entry4.get()
    entry_text5=entry5.get()
    text_text = text.get('1.0',END)

    if entry1.get()=='' or entry2.get()=='' or entry3.get()=='' or entry4.get()=='' or entry5.get()=='':
        tkinter.messagebox.showinfo('Huom!','NOT allow empty input!')
    else:
        choice=tkinter.messagebox.askokcancel('','Send your information?')
        if choice:
            tkinter.messagebox.showinfo('Please Confirm', 'Your registration information: '+ '\n'+entry_text1 + '\n' +entry_text2+ '\n' +entry_text3+ '\n' +entry_text4+ '\n' +entry_text5 + '\n' +text_text)
        else:
            tkinter.messagebox.showinfo('','You have cancelled your registration.')


button = Button(root, text="Submit", width=8, height=1, command=send_info)
button.pack(anchor=E, padx=10,pady=10)

root.mainloop()
