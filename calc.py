import math
from tkinter import *

import speech_recognition
from pygame import mixer

mixer.init()


##-------------------------------------------CALCULATION BUTTON OPERATION-------------------------------------------------------
def click(value):
    ex = entryField.get()
    answer = ''

    try:
        if value == 'C':
            ex = entryField.get()
            ex = ex[0:len(ex) - 1]

            entryField.delete(0, END)
            entryField.insert(0, ex)
            return

        elif value == 'CE':
            entryField.delete(0, END)

        elif value == '√':
            answer = math.sqrt(eval(ex))

        elif value == 'π':
            answer = math.pi

        elif value == 'cosθ':
            answer = math.cos(math.radians(eval(ex)))

        elif value == 'tanθ':
            answer = math.tan(math.radians(eval(ex)))

        elif value == 'sinθ':
            answer = math.sin(math.radians(eval(ex)))

        elif value == '2π':
            answer = 2 * math.pi

        elif value == 'cosh':
            answer = math.cosh(eval(ex))

        elif value == 'tanh':
            answer = math.tanh(eval(ex))

        elif value == 'sinh':
            answer = math.cosh(eval(ex))

        elif value == chr(8731):
            answer = eval(ex) ** (1 / 3)

        elif value == 'x\u02b8':
            entryField.insert(END, '**')
            return

        elif value == 'x\u00B3':
            answer = eval(ex) ** 3

        elif value == 'x\u00B2':
            answer = eval(ex) ** 2

        elif value == 'ln':
            answer = math.log2(eval(ex))

        elif value == 'deg':
            answer = math.degrees(eval(ex))

        elif value == 'rad':
            answer = math.radians(eval(ex))

        elif value == 'e':
            answer = math.e

        elif value == 'log10':
            answer = math.log10(eval(ex))

        elif value == 'x!':
            answer = math.factorial(eval(ex))

        elif value == chr(247):
            entryField.insert(END, "/")
            return

        elif value == '=':
            answer = eval(ex)

        else:
            entryField.insert(END, value)
            return

        entryField.delete(0, END)
        entryField.insert(0, answer)

    except SyntaxError:
        pass


##------------------------------------------------VOICE OPERATION PART--------------------------------------------------

def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


def mod(a, b):
    return a % b


def lcm(a, b):
    l = math.lcm(a, b)
    return l


def hcf(a, b):
    h = math.gcd(a, b)
    return h


operations = {'ADD': add, 'ADDITION': add, 'SUM': add, 'PLUS': add,
              'SUBTRACTION': sub, 'DIFFERENCE': sub, ' MINUS ': sub, 'SUBTRACT': sub,
              'PRODUCT': mul, 'MULTIPLICATION': mul, 'MULTIPLY': mul,
              'DIVISION': div, 'DIV': div, 'DIVIDE': div,
              'LCM': mod, 'HCF': hcf,
              'MOD': mod, 'REMAINDER': mod, 'MODULUS': mod
              }


def findNumbers(t):
    l = []
    for num in t:
        try:
            l.append(int(num))
            pass

        except ValueError:
            pass
    return l


##------------------------------------------------AUDIO ANALYSING PART--------------------------------------------------
def audio():
    mixer.music.load('micstart.mp3')
    mixer.music.play()
    sr = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as m:

        try:
            sr.adjust_for_ambient_noise(m, duration=0.2)
            voice = sr.listen(m)
            text = sr.recognize_google(voice)

            mixer.music.load('micend.mp3')
            mixer.music.play()
            text_list = text.split(' ')
            for word in text_list:
                if word.upper() in operations.keys():
                    l = findNumbers(text_list)
                    print(l)
                    result = operations[word.upper()](l[0], l[1])
                    entryField.delete(0, END)
                    entryField.insert(END, result)

                else:
                    pass
        except:
            pass

##-------------------------------------------FRONT APPERANCE PART-------------------------------------------------------

root = Tk()
root.title('Voice Calculator')
root.config(bg='black')
root.geometry('650x450+100+100')

logoImage = PhotoImage(file='logo (2).png')
logoLabel = Label(root, image=logoImage)
logoLabel.grid(row=0, column=0)

entryField = Entry(root, font=('arial', 16, 'bold'), bg='white', fg='blue', bd=20, relief=SUNKEN, width=30)
entryField.grid(row=0, column=0, columnspan=8)

micImage = PhotoImage(file='microphone.png')
micButton = Button(root, image=micImage, bd=0, bg='black', activebackground='black', command=audio)
micButton.grid(row=0, column=7)

button_text_list = ["C", "CE", "√", "+", "π", "cosθ", "tanθ", "sinθ",
                    "1", "2", "3", "-", "2π", "cosh", "tanh", "sinh",
                    "4", "5", "6", "*", chr(8731), "x\u02b8", "x\u00B3", "x\u00B2",
                    "7", "8", "9", chr(247), "ln", "deg", "rad", "e",
                    "0", ".", "%", "=", "log10", "(", ")", "x!"
                    ]
rowval = 1
colval = 0
for i in button_text_list:

    button = Button(root, width=5, height=2, bd=2, relief=SUNKEN, text=i, bg='orange', fg='white',
                    font=('Times', '18', 'bold'), activebackground='white', command=lambda button=i: click(button))
    button.grid(row=rowval, column=colval, pady=1)
    colval += 1
    if colval > 7:
        rowval += 1
        colval = 0

root.mainloop()









# DEVELOPED AND DESINGNED BY K ARUNKUMAR(010) AND P KEERTHANA(054)#
