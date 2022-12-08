import random
from tkinter import *
from tkinter.messagebox import showinfo
from itertools import permutations

y = ""
x = 2
player1 = []
player2 = []


def start():
    button1['state'] = 'active'
    button2['state'] = 'active'
    button3['state'] = 'active'
    button4['state'] = 'active'
    button5['state'] = 'active'
    button6['state'] = 'active'
    button7['state'] = 'active'
    button8['state'] = 'active'
    button9['state'] = 'active'
    button11['state'] = 'active'


def reset():
    player1 = []
    player2 = []
    button1['text'] = ''
    button2['text'] = ''
    button3['text'] = ''
    button4['text'] = ''
    button5['text'] = ''
    button6['text'] = ''
    button7['text'] = ''
    button8['text'] = ''
    button9['text'] = ''


def define_sign(num):
    global x, y
    global player1, player2

    set1 = permutations([1, 2, 3])
    set2 = permutations([4, 5, 6])
    set3 = permutations([7, 8, 9])
    set4 = permutations([1, 4, 7])
    set5 = permutations([2, 5, 8])
    set6 = permutations([3, 6, 9])
    set7 = permutations([1, 5, 9])
    set8 = permutations([3, 5, 7])

    for i in set1, set2, set3, set4, set5, set6, set7, set8:
        for j in list(i):
            play1 = all(elem in player1 for elem in j)
            play2 = all(elem in player2 for elem in j)
            if play1:
                showinfo("WIN!!!", "Player 1 wins!!!")
                player1 = []
                player2 = []
                button1['text'] = ''
                button2['text'] = ''
                button3['text'] = ''
                button4['text'] = ''
                button5['text'] = ''
                button6['text'] = ''
                button7['text'] = ''
                button8['text'] = ''
                button9['text'] = ''
                break
            elif play2:
                showinfo("WIN!!!", "Player 2 wins!!!")
                player1 = []
                player2 = []
                button1['text'] = ''
                button2['text'] = ''
                button3['text'] = ''
                button4['text'] = ''
                button5['text'] = ''
                button6['text'] = ''
                button7['text'] = ''
                button8['text'] = ''
                button9['text'] = ''
                break
            else:
                pass

    if num == 1:
        if x % 2 == 0:
            y = 'X'
            if button1['text'] == 'O' or button1['text'] == 'X':
                showinfo("Uh Oh!", "Choose another spot")
                x += 1

            else:
                button1.config(text=y)
                player1.append(num)
                x += 1
                bot_click()
                x += 1

        elif x % 2 != 0:
            y = 'O'
            if button1['text'] == 'X' or button1['text'] == 'O':
                bot_click()
                x += 1

            else:
                button1.config(text=y)
                player2.append(num)
        x += 1

    if num == 2:
        if x % 2 == 0:
            y = 'X'
            if button2['text'] == 'O' or button2['text'] == 'X':
                showinfo("Uh Oh!", "Choose another spot")
                x += 1

            else:
                button2.config(text=y)
                player1.append(num)
                x += 1
                bot_click()
                x += 1

        elif x % 2 != 0:
            y = 'O'
            if button2['text'] == 'X' or button2['text'] == 'O':
                bot_click()
                x += 1

            else:
                button2.config(text=y)
                player2.append(num)
        x += 1

    if num == 3:
        if x % 2 == 0:
            y = 'X'
            if button3['text'] == 'O' or button3['text'] == 'X':
                showinfo("Uh Oh!", "Choose another spot")
                x += 1

            else:
                button3.config(text=y)
                player1.append(num)
                x += 1
                bot_click()
                x += 1

        elif x % 2 != 0:
            y = 'O'
            if button3['text'] == 'X' or button3['text'] == 'O':
                bot_click()
                x += 1

            else:
                button3.config(text=y)
                player2.append(num)
        x += 1

    if num == 4:
        if x % 2 == 0:
            y = 'X'
            if button4['text'] == 'O' or button4['text'] == 'X':
                showinfo("Uh Oh!", "Choose another spot")
                x += 1

            else:
                button4.config(text=y)
                player1.append(num)
                x += 1
                bot_click()
                x += 1

        elif x % 2 != 0:
            y = 'O'
            if button4['text'] == 'X' or button4['text'] == 'O':
                bot_click()
                x += 1

            else:
                button4.config(text=y)
                player2.append(num)
        x += 1

    if num == 5:
        if x % 2 == 0:
            y = 'X'
            if button5['text'] == 'O' or button5['text'] == 'X':
                showinfo("Uh Oh!", "Choose another spot")
                x += 1

            else:
                button5.config(text=y)
                player1.append(num)
                x += 1
                bot_click()
                x += 1

        elif x % 2 != 0:
            y = 'O'
            if button5['text'] == 'X' or button1['text'] == 'O':
                bot_click()
                x += 1

            else:
                button5.config(text=y)
                player2.append(num)
        x += 1

    if num == 6:
        if x % 2 == 0:
            y = 'X'
            if button6['text'] == 'O' or button6['text'] == 'X':
                showinfo("Uh Oh!", "Choose another spot")
                x += 1

            else:
                button6.config(text=y)
                player1.append(num)
                x += 1
                bot_click()
                x += 1

        elif x % 2 != 0:
            y = 'O'
            if button6['text'] == 'X' or button6['text'] == 'O':
                bot_click()
                x += 1

            else:
                button6.config(text=y)
                player2.append(num)
        x += 1

    if num == 7:
        if x % 2 == 0:
            y = 'X'
            if button7['text'] == 'O' or button7['text'] == 'X':
                showinfo("Uh Oh!", "Choose another spot")
                x += 1

            else:
                button7.config(text=y)
                player1.append(num)
                x += 1
                bot_click()
                x += 1

        elif x % 2 != 0:
            y = 'O'
            if button7['text'] == 'X' or button7['text'] == 'O':
                bot_click()
                x += 1

            else:
                button7.config(text=y)
                player2.append(num)
        x += 1

    if num == 8:
        if x % 2 == 0:
            y = 'X'
            if button8['text'] == 'O' or button8['text'] == 'X':
                showinfo("Uh Oh!", "Choose another spot")
                x += 1

            else:
                button8.config(text=y)
                player1.append(num)
                x += 1
                bot_click()
                x += 1

        elif x % 2 != 0:
            y = 'O'
            if button8['text'] == 'X' or button8['text'] == 'O':
                bot_click()
                x += 1

            else:
                button8.config(text=y)
                player2.append(num)
        x += 1

    if num == 9:
        if x % 2 == 0:
            y = 'X'
            if button9['text'] == 'O' or button9['text'] == 'X':
                showinfo("Uh Oh!", "Choose another spot")
                x += 1

            else:
                button9.config(text=y)
                player1.append(num)
                x += 1
                bot_click()
                x += 1

        elif x % 2 != 0:
            y = 'O'
            if button9['text'] == 'X' or button9['text'] == 'O':
                bot_click()
                x += 1

            else:
                button9.config(text=y)
                player2.append(num)
        x += 1


