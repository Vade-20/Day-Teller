from tkinter import *

root = Tk()
root.title('Day Teller')
root.config(bg='sky blue')
root.iconbitmap(r'Day-Teller\calendar.ico')
l1 = Label(root,text='Day Teller',fg='gold',bg='sky blue', padx=250, font=('Comic Sans MS', '40'),
               )
l1.grid(row=0,column=0,columnspan=6)
l2 = Label(root,text='Enter the date-',fg='gold',bg='sky blue', font=('Comic Sans MS', '20'),
               )
l2.grid(row=1,column=0)
l3 = Label(root,text='/',fg='gold',bg='sky blue',  font=('Comic Sans MS', '40'),
               )
l4 = Label(root,text='/',fg='gold',bg='sky blue',  font=('Comic Sans MS', '40'),
               )
l3.grid(row=1,column=2)
l4.grid(row=1,column=4)
l5 = Label(root,text='',fg='gold',bg='sky blue',  font=('Comic Sans MS', '20'),
            )
l5.grid(row=3,column=0,columnspan=6)
e1 = Entry(root, fg='gold',bg='light sky blue',font=('Comic Sans MS', '20'), width=5, borderwidth=2)
e2 = Entry(root, fg='gold',bg='light sky blue',font=('Comic Sans MS', '20'), width=5, borderwidth=2)
e3 = Entry(root, fg='gold',bg='light sky blue',font=('Comic Sans MS', '20'), width=5, borderwidth=2)
e1.grid(row =1,column=1)
e2.grid(row =1,column=3)
e3.grid(row =1,column=5)


def reset():
    global e1,e2,e3,l5
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    l5.config(text='')


def teller():
    from tkinter import messagebox
    global e1,e2,e3
    date = [int(e1.get()),int(e2.get()),int(e3.get())]
    if not check_format(date):    
        error = messagebox.showerror('Error','Enter the date in the format (DD/MM/YYYY)')
        reset()
        return None
    if not check_month(date):
        print("sen3")
        reset()
        return None
    d = day(date)
    sen = f'The day on {e1.get()}/{e2.get()}/{e3.get()} is {d}'
    l5.config(text=sen)
    

def check_format(n):
    n = [str(i) for i in n]
    if len(n[0]) > 2:
        return False
    elif len(n[1]) > 2:
        return False
    elif len(n[2]) > 4 or len(n[2]) < 4:
        return False
    else:
        return True


def check_leap_year(n):
    if n[2] % 100 == 0:
        if n[2] % 400 == 0:
            return True
        else:
            return False
    else:
        if n[2] % 4 == 0:
            return True
        else:
            return False


def check_month(n):
    from tkinter import messagebox
    months = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July",
              8: "August", 9: "September", 10: "October", 11: "November", 12: "December"}
    if n[1] == 0 or n[2] == 0 or n[0] == 0:
        error = messagebox.showerror('Error','Enter the date in the format (DD/MM/YYYY)')
        return False
    else:
        if check_leap_year(n):
            if n[1] > 12:
                error = messagebox.showerror('Error','Enter a proper value for month')
                return False
            elif n[1] == 2 and n[0] > 29:
                error = messagebox.showerror('Error','There are only 29 days in February of a Leap year')
                return False
            elif n[1] < 8 and n[1] % 2 == 0 and n[0] > 30:
                error = messagebox.showerror('Error',f"There are only 30 days in {months.get(n[1])}")
                return False
            elif n[1] < 8 and n[1] % 2 != 0 and n[0] > 31:
                error = messagebox.showerror('Error',f"There are only 31 days in {months.get(n[1])}")
                return False
            elif n[1] >= 8 and n[1] % 2 == 0 and n[0] > 31:
                error = messagebox.showerror('Error',f"There are only 31 days in {months.get(n[1])}")
                return False
            elif n[1] >= 8 and n[1] % 2 != 0 and n[0] > 30:
                error = messagebox.showerror('Error',f"There are only 30 days in {months.get(n[1])}")
                return False
        else:
            if n[1] == 2 and n[0] > 28:
                error = messagebox.showerror('Error','There are only 28 days in February of a regular year')
                return False
            else:
                if n[1] > 12:
                    error = messagebox.showerror('Error','Enter a proper value for month')
                    return False
                elif n[1] < 8 and n[1] % 2 == 0 and n[0] > 30:
                    error = messagebox.showerror('Error',f"There are only 30 days in {months.get(n[1])}")
                    return False
                elif n[1] < 8 and n[1] % 2 != 0 and n[0] > 31:
                    error = messagebox.showerror('Error',f"There are only 31 days in {months.get(n[1])}")
                    return False
                elif n[1] >= 8 and n[1] % 2 == 0 and n[0] > 31:
                    error = messagebox.showerror('Error',f"There are only 31 days in {months.get(n[1])}")
                    return False
                elif n[1] >= 8 and n[1] % 2 != 0 and n[0] > 30:
                    error = messagebox.showerror('Error',f"There are only 30 days in {months.get(n[1])}")
                    return False
    return True            


def day(n):
    days = 0
    for i in range(1, n[2]):
        if i % 100 == 0:
            if i % 400 == 0:
                days = days + 366
            else:
                days = days + 365
        else:
            if i % 4 == 0:
                days = days + 366
            else:
                days = days + 365

    if check_leap_year(n):
        for i in range(1, n[1]):
            if i == 2:
                days = days + 29
            else:
                if i % 2 == 0 and i < 8:
                    days = days + 30
                elif i % 2 != 0 and i < 8:
                    days = days + 31
                elif i % 2 == 0 and i >= 8:
                    days = days + 31
                elif i % 2 != 0 and i >= 8:
                    days = days + 30
    else:
        for i in range(1, n[1]):
            if i == 2:
                days = days + 28
            else:
                if i % 2 == 0 and i < 8:
                    days = days + 30
                elif i % 2 != 0 and i < 8:
                    days = days + 31
                elif i % 2 == 0 and i >= 8:
                    days = days + 31
                elif i % 2 != 0 and i >= 8:
                    days = days + 30
    days = days + n[0]
    d = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday",6: "Saturday", 7: "Sunday"}
    day = days % 7
    if day == 0:
        return d.get(7)
    else:
        return d.get(day)



b1 = Button(root,text = 'Reset',fg='gold',bg='sky blue',font= ('Comic Sans MS', '20'),command=reset,width=15,)
b1.grid(row=2,column=0,columnspan=2,sticky=W+E)
b1 = Button(root,text = 'Enter',fg='gold',bg='sky blue',font= ('Comic Sans MS', '20'),command=teller,width=20,)
b1.grid(row=2,column=2,columnspan=4,sticky=W+E)
mainloop()