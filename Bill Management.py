from tkinter import *
root=Tk()
root.geometry("1000x500")
root.title("Bill Management")
root.resizable(False,False)

def Reset():
    entry_pizza.delete(0,END)
    entry_Paneer_Pizza.delete(0,END)
    entry_Hot_Dog.delete(0,END)
    entry_Noodles.delete(0,END)
    entry_Panir_Momoz.delete(0,END)
    entry_Puff.delete(0,END)
    entry_Veg_Burger.delete(0,END)

def Total():
        try:a1=int(Cheese_Pizza.get())
        except: a1=0

        try:a2=int(Paneer_Pizza.get())
        except:a2=0

        try:a3=int(Hot_Dog.get())
        except:a3=0

        try:a4=int(Veg_Burger.get())
        except:a4=0

        try:a5=int(Puff.get())
        except:a5=0

        try:a6=int(Panir_Momoz.get())
        except:a6=0

        try:a7=int(Noodles.get())
        except:a7=0
        # price
        c1=100*a1
        c2=a2*150
        c3=a3*75
        c4=a4*60
        c5=a5*20
        c6=a6*40
        c7=a7*59

        lbl_total=Label(f2,font=('aria',20,'bold'),text="Total",width=18,fg="black",bg="darkolivegreen4")
        lbl_total.place(x=0,y=50)

        entry_total=Entry(f2,font=('aria',20,'bold'),textvariable=Total_bill,bd=6,width=15,bg="lightgreen")
        entry_total.place(x=20,y=100)

        totalcost=c1+c2+c3+c4+c5+c6+c7
        string_bill="Rs.",str('%.2f'%totalcost)
      
        Total_bill.set(string_bill)

#-----------------------------x  Main Title  x--------------------------------------------------------
    
    

Label(text="Zorko Billing System",bg="red",fg="white",font=("calibri",33),width="300",height="2").pack()


# -----------------------------------x  Menu card  x-----------------------------------------------


f=Frame(root,bg="lightgreen",highlightbackground="black",highlightthickness=2,width=300,height=370)
f.place(x=10,y=120)

Label(f,text="Menu",font=("Gabriola",48,"bold"),fg="black",bg="lightgreen").place(x=100,y=0)

Label(f,font=("Lucida Calligraphy",15,'bold'),text="Cheese Pizza.....Rs.100\-",fg="black",bg="lightgreen").place(x=10,y=90)
Label(f,font=("Lucida Calligraphy",15,'bold'),text="Paneer Pizza.....Rs.150\-",fg="black",bg="lightgreen").place(x=10,y=120)
Label(f,font=("Lucida Calligraphy",15,'bold'),text="Hot Dog.........Rs.75.00\-",fg="black",bg="lightgreen").place(x=10,y=150)
Label(f,font=("Lucida Calligraphy",15,'bold'),text="Veg Burger.......Rs.60\-",fg="black",bg="lightgreen").place(x=10,y=180)
Label(f,font=("Lucida Calligraphy",15,'bold'),text="Puff................Rs.20\-",fg="black",bg="lightgreen").place(x=10,y=210)
Label(f,font=("Lucida Calligraphy",15,'bold'),text="Panir Momoz..Rs.40\-",fg="black",bg="lightgreen").place(x=10,y=240)
Label(f,font=("Lucida Calligraphy",15,'bold'),text="Noodles.......Rs.59\-",fg="black",bg="lightgreen").place(x=10,y=270)


#----------------------------------x  Entry Work  x---------------------------------------------------------


f1=Frame(root,bd=5,bg="antiquewhite1",highlightbackground="black",highlightthickness=2,height=370,width=300,relief=RAISED)
f1.place(x=320,y=120)

Cheese_Pizza=StringVar()
Paneer_Pizza=StringVar()
Hot_Dog=StringVar()
Veg_Burger=StringVar()
Puff=StringVar()
Panir_Momoz=StringVar()
Noodles=StringVar()
Total_bill=StringVar()

#--------------------------------------x  Label  x-------------------------------------------------------------------


