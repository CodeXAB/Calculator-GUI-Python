from tkinter import *

calculation = ""

def add_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0,"end")
    text_result.insert(1.0,calculation)

def eval_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0,"end")
        text_result.insert(1.0,calculation)
    except:
        clear_field()
        text_result.insert(1.0,"Error")

def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")

root = Tk()
root.geometry("430x350")
root.resizable(False,False)
text_result = Text(root,height=2, width=27, font=("arial",20))
text_result.grid(columnspan=4)

button1 = Button(root,text="1", command=lambda: add_calculation(1), width=5,font=("arial",20))
button1.grid(row=1,column=0)
button2 = Button(root,text="2", command=lambda: add_calculation(2), width=5,font=("arial",20))
button2.grid(row=1,column=1)
button3 = Button(root,text="3", command=lambda: add_calculation(3), width=5,font=("arial",20))
button3.grid(row=1,column=2)
button4 = Button(root,text="4", command=lambda: add_calculation(4), width=5,font=("arial",20))
button4.grid(row=2,column=0)
button5 = Button(root,text="5", command=lambda: add_calculation(5), width=5,font=("arial",20))
button5.grid(row=2,column=1)
button6 = Button(root,text="6", command=lambda: add_calculation(6), width=5,font=("arial",20))
button6.grid(row=2,column=2)
button7 = Button(root,text="7", command=lambda: add_calculation(7), width=5,font=("arial",20))
button7.grid(row=3,column=0)
button8 = Button(root,text="8", command=lambda: add_calculation(8), width=5,font=("arial",20))
button8.grid(row=3,column=1)
button9 = Button(root,text="9", command=lambda: add_calculation(9), width=5,font=("arial",20))
button9.grid(row=3,column=2)
button0 = Button(root,text="0", command=lambda: add_calculation(0), width=5,font=("arial",20))
button0.grid(row=4,column=1)
button_plus = Button(root,text="+", command=lambda: add_calculation("+"), width=5,font=("arial",20))
button_plus.grid(row=1,column=3)
button_minus = Button(root,text="-", command=lambda: add_calculation("-"), width=5,font=("arial",20))
button_minus.grid(row=2,column=3)
button_multiply = Button(root,text="x", command=lambda: add_calculation("*"), width=5,font=("arial",20))
button_multiply.grid(row=3,column=3)
button_divide = Button(root,text="/", command=lambda: add_calculation("/"), width=5,font=("arial",20))
button_divide.grid(row=4,column=3)
button_open = Button(root,text="(", command=lambda: add_calculation("("), width=5,font=("arial",20))
button_open.grid(column=0,row=4)
button_closed = Button(root,text=")", command=lambda: add_calculation(")"), width=5,font=("arial",20))
button_closed.grid(column=2,row=4)
button_equal = Button(root,text="=", command=eval_calculation, width=13,font=("arial",20))
button_equal.grid(column=2,row=5,columnspan=2)
button_clear = Button(root,text="C", command=clear_field, width=13,font=("arial",20))
button_clear.grid(column=0,row=5,columnspan=2)

root.mainloop()