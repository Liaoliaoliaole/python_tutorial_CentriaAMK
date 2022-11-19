# Create a mini calculator
# reference and study from:
# https://www.w3schools.com/python/python_lambda.asp
# https://www.youtube.com/watch?v=vIvfPHqRK_M

from tkinter import *
import math

class calculator:
    def __init__(self):
        #root as artributs of class
        self.root = Tk()
        self.root.minsize(280, 450)
        self.root.maxsize(280, 470)
        self.root.title('Lili Mini Calculator')
        # calculation result 
        self.result = StringVar()
        self.result.set(0)
        # global variable lists stores all expression for calculation
        self.lists = []
        # check if clicked '='
        self.ispresssign = False
		#interface design
        self.menus()
        self.layout()
        self.root.mainloop()


    def menus(self):
        allmenu = Menu(self.root)
        allmenu.add_cascade(label='Menu Options coming later....')
        self.root.config(menu=allmenu)

    def layout(self):
        result = StringVar()
        result.set(0)
        show_label = Label(self.root, bd=3, bg='white', font=('Arial', 30), anchor='e', textvariable=self.result)
        show_label.place(x=5, y=20, width=270, height=70)
        # function buttons first and second rows(5 buttons per row )
        button_mc = Button(self.root, text='MC')
        button_mc.place(x=5, y=95, width=50, height=50)

        button_mr = Button(self.root, text='MR')
        button_mr.place(x=60, y=95, width=50, height=50)

        button_ms = Button(self.root, text='MS')
        button_ms.place(x=115, y=95, width=50, height=50)

        button_mjia = Button(self.root, text='M+')
        button_mjia.place(x=170, y=95, width=50, height=50)

        button_mjian = Button(self.root, text='M-')
        button_mjian.place(x=225, y=95, width=50, height=50)

        button_zuo = Button(self.root, text='←', command=self.dele_one)
        button_zuo.place(x=5, y=150, width=50, height=50)

        button_ce = Button(self.root, text='CE', command=lambda: self.result.set(0))
        button_ce.place(x=60, y=150, width=50, height=50)

        button_c = Button(self.root, text='C', command=self.sweeppress)
        button_c.place(x=115, y=150, width=50, height=50)

        button_zf = Button(self.root, text='±', command=self.posneg)
        button_zf.place(x=170, y=150, width=50, height=50)

        button_kpf = Button(self.root, text='√', command=self.mysqrt)
        button_kpf.place(x=225, y=150, width=50, height=50)

        # number buttons third row
        button_7 = Button(self.root, text='7', command=lambda: self.pressnum('7'))
        button_7.place(x=5, y=205, width=50, height=50)

        button_8 = Button(self.root, text='8', command=lambda: self.pressnum('8'))
        button_8.place(x=60, y=205, width=50, height=50)

        button_9 = Button(self.root, text='9', command=lambda: self.pressnum('9'))
        button_9.place(x=115, y=205, width=50, height=50)
        # function buttons
        button_division = Button(self.root, text='/', command=lambda: self.presscalculate('/'))
        button_division.place(x=170, y=205, width=50, height=50)

        button_remainder = Button(self.root, text='//', command=lambda:self.presscalculate('//'))
        button_remainder.place(x=225, y=205, width=50, height=50)

        # number buttons fourth row
        button_4 = Button(self.root, text='4', command=lambda: self.pressnum('4'))
        button_4.place(x=5, y=260, width=50, height=50)

        button_5 = Button(self.root, text='5', command=lambda: self.pressnum('5'))
        button_5.place(x=60, y=260, width=50, height=50)

        button_6 = Button(self.root, text='6', command=lambda: self.pressnum('6'))
        button_6.place(x=115, y=260, width=50, height=50)

        button_multiplication = Button(self.root, text='*', command=lambda: self.presscalculate('*'))
        button_multiplication.place(x=170, y=260, width=50, height=50)

        button_reciprocal = Button(self.root, text='1/x', command=self.ds)
        button_reciprocal.place(x=225, y=260, width=50, height=50)

        # fifth row 4+1
        button_1 = Button(self.root, text='1', command=lambda: self.pressnum('1'))
        button_1.place(x=5, y=315, width=50, height=50)

        button_2 = Button(self.root, text='2', command=lambda: self.pressnum('2'))
        button_2.place(x=60, y=315, width=50, height=50)

        button_3 = Button(self.root, text='3', command=lambda: self.pressnum('3'))
        button_3.place(x=115, y=315, width=50, height=50)

        button_subtraction = Button(self.root, text='-', command=lambda: self.presscalculate('-'))
        button_subtraction.place(x=170, y=315, width=50, height=50)

        button_equal = Button(self.root, text='=', command=lambda: self.pressequal())
        button_equal.place(x=225, y=315, width=50, height=105)

        # last row 3+1
        button_0 = Button(self.root, text='0', command=lambda: self.pressnum('0'))
        button_0.place(x=5, y=370, width=105, height=50)

        button_point = Button(self.root, text='.', command=lambda: self.pressnum('.'))
        button_point.place(x=115, y=370, width=50, height=50)

        button_plus = Button(self.root, text='+', command=lambda: self.presscalculate('+'))
        button_plus.place(x=170, y=370, width=50, height=50)

    #print expression function
    def pressnum(self,num):
        if self.ispresssign == False:
            pass
        else:
            self.result.set(0)
            self.ispresssign = False
        if num == '.':
            num = '0.'
        oldnum = self.result.get()
        if oldnum == '0':
            self.result.set(num)
        else:
            newnum = oldnum + num
            self.result.set(newnum)


    #press calculation events
    def presscalculate(self,sign):
        num = self.result.get()
        self.lists.append(num)
        self.lists.append(sign)
        self.ispresssign = True


    #calculate the result
    def pressequal(self):
        # get all expressions and store to lists
        curnum = self.result.get()
        self.lists.append(curnum)
        calculatestr = ''.join(self.lists)
        #  parses the expression passed to this method and runs python expression (code) within the program.
        endnum = eval(calculatestr)
        # save result 
        self.result.set(str(endnum)[:10])
        if self.lists != 0:
            self.ispresssign = True

        self.lists.clear()


    def dele_one(self):
        if self.result.get() == '' or self.result.get() == '0':
            self.result.set('0')
            return
        else:
            num = len(self.result.get())
            if num > 1:
                strnum = self.result.get()
                strnum = strnum[0:num - 1]
                self.result.set(strnum)
            else:
                self.result.set('0')

    def posneg(self):
        strnum = self.result.get()
        if strnum[0] == '-':
            self.result.set(strnum[1:])
        elif strnum[0] != '-' and strnum != '0':
            self.result.set('-' + strnum)

    def ds(self):
        dsnum = 1 / int(self.result.get())
        self.result.set(str(dsnum)[:10])
        if self.lists != 0:
            self.ispresssign = True

        self.lists.clear()

    def sweeppress(self):
        self.lists.clear()
        self.result.set(0)

    def mysqrt(self):
        strnum = float(self.result.get())
        endnum = math.sqrt(strnum)
        if str(endnum)[-1] == '0':
            self.result.set(str(endnum)[:-2])
        else:
            self.result.set(str(endnum)[:10])
        if self.lists != 0:
            self.ispresssign = True

        self.lists.clear()

mycalculator = calculator()
