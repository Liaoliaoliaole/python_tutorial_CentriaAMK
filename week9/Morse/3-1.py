#Create a morse coder
from tkinter import *

class morse2char():
    char_morse = {}
    morse_char = {}
    morse_num = {}
    char_num = {}
    def __init__(self):
        self.root = Tk()
        self.root.title("MORSE CODE TRANSLATOR")
        self.frm = Frame(self.root)
        #top
        Label(self.root,text="MORSE CODE TRANSLATOR", bg="green", font=('Arial',15)).pack()
        self.morse_table()
        #left
        self.frm_L = Frame(self.frm)
        self.frm_LT = Frame(self.frm_L)
        self.var_char = StringVar()
        Entry(self.frm_LT, textvariable=self.var_char, width=5, font=('Arial',15)).pack(side=RIGHT)
        Label(self.frm_LT, text="EN", bg="yellow", font=('Arial',12)).pack(side=LEFT)
        self.frm_LT.pack(side=TOP)
        self.var_L_char = StringVar()
        self.lb_char = Listbox(self.frm_L, selectmode=BROWSE, listvariable=self.var_L_char, font =('Verdana',12), width=6, height=13)
        self.lb_char.bind('<ButtonRelease-1>', self.get_char)
        for key in self.char_num:
            self.lb_char.insert(END, key[0])
        self.scrl_char = Scrollbar(self.frm_L)
        self.scrl_char.pack(side=RIGHT, fill=Y)
        self.lb_char.configure(yscrollcommand = self.scrl_char.set)
        self.lb_char.pack(side=LEFT, fill=BOTH)
        self.scrl_char['command'] = self.lb_char.yview
        self.frm_L.pack(side=LEFT)
        #mid
        self.frm_M = Frame(self.frm)
        self.t_show = Text(self.frm_M, width=20, height=5, font =('Verdana',15))
        self.t_show.insert('1.0', '')
        self.t_show.pack()
        self.frm_MB = Frame(self.frm_M)
        Button(self.frm_MB, text="CLEAR", command=self.clear, width=6, height=1, bd=3, font=('Arial', 10)).pack(side=LEFT)
        Button(self.frm_MB, text="RESULT", command=self.search, width=6, height=1, bd=3, font=('Arial', 10)).pack(side=RIGHT)
        self.frm_MB.pack(side=BOTTOM)
        self.frm_M.pack(side=LEFT)
        #right
        self.frm_R = Frame(self.frm)
        self.frm_RT = Frame(self.frm_R)
        self.var_morse = StringVar()
        Entry(self.frm_RT, textvariable=self.var_morse, width=5, font=('Arial',15)).pack(side=LEFT)
        Label(self.frm_RT, text="MORSE CODE", bg="pink", font=('Arial',12)).pack(side=RIGHT)
        self.frm_RT.pack(side=TOP)
        self.var_R_morse = StringVar()
        self.lb_morse = Listbox(self.frm_R, selectmode=BROWSE, listvariable=self.var_R_morse, font=('Verdana',12), width=10, height=13)
        self.lb_morse.bind('<ButtonRelease-1>',self.get_morse)
        for key in self.morse_num:
            self.lb_morse.insert(END,key[0])
        self.scrl_morse = Scrollbar(self.frm_R)
        self.scrl_morse.pack(side=RIGHT,fill=Y)
        self.lb_morse.configure(yscrollcommand=self.scrl_morse.set)
        self.lb_morse.pack(side=LEFT,fill=BOTH)
        self.scrl_morse['command'] = self.lb_morse.yview
        self.frm_R.pack(side=LEFT)
        self.frm.pack()

    def get_char(self, event):
        self.var_char.set('')
        self.var_morse.set('')
        tmp = self.lb_char.get(self.lb_char.curselection())
        self.var_char.set(tmp)

    def get_morse(self, event):
        self.var_morse.set('')
        self.var_char.set('')
        tmp = self.lb_morse.get(self.lb_morse.curselection())
        self.var_morse.set(tmp)


    def clear(self):
        self.var_char.set('')
        self.var_morse.set('')
        self.t_show.delete('1.0','10.0')

    def search(self):
        self.t_show.delete('1.0','10.0')
        tmp_char = self.var_char.get().upper()
        tmp_morse = self.var_morse.get()
        if tmp_char != '':
            #if not self.char_morse.has_key(tmp_char):
            if not self.char_morse.keys():
                self.t_show.insert('1.0','Invalid Input!')
            else:
                self.t_show.insert('1.0','morse code: ' + '\t' + self.char_morse[tmp_char][0:] + '\n')
        elif tmp_morse != '':
            if not self.morse_char.keys():
                self.t_show.insert('1.0','Invalid Input!')
            else:
                self.t_show.insert('1.0','charactor：' + '\t' + self.morse_char[tmp_morse][0] + '\n')
        else:
            self.t_show.insert('1.0',"Please select: ")
        self.var_char.set('')
        self.var_morse.set('')

    def morse_table(self):
        f = open('morse_query.txt','r')
        for line in f.readlines():
            print(line)
            pair = line.strip().split("  ")
            print(pair)
            self.char_morse[pair[0]] = pair[1]
            self.morse_char[pair[1]] = pair[0]

        self.char_num = sorted(self.char_morse.items(), key = lambda asd:asd[1])
        self.morse_num = sorted(self.morse_char.items(), key = lambda asd:asd[0])

def main():
    m = morse2char()
    mainloop()

if __name__ == "__main__":
    main()