def bot_click():
    num = random.randint(1, 9)
    define_sign(num)


root = Tk()

button1 = Button(root, width=20, height=10, command=lambda: define_sign(1), state=DISABLED)
button1.grid(row=1, column=1)

button2 = Button(root, width=20, height=10, command=lambda: define_sign(2), state=DISABLED)
button2.grid(row=1, column=2)

button3 = Button(root, width=20, height=10, command=lambda: define_sign(3), state=DISABLED)
button3.grid(row=1, column=3)

button4 = Button(root, width=20, height=10, command=lambda: define_sign(4), state=DISABLED)
button4.grid(row=4, column=1)

button5 = Button(root, width=20, height=10, command=lambda: define_sign(5), state=DISABLED)
button5.grid(row=4, column=2)

button6 = Button(root, width=20, height=10, command=lambda: define_sign(6), state=DISABLED)
button6.grid(row=4, column=3)

button7 = Button(root, width=20, height=10, command=lambda: define_sign(7), state=DISABLED)
button7.grid(row=8, column=1)

button8 = Button(root, width=20, height=10, command=lambda: define_sign(8), state=DISABLED)
button8.grid(row=8, column=2)

button9 = Button(root, width=20, height=10, command=lambda: define_sign(9), state=DISABLED)
button9.grid(row=8, column=3)

button10 = Button(root, text="Start", width=20, height=3, command=lambda: start())
button10.grid(row=0, column=1)

button11 = Button(root, text="Reset", width=20, height=3, command=lambda: reset(), state=DISABLED)
button11.grid(row=0, column=3)

button12 = Button(root, width=20, height=3, command=lambda: start(), state=DISABLED)
button12.grid(row=0, column=2)

root.mainloop()
