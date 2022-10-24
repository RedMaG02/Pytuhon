import tkinter
import random
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from math import pi

#1
#def click():
#    inp = entry.get()

#    if(inp.isnumeric()):
#        celsium = (float(inp) - 32) / 1.8
#        label.config(text=celsium)
#    else:
#        print('INPUT MUST ME NUMERIC')

#window = tkinter.Tk()
#frame = tkinter.Frame(window)
#frame.pack(side='top')
#entry = tkinter.Entry(frame)
#entry.pack(side='top')
#label = tkinter.Label(frame)
#label.pack(side='top')
#convert = tkinter.Button(frame, text='Convert', command=click)
#convert.pack(side='top')
#exit = tkinter.Button(window, text='Exit', command=window.destroy).pack(side='top')
#window.mainloop()

#2
#def click1():
#    global tryes
#    var = entry1.get()
#    if label2.cget("text") != "":
#        if var.isalpha():
#            if tryes != 0:
#                if var == dict[rus]:
#                    label5.config(text="CORRECT")
#                    tryes = 5
#                else:
#                    label5.config(text="UNCORRECT tryes left:" + str(tryes))
#                    tryes -= 1
#            else:
#                label5.config(text="0 tryes left, generate new word")
#                click2()
#                tryes = 5
#        else:
#            label5.config(text="EMPTY, TRY AGAIN")
#    else:
#        click2()

#def click2():
#    global rus, eng
#    rus, eng = random.choice(list(dict.items()))
#    label2.config(text=rus)

#window = tkinter.Tk()
#dict = {"ЛУЧШИЙ ЯЗЫК": "PYTHON",
#              "АНИМЕ": "ANIME",
#              "ПИТОН": "SNAKE",
#              }
#tryes = 5
#rus = ""
#eng = ""
#label2 = Label(width=20)
#label2.grid(row=0, column=1, pady=10, padx=10)
#entry1 = Entry(width=20)
#entry1.grid(row=3, column=1, pady=10, padx=10)
#button1 = Button(text="Get word", width=20, command=lambda: click2())
#button1.grid(row=1, column=0, columnspan=3, pady=10, padx=10)
#button2 = Button(text="entry", width=20, command=lambda: click1())
#button2.grid(row=4, column=0, columnspan=3, pady=10, padx=10)
#label5 = Label(width=60, height=3)
#label5.grid(row=5, column=0, columnspan=3, pady=10, padx=10)
#window.mainloop()



#3
#html_template1 = """<html>
#<head>
#<title>Title</title>
#</head>
#<body>
#<h2>Текст:</h2>
#<p>
#"""
#html_template2 = """.</p>
#</body>
#</html>
#"""

#def saveTXT():
#    try:
#        path = filedialog.asksaveasfile(filetypes=(("Text files", "*.txt"), ("All files", "*.*"))).name
#        window.title('Notepad - ' + path + ".txt")
#    except:
#        return
#    with open(path + ".txt", 'w') as f:
#        f.write(entry_1.get())
#        f.close()


#def saveHTML():
#    try:
#        path = filedialog.asksaveasfile(filetypes=(("Html file", "*.html"), ("All files", "*.*"))).name
#        window.title('Notepad - ' + path + ".html")
#    except:
#        return
#    with open(path + ".html", 'w') as f:
#        f.write(html_template1)
#        f.write(entry_1.get())
#        f.write(html_template2)
#        f.close()

#def click():
#    if(opt.get() == "SAVE TXT"):
#        saveTXT()
#    else:
#        saveHTML()


#window = tkinter.Tk()

#opt = ttk.Combobox(window,  values = ["SAVE TXT", "SAVE HTML"])
#opt.config(width=30)
#opt.grid(row=1, column=1, pady=10, padx=10)
#button1 = Button(text="Save", width=20, command=lambda: click())
#button1.grid(row=1, column=2, columnspan=3, pady=10, padx=10)
#entry_1 = Entry(width=100, borderwidth=2)
#entry_1.grid(row=0, column=1, pady=10, padx=10)

#window.mainloop()




#4
html_template1 = """<html>
<head>
<title>Title</title>
</head>
<body>
<h2>Текст в формате html</h2>
<p>
"""
html_template2 = """.</p>
</body>
</html>
"""

def click():

    if entry_1.get().isdigit():
        inp = float(entry_1.get())
        try:
            res = (4 * pi * inp ** 3) / 3
            label1.config(text=res)
        except:
            label1.config(text="INPUT MUST BE NUMERIC!")
    else:
        label1.config(text="INPUT MUST BE NUMERIC!")


def saveTXT():
    var = str(label1.cget("text"))
    if var != "":
        try:
            path = filedialog.asksaveasfile(filetypes=(("Text files", "*.txt"), ("All files", "*.*"))).name
            window.title('Notepad - ' + path + ".txt")
        except:
            return
        with open(path + ".txt", 'w') as f:
            f.write("Answert for radius: " + str(entry_1.get()) + " = " + str(label1.cget("text")))
            f.close()
    else:
        pass


def saveHTML():
    var = str(label1.cget("text"))
    if var != "":
        try:
            path = filedialog.asksaveasfile(filetypes=(("Html file", "*.html"), ("All files", "*.*"))).name
            window.title('Notepad - ' + path + ".html")
        except:
            return
        with open(path + ".html", 'w') as f:
            f.write(html_template1)
            f.write("Answert for radius: " + str(entry_1.get()) + " = " + str(label1.cget("text")))
            f.write(html_template2)
            f.close()
    else:
        pass

def saveClick():
    if(opt.get() == "SAVE TXT"):
        saveTXT()
    else:
        saveHTML()


window = tkinter.Tk()

label1 = Label(width=20, borderwidth=1, relief="solid")
label1.grid(row=1, column=0, pady=10, padx=10)
entry_1 = Entry(width=25, borderwidth=2)
entry_1.grid(row=0, column=0, pady=10, padx=10)
button_1 = Button(text="Посчитать", width=30, command=lambda: click())
button_1.grid(row=3, column=0, columnspan=1, pady=10, padx=10)
button_2 = Button(text="Сохранить", width=10, command=lambda: saveClick())
button_2.grid(row=4, column=0, columnspan=1, pady=10, padx=10)
opt = ttk.Combobox(window,  values = ["SAVE TXT", "SAVE HTML"])
opt.config(width=15)
opt.grid(row=4, column=1, pady=10, padx=10)

window.mainloop()