lbl_cheese_pizza=Label(f1,text="Cheese Pizza",font=("Verdana",15,'bold'),width=12,fg="black",bg="antiquewhite1")
lbl_Paneer_Pizza=Label(f1,text="Paneer Pizza",font=("Verdana",15,'bold'),width=12,fg="black",bg="antiquewhite1")
lbl_Hot_Dog=Label(f1,text="Hot Dog",font=("Verdana",15,'bold'),width=12,fg="black",bg="antiquewhite1")
lbl__Veg_Burger=Label(f1,text="Veg Burger",font=("Verdana",15,'bold'),width=12,fg="black",bg="antiquewhite1")
lbl_Puff=Label(f1,text="Puff",font=("Verdana",15,'bold'),width=12,fg="black",bg="antiquewhite1")
lbl_Panir_Momoz=Label(f1,text="Panir Momoz",font=("Verdana",15,'bold'),width=12,fg="black",bg="antiquewhite1")
lbl_Noodles=Label(f1,text="Noodles",font=("Verdana",15,'bold'),width=12,fg="black",bg="antiquewhite1")

lbl_cheese_pizza.grid(row=1,column=0)
lbl_Paneer_Pizza.grid(row=2,column=0)
lbl_Hot_Dog.grid(row=3,column=0)
lbl__Veg_Burger.grid(row=4,column=0)
lbl_Puff.grid(row=5,column=0)
lbl_Panir_Momoz.grid(row=6,column=0)
lbl_Noodles.grid(row=7,column=0)

#---------------------------------x  entry  x-------------------------------------------------------------------

entry_pizza=Entry(f1,font=("aria",20,),justify=CENTER,textvariable=Cheese_Pizza,bd=6,width=10,bg="yellow")
entry_Paneer_Pizza=Entry(f1,font=("aria",20,),justify=CENTER,textvariable=Paneer_Pizza,bd=6,width=10,bg="yellow")
entry_Hot_Dog=Entry(f1,font=("aria",20,),justify=CENTER,textvariable=Hot_Dog,bd=6,width=10,bg="yellow")
entry_Veg_Burger=Entry(f1,font=("aria",20,),justify=CENTER,textvariable=Veg_Burger,bd=6,width=10,bg="yellow")
entry_Puff=Entry(f1,font=("aria",20,),justify=CENTER,textvariable=Puff,bd=6,width=10,bg="yellow")
entry_Panir_Momoz=Entry(f1,font=("aria",20,),justify=CENTER,textvariable=Panir_Momoz,bd=6,width=10,bg="yellow")
entry_Noodles=Entry(f1,font=("aria",20,),justify=CENTER,textvariable=Noodles,bd=6,width=10,bg="yellow")

entry_pizza.grid(row=1,column=1)
entry_Paneer_Pizza.grid(row=2,column=1)
entry_Hot_Dog.grid(row=3,column=1)
entry_Veg_Burger.grid(row=4,column=1)
entry_Puff.grid(row=5,column=1)
entry_Panir_Momoz.grid(row=6,column=1)
entry_Noodles.grid(row=7,column=1)


#--------------------------------------------------x  Button  x-----------------------------------------------------------------------------------


btn_reset=Button(f1,bd=5,fg="black",bg="tomato2",font=("Time New Roman",16,'bold'),width=10,text="Reset",command=Reset)
btn_reset.grid(row=8,column=0)

btn_total=Button(f1,bd=5,font=("Time New Roman",16,'bold'),width=10,text="Total",bg="tomato2",fg="black",command=Total)
btn_total.grid(row=8,column=1)


# -----------------------------------------------------x  Bill  x-------------------------------------------------------------------------------


f2=Frame(root,bg="cyan2",highlightbackground="black",highlightthickness=2,width=300,height=370,)
f2.place(x=690,y=120)
Bill=Label(f2,text="Bill Area",font=("Gabriola",28,'bold'),bg="cyan2")
Bill.place(x=80,y=0)
Label(f2,text="Thank you for visit",font=("Gabriola",30,"bold"),fg="black",bg="cyan2").place(x=10,y=150)

root.mainloop()