from tkinter import *
import mysql.connector
import tkinter.messagebox as m
from operator import itemgetter
root=Tk()
root.title("login and singup")
root.geometry("400x400")
bigText=Label(text="Login and Singup",font="Verdana 20 bold")
bigText.place(x=30,y=30)
def register():
    register=Tk()
    register.title("register")
    register.geometry("400x400")
    mydb= mysql.connector.connect(host="localhost",user="root",password="",database="pp")
    mycursor = mydb.cursor()
    bigText=Label(text="registration" ,font="Vardana 10 bold")
    bigText.place(x=100,y=30)
    name=Label(register,text="Name")
    name.place(x=90,y=100)
    email = Label(register, text="Email")
    email.place(x=90, y=140)
    password = Label(register, text="Password")
    password.place(x=90, y=180)
    repassword = Label(register, text="Repassword")
    repassword.place(x=90, y=220)

    e1=Entry(register)
    e1.place(x=180,y=100)
    e2 = Entry(register)
    e2.place(x=180, y=140)
    e3 = Entry(register,show="*")
    e3.place(x=180, y=180)
    e4 = Entry(register,show="*")
    e4.place(x=180, y=220)
    def clearEnrtyBox():
        e1.delete(first=0,last=100)
        e2.delete(first=0, last=100)
        e3.delete(first=0, last=100)
        e4.delete(first=0, last=100)
    def error():
        m.showerror(title="error",message="password not same")
    def insert():
        insert = ("insert into login(name,password,) values (%s,%s)")
        values = [e1.get(), e3.get()]
        cursor.execute(insert, values)


    registerbtn=Button(register,text="Register",fg="green",command=insert)
    registerbtn.place(x=175,y=260)
    btnExit = Button(register, text="Exit", bg="red", command=root.destroy)
    btnExit.place(x=350, y=350)







def login():
   print("hello")


goToLogin=Button(root,text="Login",fg="green",font="Verdana 10 bold",command=login)
goToLogin.place(x=120,y=200)
goToRegister=Button(root,text="Register",fg="green",font="Verdana 10 bold",command=register)
goToRegister.place(x=180,y=200)
btnExit=Button(root,text="Exit",bg="red",command=root.destroy)
btnExit.place(x=350,y=350)





















root.mainloop()