from tkinter import *
from tkinter import messagebox as mb


#========================================================= Classes
class numButton:
    def __init__(self, number):
        self.number = number

    def call(self):
        if answer_status == False:
            if operation == False:
                global n, m
                n += self.number
                results.config(text=n)
            else:
                m += self.number
                results2.config(text=m)
        else:
            pass

button1 = numButton('1')
button2 = numButton('2')
button3 = numButton('3')
button4 = numButton('4')
button5 = numButton('5')
button6 = numButton('6')
button7 = numButton('7')
button8 = numButton('8')
button9 = numButton('9')
button0 = numButton('0')
buttondot = numButton('.')
#================================================================
window = Tk()
window.title('Calculator')
window.geometry('300x400+1000+200')
window.minsize(297, 505)
window.maxsize(297, 505)
# menus
def about():
    mb.showinfo('About This Calculator', 'This calculator was written by\
                 \"Ali J Rad\" using Python 3.8.8')


menubar = Menu(window)
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Check me out!', menu=filemenu)
filemenu.add_command(label='About', command=about)
filemenu.add_command(label='Exit', command=window.quit)



# results in frame1
frame1 = Frame(window, bg='#1a0033', bd=5, )
frame1.pack(fill=BOTH,)
# frame for results

r_frame = LabelFrame(window, text='Results', bg='#dbd2f9')
r_frame.pack(fill=BOTH, expand=True)

#results label
results = Label(frame1, text='0', fg='#dbd2f9', bg='#1a0033',\
                font='times 30')
results.pack()

sign = Label(frame1, text='', fg='#dbd2f9', bg='#1a0033',\
                font='times 40')
sign.pack()

results2 = Label(frame1, text='', fg='#dbd2f9', bg='#1a0033',\
                font='times 30')
results2.pack()

final = Label(r_frame, text='', fg='black', bg='#dbd2f9',\
                font='times 40')
final.pack()

#frame2 for buttons
frame2 = Frame(window, bg='#dbd2f9', bd=0, )
frame2.pack(side='bottom', fill=BOTH,)







# =============> constants

n = ''
operation = False
answer_status = False
operator = ''
m = ''

# =============> operation functions
def _ac_push():
    global n, m, operator, operation, answer, answer_status
    answer_status = False
    answer = ''
    n = ''
    m = ''
    operator = ''
    operation = False
    results.config(text='0')
    results2.config(text=m)
    sign.config(text=operator)
    final.config(text=answer)
def _del_push():
    global answer
    if answer_status == False:
        if operation == False:
            global n, m
            if n !='':
                n = n[:-1]
                results.config(text=n)
            elif n=='':
                results.config(text='0')
        else:
            m = m[:-1]
            results2.config(text=m)
    elif answer_status == True:
        if answer == int(answer):
            answer = str(int(answer))[:-1]
            final.config(text=answer)
        else:
            answer = str(answer)[:-1]
            final.config(text=answer)
def _plus_push():
    global operation, operator
    if n!='':
        if operation == False:
            operation = True
            operator = '+'
            sign.config(text='+')
        else:
            pass
    else:
        pass
def _minus_push():
    global operation, operator 
    if n!='':   
        if operation == False:
            operation = True
            operator = '-'
            sign.config(text='-')
        else:
            pass
    else:
        pass
def _mult_push():
    global operation, operator
    if n!='':
        if operation == False:
            operation = True
            operator = '*'
            sign.config(text='*')
        else:
            pass
    else:
        pass
def _div_push():
    global operation, operator
    if n!='':
        if operation == False:
            operation = True
            operator = '/'
            sign.config(text='/')
        else:
            pass
    else:
        pass
last_answer = ''
def _m_push():
    global m, n, answer, answer_status, operation, last_answer
    if answer_status == True:
        last_answer = answer
    elif answer_status == False:
        if operation == False:
            if last_answer !='':
                n = last_answer
                if n == int(n):
                    results.config(text=str(int(n)))
                    n = str(int(n))  # to be able to del the number
                else:
                    results.config(text=str(n))
                    n = str(n)
            else:
                pass
        elif operation == True:
            if last_answer !='':
                m = last_answer
                if m == int(m):
                    results2.config(text=str(int(m)))
                    m = str(int(m))
                else:
                    results2.config(text=str(m))
                    m = str(m)
            else:
                pass
def _neg_push():
    global m, n
    if answer_status == True:
        pass
    else:
        if operation == False:
            if '-' in n:
                n = n.replace('-', '')
                results.config(text=n)
            elif '-' not in n:
                n = '-' + n
                results.config(text=n)
        elif operation == True:
            if '-' in m:
                m = m.replace('-', '')
                results2.config(text=m)
            elif '-' not in m:
                m = '-' + m
                results2.config(text=m)

