#CodeSoft task-2 (Creating Calculator using tkinter)
from tkinter import *
root=Tk()
root.geometry("555x333")

mainframe=Frame(root,width=45,bd=10,relief=RIDGE,bg="blue")
mainframe.pack()
drum=Frame(mainframe,width=45,bd=10,relief=RIDGE,bg="black")
drum.pack()


e=Entry(drum,width=65,borderwidth=5)
e.grid(row=0,column=0,columnspan=4,padx=10,pady=1)


def onclick(num):
 x=e.get()
 e.delete(0,END)
 e.insert(0,str(x)+str(num)) 

 
def clear():
 e.delete(0,END)

 
def add():
 global first,op
 op='+'
 first=e.get()
 e.delete(0,END)

 
def sub():
 global first,op
 op='-'
 first=e.get()
 e.delete(0,END)

 
def mul():
 global first,op
 op='*'
 first=e.get()
 e.delete(0,END)


def div():
 global first,op
 op='/'
 first=e.get()
 e.delete(0,END)

def root():
 global first,op
 op='?'
 first=e.get()
 e.delete(0,END)

 
def equal():
 second=e.get()
 if op=='+':
  result=float(first)+float(second)
 elif op=='-':
  result=float(first)-float(second)
 elif op=='*':
  result=float(first)*float(second)
 elif op=='/':
  result=float(first)/float(second)
 elif op=='?':
  result=(float(first))*1/2
 e.delete(0,END)
 e.insert(0,result)


############################################################
 ####Button widget####
b1=Button(drum,text='1',padx=30,pady=10,relief=RIDGE,font=15,width=4,command=lambda:onclick(1))
b1.grid(row=3,column=0)
b2=Button(drum,text='2',padx=30,pady=10,relief=RIDGE,font=15,width=4,command=lambda:onclick(2))
b2.grid(row=3,column=1)
b3=Button(drum,text='3',padx=30,pady=10,relief=RIDGE,font=15,width=4,command=lambda:onclick(3))
b3.grid(row=3,column=2)
b4=Button(drum,text='4',padx=30,pady=10,relief=RIDGE,font=15,width=4,command=lambda:onclick(4))
b4.grid(row=2,column=0)
b5=Button(drum,text='5',padx=30,pady=10,relief=RIDGE,font=15,width=4,command=lambda:onclick(5))
b5.grid(row=2,column=1)
b6=Button(drum,text='6',padx=30,pady=10,relief=RIDGE,font=15,width=4,command=lambda:onclick(6))
b6.grid(row=2,column=2)
b7=Button(drum,text='7',padx=30,pady=10,relief=RIDGE,font=15,width=4,command=lambda:onclick(7))
b7.grid(row=1,column=0)
b8=Button(drum,text='8',padx=30,pady=10,relief=RIDGE,font=15,width=4,command=lambda:onclick(8))
b8.grid(row=1,column=1)
b9=Button(drum,text='9',padx=30,pady=10,relief=RIDGE,font=15,width=4,command=lambda:onclick(9))
b9.grid(row=1,column=2)
b0=Button(drum,text='0',padx=30,pady=10,relief=RIDGE,font=15,width=4,command=lambda:onclick(0))
b0.grid(row=4,column=0)


# operation button
b_add=Button(drum,text='+',padx=30,pady=10,relief=RIDGE,font=15,width=4,command=add)
b_add.grid(row=1,column=3)
b_sub=Button(drum,text='-',padx=30,pady=10,relief=RIDGE,font=15,width=4,command=sub)
b_sub.grid(row=2,column=3)
b_mul=Button(drum,text='*',padx=30,pady=10,relief=RIDGE,font=15,width=4,command=mul)
b_mul.grid(row=3,column=3)
b_div=Button(drum,text='/',padx=30,pady=10,relief=RIDGE,font=15,width=4,command=div)
b_div.grid(row=4,column=3)
b_equal=Button(drum,text='=',padx=30,pady=10,relief=RIDGE,font=15,width=4,command=equal)
b_equal.grid(row=4,column=2)
b_clear=Button(drum,text='C',padx=30,pady=10,relief=RIDGE,font=15,width=4,command=clear)
b_clear.grid(row=4,column=1)
b_root=Button(drum,text='?',padx=30,pady=10,relief=RIDGE,font=15,width=4,command=root)
b_root.grid(row=5,column=3)

root.mainloop()  