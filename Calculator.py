from tkinter import *

root = Tk()
root.title("Simple Calculator")
root.iconbitmap("Calculator.ico")

def key_event(event):
    key = event.char
    if key and key in "0123456789c+-*/.%^":
        button_click(key)
    elif key == '=' or event.keysym == 'Return':
        button_equal()
    elif event.keysym == 'BackSpace':
        button_backspace()

root.bind("<Key>", key_event)

entry = Entry(root, width = 23, borderwidth = 3)
entry.grid(row = 0, column = 0, columnspan = 4)

def button_click(val):
    global f_num
    global math

    if val == 'c':
        entry.delete(0, END)
        return
    
    elif val in "+-*/%^":
        try:
            f_num = float(entry.get())

        except ValueError:
            entry.delete(0, END)
            entry.insert(0, "Error")
            return

        math = val
        entry.delete(0, END)
        return
    
    elif val == '.':
        num = entry.get()
        if '.' not in num:
            entry.insert(END, '.')
            return

    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(val))

def button_equal():
    try:
        s_num = float(entry.get())

    except ValueError:
        entry.delete(0, END)
        return
    
    match math:
        case '+':
            total = f_num + s_num
            
        case '-':
            total = f_num - s_num

        case '*':
            total = f_num * s_num

        case '/':
            try:
                total = f_num / s_num
            except ZeroDivisionError:
                entry.delete(0, END)
                entry.insert(0, "Error")
                return
            
        case '%':
            total = (f_num * int(entry.get())) / 100

        case '^':
            total = f_num ** s_num

    entry.delete(0, END)
    entry.insert(0, total)

def button_backspace():
    current = entry.get()
    if current:
        entry.delete(len(current) - 1, END)

button_0 = Button(root, text = '0', padx = 30, pady = 20, command = lambda: button_click('0')).grid(row = 6, column = 1)
button_1 = Button(root, text = '1', padx = 30, pady = 20, command = lambda: button_click('1')).grid(row = 5, column = 0)
button_2 = Button(root, text = '2', padx = 30, pady = 20, command = lambda: button_click('2')).grid(row = 5, column = 1)
button_3 = Button(root, text = '3', padx = 30, pady = 20, command = lambda: button_click('3')).grid(row = 5, column = 2)
button_4 = Button(root, text = '4', padx = 30, pady = 20, command = lambda: button_click('4')).grid(row = 4, column = 0)
button_5 = Button(root, text = '5', padx = 30, pady = 20, command = lambda: button_click('5')).grid(row = 4, column = 1)
button_6 = Button(root, text = '6', padx = 30, pady = 20, command = lambda: button_click('6')).grid(row = 4, column = 2)
button_7 = Button(root, text = '7', padx = 30, pady = 20, command = lambda: button_click('7')).grid(row = 3, column = 0)
button_8 = Button(root, text = '8', padx = 30, pady = 20, command = lambda: button_click('8')).grid(row = 3, column = 1)
button_9 = Button(root, text = '9', padx = 30, pady = 20, command = lambda: button_click('9')).grid(row = 3, column = 2)

button_mul = Button(root, text = '*', padx = 30, pady = 20, command = lambda: button_click('*')).grid(row = 3, column = 3)
button_sub = Button(root, text = '-', padx = 30, pady = 20, command = lambda: button_click('-')).grid(row = 4, column = 3)
button_add = Button(root, text = '+', padx = 29, pady = 20, command = lambda: button_click('+')).grid(row = 5, column = 3)
button_div = Button(root, text = '/', padx = 31, pady = 20, command = lambda: button_click('/')).grid(row = 1, column = 2)

button_percent = Button(root, text = '%', padx = 28, pady = 20, command = lambda: button_click('%')).grid(row = 1, column = 0)
button_power = Button(root, text = 'x^y', padx = 23, pady = 20, command = lambda: button_click('^')).grid(row = 1, column = 1)
button_back = Button(root, text = '←', padx = 27, pady = 20, command = button_backspace).grid(row = 1, column = 3)
button_ans = Button(root, text = '=', padx = 29, pady = 20, command = button_equal).grid(row = 6, column = 3)
button_clear = Button(root, text = 'C', padx = 29, pady = 20, command = lambda: button_click('c')).grid(row = 6, column = 0)
button_point = Button(root, text = ". ", padx = 30, pady = 20, command = lambda: button_click('.')).grid(row = 6, column = 2)

root.mainloop()