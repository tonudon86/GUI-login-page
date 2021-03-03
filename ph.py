import mysql.connector as sql
from tkinter import *
from tkinter import messagebox
win = Tk()
win.geometry("500x500")
win.title("Login Page")
def login() :
    db = sql.connect(host = "localhost", user = "root", passwd = "")
    cur = db.cursor()
    try :
        cur.execute("create database login")
        db = sql.connect(host = "localhost", user = "root", passwd = "", database = "Login")
        cur = db.cursor
    except sql.errors.DatabaseError:
        db= sql.connect(host = "localhost", user = "root", passwd = "", database = "Login")
        cur = db.cursor()
        try :
            cur.execute("create table main(username varchar(50), NOT NULL, password int NOT NULL)")
        except sql.errors.ProgrammingError:
            pass
    finally :
        try :
            cur.execute("create table main(username varchar(50) NOT NULL, "
                        "password int NOT NULL)")
        except sql.errors.ProgrammingError:
            pass
    while True :
        user = user1.get()
        passwd = passwd1.get()
        cur.execute("select * from login where name = '%s' and password = %s" % (user, passwd))
        rud = cur.fetchall()
        if rud:
            print("Welcome")
            messagebox.showinfo("Alert", "Welcome")
            ok = Button(win, text="Start Session",width=10,height=1, command=win.destroy)
            ok.pack(pady=20)
            ok.place(x=208, y=350)
            ok.configure(bg="yellow")
            break
        else:
            messagebox.showerror("Error", "Login Failed")
    cur.close()
    db.close()
userlvl = Label(win, text = "Username :")
passwdlvl = Label(win, text = "Password  :")
user1 = Entry(win, textvariable = StringVar())
passwd1 = Entry(win, textvariable = IntVar().set(""))
passwd1.config(show="*")
enter = Button(win, text = "Enter",width=10,height=1,command= lambda:login(),bd = 0)
enter.configure(bg = "cyan")
user1.place(x = 200, y = 220)
passwd1.place(x = 200, y = 270)
userlvl.place(x = 130, y = 220)
passwdlvl.place(x = 130, y = 270)
enter.place(x = 208, y = 325)
win.mainloop()