def _equ_push():
    global n, m, operator, answer_status, answer
    if m!='':
        answer_status = True
        if operator =='+':
            int_n = float(n)
            int_m = float(m)
            answer = int_n + int_m
            if answer == int(answer):
                final.config(text=str(int(answer)))
            else:
                final.config(text=str(float(answer)))
        elif operator =='-':
            int_n = float(n)
            int_m = float(m)
            answer = int_n - int_m
            if answer == int(answer):
                final.config(text=str(int(answer)))
            else:
                final.config(text=str(float(answer)))
        elif operator =='*':
            int_n = float(n)
            int_m = float(m)
            answer = int_n * int_m
            if answer == int(answer):
                final.config(text=str(int(answer)))
            else:
                final.config(text=str(float(answer)))
        elif operator =='/':
            int_n = float(n)
            int_m = float(m)
            try:
                answer = int_n / int_m
                if answer == int(answer):
                    final.config(text=str(int(answer)))
                else:
                    final.config(text=str(float(answer)))
            except:
                mb.showerror('Division Error', 'Can\'t divide by zero! Try again.')
                _ac_push()
    else:
        pass
# ==========================>> buttons

b7 = Button(frame2, text = '7', fg='#8533ff', command=button7.call, \
     relief="groove",padx=14, pady=10, font='arial 20', bg='#dbd2f9')
b7.grid(row=1, column=0)

b8 = Button(frame2, text = '8', fg='#8533ff', command=button8.call, \
     relief="groove",padx=14, pady=10, font='arial 20', bg='#dbd2f9')
b8.grid(row=1, column=1)

b9 = Button(frame2, text = '9', fg='#8533ff', command=button9.call, \
     relief="groove",padx=14, pady=10, font='arial 20', bg='#dbd2f9')
b9.grid(row=1, column=2)

b4 = Button(frame2, text = '4', fg='#8533ff', command=button4.call, \
     relief="groove",padx=14, pady=10, font='arial 20', bg='#dbd2f9')
b4.grid(row=2, column=0)

b5 = Button(frame2, text = '5', fg='#8533ff', command=button5.call, \
     relief="groove",padx=14, pady=10, font='arial 20', bg='#dbd2f9')
b5.grid(row=2, column=1)

b6 = Button(frame2, text = '6', fg='#8533ff', command=button6.call, \
     relief="groove",padx=14, pady=10, font='arial 20', bg='#dbd2f9')
b6.grid(row=2, column=2)

b1 = Button(frame2, text = '1', fg='#8533ff', command=button1.call, \
     relief="groove",padx=14, pady=10, font='arial 20', bg='#dbd2f9')
b1.grid(row=3, column=0)

b2 = Button(frame2, text = '2', fg='#8533ff', command=button2.call, \
     relief="groove",padx=14, pady=10, font='arial 20', bg='#dbd2f9')
b2.grid(row=3, column=1)

b3 = Button(frame2, text = '3', fg='#8533ff', command=button3.call, \
     relief="groove",padx=14, pady=10, font='arial 20', bg='#dbd2f9')
b3.grid(row=3, column=2)

b_dot = Button(frame2, text = '.', fg='#8533ff', command=buttondot.call, \
     relief="groove",padx=17, pady=10, font='arial 20', bg='#dbd2f9')
b_dot.grid(row=4, column=0)

b0 = Button(frame2, text = '0', fg='#8533ff', command=button0.call, \
     relief="groove",padx=14, pady=10, font='arial 20', bg='#dbd2f9')
b0.grid(row=4, column=1)

b_equ = Button(frame2, text = '=', fg='#8533ff', command= _equ_push, \
     relief="groove",padx=14, pady=10, font='arial 20', bg='#dbd2f9')
b_equ.grid(row=4, column=2)

b_plus = Button(frame2, text = '+', fg='#8533ff', command=_plus_push, \
     relief="groove",padx=14.5, pady=10, font='arial 20', bg='#dbd2f9')
b_plus.grid(row=3, column=3)

b_minus = Button(frame2, text = '-', fg='#8533ff', command= _minus_push, \
     relief="groove",padx=17.5, pady=10, font='arial 20', bg='#dbd2f9')
b_minus.grid(row=2, column=3)

b_mult = Button(frame2, text = '*', fg='#8533ff', command= _mult_push, \
    relief="groove",padx=17.4, pady=10, font='arial 20', bg='#dbd2f9')
b_mult.grid(row=1, column=3)

b_div = Button(frame2, text = '/', fg='#8533ff', command=_div_push, \
     relief="groove",padx=17.5, pady=11, font='arial 20', bg='#dbd2f9')
b_div.grid(row=0, column=3)

b_ac = Button(frame2, text = 'AC', fg='#8533ff', command=_ac_push, \
     relief="groove",padx=9.3, pady=14, font='arial 15', bg='#dbd2f9')
b_ac.grid(row=0, column=0,)

b_neg = Button(frame2, text = '-/+', fg='#8533ff', command=_neg_push, \
     relief="groove",padx=11.3, pady=14, font='arial 15', bg='#dbd2f9')
b_neg.grid(row=0, column=1,)

b_del = Button(frame2, text = 'DEL', fg='#8533ff', command=_del_push, \
     relief="groove",padx=5, pady=14, font='arial 15', bg='#dbd2f9')
b_del.grid(row=0, column=2,)

b_M = Button(frame2, text = 'M+', fg='#8533ff', command=_m_push, \
     relief="groove",padx=7, pady=10, font='arial 20', bg='#dbd2f9')
b_M.grid(row=4, column=3)

# ===========================> buttons

window.config(menu=menubar)
window.mainloop()

