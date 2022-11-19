#Create a Finnish - English - Finnish dictionary with some 50 word pairs...
#Create a 2 dimensional array – try to take word pairs from Internet or other source directly instead of typing them yourself (remember to mention to source!).
#Using Translators library: https://pypi.org/project/translate-api/

import translators as ts
from tkinter import Tk, Button, Entry, Label, Text, END

class Translate(object):
    def __init__(self):
        pass

    def translate2Fi(self, word):
        ts._google.language_map
        result = ts.google(word, from_language='en', to_language='fi')
        return result

    def translate2En(self, word):
        ts._google.language_map
        result = ts.google(word)
        return result


class Application(object):
    def __init__(self):
        self.window = Tk()
        self.fanyi = Translate()

        self.window.title(u'Translator')

        self.window.geometry('310x370+500+300')
        self.window.minsize(310, 370)
        self.window.maxsize(310, 370)

        self.result_text1 = Text(self.window, background='white')
        self.result_text1.place(x=10, y=5, width=285, height=155)
        #self.result_text1.bind("<Key-Return>", self.submit1)

        self.submit_btn0 = Button(self.window, text=u'To Finnish', command=self.submit1)
        self.submit_btn0.place(x=80, y=165, width=100, height=25)
        self.submit_btn1 = Button(self.window, text=u'To English', command=self.submit2)
        self.submit_btn1.place(x=160, y=165, width=100, height=25)
        self.submit_btn2 = Button(self.window, text=u'Clear', command=self.clean)
        self.submit_btn2.place(x=240, y=165, width=50, height=25)

        self.title_label = Label(self.window, text=u'Result:')
        self.title_label.place(x=10, y=165)

        self.result_text = Text(self.window, background='white')
        self.result_text.place(x=10, y=190, width=285, height=165)


    def submit1(self):
        content = self.result_text1.get(0.0, END).strip().replace("\n", " ")
        result = self.fanyi.translate2Fi(content)
        self.result_text.delete(0.0, END)
        self.result_text.insert(END, result)
        print(content)
    
    def submit2(self):
        content = self.result_text1.get(0.0, END).strip().replace("\n", " ")
        result = self.fanyi.translate2En(content)
        self.result_text.delete(0.0, END)
        self.result_text.insert(END, result)
        print(content)

    def clean(self):
        self.result_text1.delete(0.0, END)
        self.result_text.delete(0.0, END)

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    app = Application()
    app.run()
