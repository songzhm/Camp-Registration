from tkinter import *
import sqlite3

class menu:
    def __init__(self, master):
        self.master = master
        frame = Frame(master)
        frame.pack()
        self.title = Label(frame, text="Menu")
        self.title.grid(row=0)
        self.Newapp = Button(frame, text="New applicants", command=self.newapp)
        self.Newapp.grid(row=1)
        self.ViewModify = Button(frame, text="View/Modify", command=self.viewapp)
        self.ViewModify.grid(row=2)
        self.Payment = Button(frame, text="Payment", command=payment)
        self.Payment.grid(row=3)

    def payment(self):
        top = Tk()
        self.master.destroy()
        payment(top)

    def newapp(self):
        top = Tk()
        self.master.destroy()
        newApplicant(top)

    def viewapp(self):
        top = Tk()
        self.master.destroy()
        viewApplicant(top)

class newApplicant:
    def __init__(self, master):
        label_1 = Label(master, text="First Name")
        label_2 = Label(master, text="Last Name")
        self.entry_1 = Entry(master)
        self.entry_2 = Entry(master)
        label_1.grid(row=0, sticky=W)
        label_2.grid(row=1, sticky=W)
        label_3 = Label(master, text="Age")
        label_4 = Label(master, text="Gender")
        self.entry_3 = Entry(master)
        self.entry_4 = Entry(master)
        label_1.grid(row=0, sticky=W)
        label_2.grid(row=1, sticky=W)
        self.entry_1.grid(row=0, column=1)
        self.entry_2.grid(row=1, column=1)
        label_3.grid(row=2, sticky=W)
        label_4.grid(row=3, sticky=W)
        self.entry_3.grid(row=2, column=1)
        self.entry_4.grid(row=3, column=1)
        button1 = Button(master, text = "Submit",fg="red", command=self.submit)
        button2 = Button(master, text = "Quit",fg="green", command=quit)
        button1.grid(row=4)
        button2.grid(row=4, column=1)

    def submit(self):
        fname = self.entry_1.get()
        lname = self.entry_2.get()
        age = self.entry_3.get()
        gender = self.entry_4.get()

        conn = sqlite3.connect('example.db')
        c = conn.cursor()
        p = [str(fname), str(lname), age, str(gender)]
        c.execute('INSERT INTO stocks(first_name, last_name, age, gender) VALUES (?,?,?,?)', p)
        conn.commit()
        conn.close()

class viewApplicant:
    def __init__(self, master):
        label_1 = Label(master, text="First Name")
        label_2 = Label(master, text="Last Name")
        self.entry_1 = Entry(master)
        self.entry_2 = Entry(master)
        label_1.grid(row=0, sticky=W)
        label_2.grid(row=1, sticky=W)
        label_3 = Label(master, text="Age")
        label_4 = Label(master, text="Gender")
        entry_3 = Entry(master)
        entry_4 = Entry(master)
        label_1.grid(row=0, sticky=W)
        label_2.grid(row=1, sticky=W)
        self.entry_1.grid(row=0, column=1)
        self.entry_2.grid(row=1, column=1)
        label_3.grid(row=2, sticky=W)
        label_4.grid(row=3, sticky=W)
        entry_3.grid(row=2, column=1)
        entry_4.grid(row=3, column=1)
        button1 = Button(master, text = "View",fg="red", command=self.view)
        button2 = Button(master, text = "Quit",fg="green", command=quit)
        button1.grid(row=4)
        button2.grid(row=4, column=1)

    def view(self):
        conn = sqlite3.connect('example.db')
        c = conn.cursor()
        fname = str(self.entry_1.get())
        lname = self.entry_2.get()
        c.execute("SELECT * FROM stocks WHERE first_name = ?  or last_name = ?", (fname, lname))
        print (c.fetchone())
        conn.commit()
        conn.close()


class payment:
    def __init__(self, master):
        label_1 = Label(master, text="First Name")
        label_2 = Label(master, text="Last Name")
        self.entry_1 = Entry(master)
        entry_2 = Entry(master)
        label_1.grid(row=0, sticky=W)
        label_2.grid(row=1, sticky=W)
        self.entry_1.grid(row=0, column=1)
        entry_2.grid(row=1, column=1)
        button1 = Button(master, text = "Payment",fg="red")
        button2 = Button(master, text = "Quit",fg="green", command=quit)
        button1.grid(row=4)
        button2.grid(row=4, column=1)



root = Tk()
u = menu(root)
root.mainloop()


## Use as create a database
## conn = sqlite3.connect('example.db')
## c= conn.cursor()

## c.execute('''CREATE TABLE stocks(id integer primary key, first_name text, last_name text, age real, gender text)''')