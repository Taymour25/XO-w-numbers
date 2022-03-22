from cProfile import label
from pickle import FRAME
from tkinter import *
from tkinter import Pack
from tkinter import messagebox
import tkinter
from tkinter import font
from tracemalloc import start
from turtle import bgcolor, left, right

#giving a variable of the user a value of true so we will be able to toggle the uder during the code
user=True
turns=0
#intiating the screen
frm =Tk()
frm.title("TIC TAC TOE")
frm.minsize(900,600)
spc=Entry(width=10,font=50,bg='silver')
spc.place(x=550,y=180)
nm= ["0","1","2","3","4","5","6","7","8","9"]
#this function is used to disable all the keys when a player wins 
def dab():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)
#this is the winning function , used for checking the rows&columns
def winning():
    if b1["text"]!="  "and b2["text"]!="  "and b3["text"]!="  ":
     if (int(b1["text"])+(int(b2["text"]))+(int(b3["text"])))==15:
      b1.config(bg='green')
      b2.config(bg='green')
      b3.config(bg='green')
      messagebox.showinfo("WINNER","YOU WON!")
      dab()
    if b4["text"]!="  "and b5["text"]!="  "and b6["text"]!="  ":
     if (int(b4["text"])+(int(b5["text"]))+(int(b6["text"])))==15:
      b4.config(bg='green')
      b5.config(bg='green')
      b6.config(bg='green')
      messagebox.showinfo("WINNER","YOU WON!")
      dab()
    if b7["text"]!="  "and b8["text"]!="  "and b9["text"]!="  ":
     if (int(b7["text"])+int(b8["text"])+int(b9["text"]))==15:
      b7.config(bg='green')
      b8.config(bg='green')
      b9.config(bg='green')

      messagebox.showinfo("WINNER","YOU WON!")
      dab()
    if b1["text"]!="  "and b4["text"]!="  "and b7["text"]!="  ":
     if (int(b1["text"])+int(b4["text"])+int(b7["text"]))==15:
      b1.config(bg='green')
      b4.config(bg='green')
      b7.config(bg='green')

      messagebox.showinfo("WINNER","YOU WON!")
      dab()
    if b2["text"]!="  "and b5["text"]!="  "and b8["text"]!="  ":
     if (int(b5["text"])+int(b2["text"])+int(b8["text"]))==15:
      b5.config(bg='green')
      b2.config(bg='green')
      b8.config(bg='green')
      messagebox.showinfo("WINNER","YOU WON!")
      dab()
    if b3["text"]!="  "and b6["text"]!="  "and b9["text"]!="  ":
     if (int(b6["text"])+int(b9["text"])+int(b3["text"]))==15:
      b6.config(bg='green')
      b9.config(bg='green')
      b3.config(bg='green')
      messagebox.showinfo("WINNER","YOU WON!")
      dab()
#This is the main function made for all of the buttons
def clicked(b):
    global turns,user,player
    if b["text"] =="  " and user==True:
        if int(spc.get())%2!=0 or int(spc.get())>9:
         messagebox.showinfo("Warning","The number you entered is unavailable")
        else:
         b["text"]=spc.get()
         user=not user
         turns+=1
         winning()
    if b["text"] =="  " and user==False:
        if int(spc.get())%2==0 or int(spc.get())>9:
         messagebox.showinfo("Warning","The number you entered is unavailable")
        else:
         b["text"]=spc.get()
         user=not user
         turns+=1
         winning()
#a function for the help button explaining the game
def descrb():
    messagebox.showinfo("description","this is a game of X0 but with numbers \n you choose a number then press the button to place your number")

dscrpt=Button(frm,text="?",bg="yellow",command=descrb)
dscrpt.place(x=600,y=10)
txt=Label(frm,text="ENTER YOUR NUMBER HERE",font=32)
txt.place(x=500,y=100)
 
 #every button int the nine buttons but with diffrent parameter for each 
b1=Button(frm,text="  ",font=34,fg='green',height=10,width=12,bg="grey",command=lambda:clicked(b1))
b2=Button(frm,text="  ",font=34,fg='green',height=10,width=12,bg="grey",command=lambda:clicked(b2))
b3=Button(frm,text="  ",font=34,fg='green',height=10,width=12,bg="grey",command=lambda:clicked(b3))
b4=Button(frm,text="  ",font=34,fg='green',height=10,width=12,bg="grey",command=lambda:clicked(b4))
b5=Button(frm,text="  ",font=34,fg='green',height=10,width=12,bg="grey",command=lambda:clicked(b5))
b6=Button(frm,text="  ",font=34,fg='green',height=10,width=12,bg="grey",command=lambda:clicked(b6))
b7=Button(frm,text="  ",font=34,fg='green',height=10,width=12,bg="grey",command=lambda:clicked(b7))
b8=Button(frm,text="  ",font=34,fg='green',height=10,width=12,bg="grey",command=lambda:clicked(b8))
b9=Button(frm,text="  ",font=34,fg='green',height=10,width=12,bg="grey",command=lambda:clicked(b9))
b1.grid(row=0,column=0)
b2.grid(row=0,column=1)
b3.grid(row=0,column=2)

b4.grid(row=1,column=0)
b5.grid(row=1,column=1)
b6.grid(row=1,column=2)

b7.grid(row=2,column=0)
b8.grid(row=2,column=1)
b9.grid(row=2,column=2)


frm.mainloop()