from tkinter import *
from tkinter import messagebox


root=Tk()
root.title("Bill Managing System__2")
root.geometry('1280x720')
root.config(bg='pink')

#==============================================Title===================================================

title=Label(root,text='Bill Managing System',bg='green3',fg="white",font=("Gabriola",39,"bold"),relief=GROOVE,bd=12)
title.pack(fill=X)

#============================================variable======================================================

Pizza=IntVar()
Pizza2=IntVar()
Pizza3=IntVar()
Pizza4=IntVar()
Pizza5=IntVar()
total=IntVar()

po=StringVar()
po2=StringVar()
po3=StringVar()
po4=StringVar()
po5=StringVar()
total_cost=StringVar()

#=====================================Function==========================================================

def Total():
    if Pizza.get()==0 and Pizza2.get()==0 and Pizza3.get()==0 and Pizza4.get()==0 and Pizza5.get()==0:
        messagebox.showerror("Error","Please Select Number of Quantity")
    else:
        a=Pizza.get()
        b=Pizza2.get()
        c=Pizza3.get()
        d=Pizza4.get()
        e=Pizza5.get()
        t=total.get()
        
        t=float(a*100+b*150+c*150+d*60+e*120)
        total.set(a+b+c+d+e)
        total_cost.set(str(round(t,4)))

        po.set('$'+str(round(a*100,4)))
        po2.set('$'+str(round(b*150,4)))
        po3.set('$'+str(round(c*150,4)))
        po4.set('$'+str(round(d*60,4)))
        po5.set('$'+str(round(e*120,4)))


def receipt():
    textarea.delete(1.0,END)
    textarea.insert(END,'Items\tNumber of Items \tCost of Item')
    textarea.insert(END,f'\n\nCheese Pizza\t\t{Pizza.get()}\t {po.get()}')
    textarea.insert(END,f'\n\nItalian Pizza\t\t{Pizza2.get()}\t {po2.get()}')
    textarea.insert(END,f'\n\nPanir Pizza\t\t{Pizza3.get()}\t {po3.get()}')
    textarea.insert(END,f'\n\nVeg Burger\t\t{Pizza4.get()}\t {po4.get()}')
    textarea.insert(END,f'\n\nMomozr\t\t{Pizza5.get()}\t {po5.get()}')
    textarea.insert(END,'\n\n================================')
    textarea.insert(END,f'\nTotal Price\t\t{total.get()}\t{total_cost.get()}')
    textarea.insert(END,'\n================================')


def print():
    q=textarea.get('1.0',END)
    f1=open('jp.txt','w')
    f1.write(q)
    f1.close()

def reset():
    textarea.delete(1.0,END)
    Pizza.set(0)
    Pizza2.set(0)
    Pizza3.set(0)
    Pizza4.set(0)
    Pizza5.set(0)
    total.set(0)

    po.set('')
    po2.set('')
    po3.set('')
    po4.set('')
    po5.set('')
    total_cost.set('')

def exit():
    if messagebox.askyesno('Exit','Do you really want to exit'):
        root.destroy()



#==============================Product details================================================

F1=Frame(root,bg='#008080',bd=12,relief=RIDGE)
F1.place(x=5,y=125,width=830,height=470)

itm=Label(F1,text='Items',font=("Helvetic",25,"bold",'underline'),fg='black',bg='#008080',)
itm.grid(row=0,column=0,padx=20,pady=15)

n=Label(F1,text='Number Of Items',font=("Helvetic",25,"bold",'underline'),fg='black',bg='#008080',)
n.grid(row=0,column=1,padx=20,pady=15)

c=Label(F1,text='Cost of Items',font=("Helvetic",25,"bold",'underline'),fg='black',bg='#008080',)
c.grid(row=0,column=2,padx=20,pady=15)

