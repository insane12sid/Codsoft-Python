from tkinter import *
import math

answer = ""
root = ""
root = Tk()
root.title('Calculator App')
answerEntryLbl = StringVar()
Label(root, font=('futura', 25, 'bold'),
textvariable = answerEntryLbl,
justify = LEFT, height=2, width=7).grid(columnspan=4, ipadx=120)
answerFinalLbl = StringVar()
Label(root, font=('futura', 25, 'bold'),
textvariable = answerFinalLbl,
justify = LEFT, height=2, width=7).grid(columnspan = 4 , ipadx=120)

def changeAnswerEntryLbl(entry):
    global answer
    global root
    answer = answer + str(entry)
    root = answer
    answerEntryLbl.set(answer)

def clrAnswerEntryLbl():
    global answer
    global root
    root = answer
    answer = ""
    answerEntryLbl.set(answer)

def evalRoot():
    global answer
    global root
    try:
        sqrtAnswer = math.sqrt(eval(str(root)))
        clrAnswerEntryLbl()
        answerFinalLbl.set(sqrtAnswer)
    except(ValueError,SyntaxError,TypeError, ZeroDivisionError):
        try:
            sqrtAnswer = math.sqrt(eval(str(answer)))
            clrAnswerEntryLbl()
            answerFinalLbl.set(sqrtAnswer)
        except(ValueError,SyntaxError,TypeError,ZeroDivisionError):
            clrAnswerEntryLbl()
            answerFinalLbl.set("Error!")

def evalAnswer():
    global answer
    try:
       eval(answer)
       evaluatedValueAnswerLblGlobal= str(eval(answer))                    
       clrAnswerEntryLbl()
       answerFinalLbl.set(evaluatedValueAnswerLblGlobal)

    except(ValueError,SyntaxError,TypeError, ZeroDivisionError):
        clrAnswerEntryLbl()
        answerFinalLbl.set("Error!")

def allClear():
    global answer
    global root
    answer = ""
    root = ""
    answerEntryLbl.set("")
    answerFinalLbl.set("")

def createBtn(txt,x,y):
    Button(root, font=('futura', 15, 'bold'),
           padx=16,pady=16,text = str(txt),
           command = lambda:changeAnswerEntryLbl(txt),
           height = 2, width=9).grid(row = x , column = y, sticky=E)

buttons = ['AC','√','%','/','7','8','9','*','4','5','6','-','1','2','3','+','','','.','']
buttonsListTraversalCounter = 0

for i in range(3,8):
    for j in range(0,4):
        createBtn(buttons[buttonsListTraversalCounter],i,j)
        buttonsListTraversalCounter =buttonsListTraversalCounter + 1

Button(root,font=('futura', 15, 'bold'),background='blue',
       padx=16,pady=16, text = "√",
       command = lambda:evalRoot(),
       height=2, width=9).grid(row = 3 , column = 1, sticky = E)

Button(root,font=('futura', 15, 'bold'),
       padx=16,pady=16, text = "AC",
       command = lambda:allClear(),
       height=2, width=9).grid(row = 3 , column = 0 , sticky = E)

Button(root,font=('futura', 15, 'bold'),
       padx=16,pady=16, text = "0",
       command = lambda:changeAnswerEntryLbl(0),
       height=2, width=21).grid(row = 7 , column = 0 ,
       columnspan=2 , sticky = E)

Button(root,font=('futura', 15, 'bold'),
       padx=16,pady=16, text = "=",
       command = lambda:evalAnswer(),
       height=2, width=9).grid(row = 7 , column = 3, sticky = E)

root.mainloop()
