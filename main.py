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
entry1.grid(row=0, column=1)

category = ttk.Combobox(root, textvariable=var, width=10, value=["Soccer", "Movie", "Theater"])
category.grid(row=3, column=1)

number_of_tickets = ttk.Spinbox(root, from_=0, to=100, state="readonly")
number_of_tickets.grid(row=2, column=1)

lblcell = Label(root, text="Cellphone number: ")
lblcell.grid(row=0, column=0, sticky=W)

lblcat = Label(root, text="Ticket Category: ")
lblcat.grid(row=3, column=0, sticky=W)

lbltik = Label(root, text="Number of tickets: ")
lbltik.grid(row=2, column=0, sticky=W)

ans = Label(root)
ans.grid(row=14, column=0)


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
    btn.grid(row=9, column=0)

def exit():
 root.destroy()
exit_btn = Button(text = "Quit", command=exit)
exit_btn.grid(row=9, column=6)

# Adds widgets







root.mainloop()