pizza=Label(F1,text='Cheese Pizza',font=("Lucida Calligraphy",20,"bold"),fg='white',bg='#008080')
pizza.grid(row=1,column=0,padx=20,pady=15)
p_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,justify=CENTER,textvariable=Pizza)
p_txt.grid(row=1,column=1,padx=20,pady=15)
po_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,justify=CENTER,textvariable=po)
po_txt.grid(row=1,column=2,padx=0,pady=1)


pizza2=Label(F1,text='Italian Pizza',font=("Lucida Calligraphy",20,"bold"),fg='white',bg='#008080')
pizza2.grid(row=2,column=0,padx=20,pady=15)
p2_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,justify=CENTER,textvariable=Pizza2)
p2_txt.grid(row=2,column=1,padx=20,pady=15)
po2_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,justify=CENTER,textvariable=po2)
po2_txt.grid(row=2,column=2,padx=20,pady=15)


pizza3=Label(F1,text='Panir Pizza',font=("Lucida Calligraphy",20,"bold"),fg='white',bg='#008080')
pizza3.grid(row=3,column=0,padx=20,pady=15)
p_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,justify=CENTER,textvariable=Pizza3)
p_txt.grid(row=3,column=1,padx=20,pady=15)
po3_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,justify=CENTER,textvariable=po3)
po3_txt.grid(row=3,column=2,padx=20,pady=15)


pizza4=Label(F1,text='Veg Burger',font=("Lucida Calligraphy",20,"bold"),fg='white',bg='#008080')
pizza4.grid(row=4,column=0,padx=20,pady=15)
p4_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,justify=CENTER,textvariable=Pizza4)
p4_txt.grid(row=4,column=1,padx=20,pady=15)
po4_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,justify=CENTER,textvariable=po4)
po4_txt.grid(row=4,column=2,padx=20,pady=15)

pizza5=Label(F1,text='Momoz',font=("Lucida Calligraphy",20,"bold"),fg='white',bg='#008080')
pizza5.grid(row=5,column=0,padx=20,pady=15)
p5_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,justify=CENTER,textvariable=Pizza5)
p5_txt.grid(row=5,column=1,padx=20,pady=15)
po5_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,justify=CENTER,textvariable=po5)
po5_txt.grid(row=5,column=2,padx=20,pady=15)


#===================================BIll AREA==============================================

F2=Frame(relief='groove',bd=10)
F2.place(x=850,y=125,width=430,height=470)
bill_title=Label(F2,text='Receipt',font='arial 20 bold',bd=7,relief=GROOVE).pack(fill=X)
scroll=Scrollbar(F2,orient=VERTICAL)
scroll.pack(side=RIGHT,fill=Y)
textarea=Text(F2,font='arial 15 bold',yscrollcommand=scroll.set)
textarea.pack(fill=BOTH)
scroll.config(command=textarea.yview)


#===============================button================================================

F3=Frame(root,relief='groove',bd=10,bg='green3')
F3.place(x=5,y=600,width=1240,height=90)

btn=Button(F3,text='Total',font='arial 15 bold',bg='yellow',fg='crimson',padx=5,pady=5,width='15',command=Total)
btn.grid(row=0,column=0,padx=13,pady=5)

btn2=Button(F3,text='Receipt',font='arial 15 bold',bg='yellow',fg='crimson',padx=5,pady=5,width='15',command=receipt)
btn2.grid(row=0,column=2,padx=30,pady=5)

btn3=Button(F3,text='Reset',font='arial 15 bold',bg='yellow',fg='crimson',padx=5,pady=5,width='15',command=reset)
btn3.grid(row=0,column=3,padx=30,pady=5)

btn4=Button(F3,text='Print',font='arial 15 bold',bg='yellow',fg='crimson',padx=5,pady=5,width='15',command=print)
btn4.grid(row=0,column=4,padx=30,pady=5)

btn5=Button(F3,text='Exit',font='arial 15 bold',bg='yellow',fg='crimson',padx=5,pady=5,width='15',command=exit)
btn5.grid(row=0,column=5,padx=21,pady=5)














root.mainloop()