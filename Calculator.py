
# This line imports the Tkinter library, which is used to create graphical user interfaces.
from tkinter import *

# TK is consider as class TK is used to create window

# window is object name
window=Tk() # create object of TK class
window.geometry('350x330') # sets the initial size of the window to 350x330 pixels.
window.title('Calculator') #sets the title of the window to "Calculator."
window.resizable(False,False) # prevents resizing the window.

val=""#empty variables
data=StringVar()#crate object of string var class(display the content in the textbox)


# This creates an Entry widget at the top of the window where the input and result are displayed. 
# The textvariable is set to data to link the widget's text to the StringVar variable.

def btnClick(number):#use lambda for calling as it has parameters
    global val #you can access the variable in another function also
    val=val+str(number)#store it in val and concat with str
    data.set(val)#set the value in the textbox using text variable

def btnClear():
    global val
    val=""
    data.set(val)

def btnEquals():
    global val
    val=str(eval(val))
    data.set(val)



e1=Entry(window,textvariable=data,justify="right",width=50,bd=20,bg='yellow')
e1.grid(row=0,columnspan=4)

btn9=Button(window,text='7',bd=10,font=('arial',12,'bold'),width=6,height=2,command=lambda:btnClick(7))
btn9.grid(row=1,column=0)

btn8=Button(window,text='8',bd=10,font=('arial',12,'bold'),width=6,height=2,command=lambda:btnClick(8))
btn8.grid(row=1,column=1)

btn7=Button(window,text='9',bd=10,font=('arial',12,'bold'),width=6,height=2,command=lambda:btnClick(9))
btn7.grid(row=1,column=2)

btn99=Button(window,text='+',bd=10,font=('arial',12,'bold'),width=6,height=2,command=lambda:btnClick('+'))
btn99.grid(row=1,column=3)

btn6=Button(window,text='4',bd=10,font=('arial',12,'bold'),width=6,height=2,command=lambda:btnClick(4))
btn6.grid(row=2,column=0)

btn5=Button(window,text='5',bd=10,font=('arial',12,'bold'),width=6,height=2,command=lambda:btnClick(5))
btn5.grid(row=2,column=1)

btn4=Button(window,text='6',bd=10,font=('arial',12,'bold'),width=6,height=2,command=lambda:btnClick(6))
btn4.grid(row=2,column=2)

btn44=Button(window,text='*',bd=10,font=('arial',12,'bold'),width=6,height=2,command=lambda:btnClick('*'))
btn44.grid(row=2,column=3)

btn3=Button(window,text='1',bd=10,font=('arial',12,'bold'),width=6,height=2,command=lambda:btnClick(1))
btn3.grid(row=3,column=0)

btn2=Button(window,text='2',bd=10,font=('arial',12,'bold'),width=6,height=2,command=lambda:btnClick(2))
btn2.grid(row=3,column=1)

btn1=Button(window,text='3',bd=10,font=('arial',12,'bold'),width=6,height=2,command=lambda:btnClick(3))
btn1.grid(row=3,column=2)

btn17=Button(window,text='-',bd=10,font=('arial',12,'bold'),width=6,height=2,command=lambda:btnClick('-'))
btn17.grid(row=3,column=3)

btn16=Button(window,text='CE',bd=10,font=('arial',12,'bold'),width=6,height=2,command=btnClear)
btn16.grid(row=4,column=0)

btn14=Button(window,text='0',bd=10,font=('arial',12,'bold'),width=6,height=2,command=lambda:btnClick(0))
btn14.grid(row=4,column=1)

btn13=Button(window,text='/',bd=10,font=('arial',12,'bold'),width=6,height=2,command=lambda:btnClick('/'))
btn13.grid(row=4,column=2)

btn12=Button(window,text='=',bd=10,font=('arial',12,'bold'),width=6,height=2,command=btnEquals)
btn12.grid(row=4,column=3)

window.mainloop()









