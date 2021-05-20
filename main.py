# Import libraries
from tkinter import *
from tkinter import ttk


root = Tk()
root.title("Ticket Sales")
root.geometry('500x300')
root.configure(bg='yellow')



soccer = 40
movies = 75
theater = 100


var = StringVar()

entry1 = Entry(root, width=23)
entry1.place(x=170, y=100)

category = ttk.Combobox(root, textvariable=var, width=10, value=["Soccer", "Movie", "Theater"])
category.place(x=170, y=150)

number_of_tickets = ttk.Spinbox(root, from_=0, to=100, state="readonly", width=3)
number_of_tickets.place(x=170, y=200)

lblcell = Label(root, text="Cellphone number: ")
lblcell.place(x=20, y=100)

lblcat = Label(root, text="Ticket Category: ")
lblcat.place(x=20, y=150)

lbltik = Label(root, text="Number of tickets: ")
lbltik.place(x=20, y=200)

ans = Label(root)
ans.place(x=170, y=20)



#Creating class
class clsTiketSales:
    def __init__(self, celno, num_tickets, price):
      self.celno = celno
      self.num_tickets = num_tickets
      self.price = price


    def calul():
        sale = clsTiketSales(entry1.get(), float(number_of_tickets.get()), category.get())

        if category.get() == "Soccer":
            scprice = soccer * int(number_of_tickets.get()) + (14/100)
            ans.config(text="Price:"+ str(scprice) + "\n" + "tickets:"+str(number_of_tickets.get()) + "\n" +"Number:"+ str(entry1.get()))
        if category.get() == "Movie":
            mvprice = movies * int(number_of_tickets.get()) + (14/100)
            ans.config(text="Price:"+ str(mvprice) + "\n" + "tickets:"+str(number_of_tickets.get()) + "\n" +"Number:"+ str(entry1.get()))
        if category.get() == "Theater":
            thprice = theater * int(number_of_tickets.get()) + (14/100)
            ans.config(text="Price:"+ str(thprice) + "\n" + "tickets:"+str(number_of_tickets.get()) + "\n" +"Number:"+ str(entry1.get()))
    btn = Button(root, text="calculate", command=calul, width=20, height=1)
    btn.place(x=20, y=250)

def exit():
 root.destroy()
exit_btn = Button(text = "Quit", command=exit)
exit_btn.place(x=300, y=250)

root.mainloop()











