from tkinter import *
from PIL import Image, ImageTk
import tkinter.messagebox as tmsg
import mysql.connector
 
roote =Tk()
roote.title("login page")
roote.geometry("1500x800")


#========================function============================================================
def value():
  try:
      mydb = mysql.connector.connect(host="localhost", user="root", password="", database="pp")
  except:
      print("you are not connected to server ")
  else:
      print("cunnection succsful")
      email=userentryvalue.get()
      seq=passentryvalue.get()
      mycursor = mydb.cursor()
      query="SELECT name,password FROM login"
      mycursor.execute(query)
      # myresult = mycursor.fetchall()
      for (name,password) in mycursor:
          if email==name and seq==password:
              login=True
              print("loginn suces")
              tmsg.showinfo(title="done", message=" created ")

              break
          else:
              login=False

              print("logged in failed")
              tmsg.showinfo(title="error", message="Account not created ")












    # tmsg.showinfo("Notification",f" Hello  {userentryvalue.get()} you successfully loged In")
# =============================================heading====================================================
Label(roote,text="Welcome To Our Cafe",bg="cyan3",fg="crimson",font=("Times 30 bold italic"),anchor="ne").grid(pady=40,row=0,column=3,ipadx=200)
#========================================frame image======================================================
Image=Image.open("Restaurant.jpg")
Image = Image.resize((300,300))
photo=ImageTk.PhotoImage(Image)
lable1=Label(image=photo,)
lable1.grid(row=2,column=2,columnspan=3,rowspan=5)

# login input
#database
userentryvalue = StringVar()
passentryvalue=StringVar()

#========================================= entry widgets==========================================
f2 = Frame(roote).grid(row=3,column=4)
l1=Label(f2,text="Login Here ",fg="crimson",bg="cyan3",font=("Times 25 bold italic")).grid(row=3,column=4)
Label(f2,text="Username ",fg="crimson",bg="cyan3",font=("Times 20 bold italic")).grid(row=4,column=4)
userentry=Entry(f2,font=("Times 15 bold italic"),textvariable=userentryvalue)
userentry.grid(row=4,column=5)
Label(f2,text="Password ",fg="crimson",bg="cyan3",font=("Times 20 bold italic")).grid(row=5,column=4)
Entry(f2,font=("Times 15 bold italic"),textvariable=passentryvalue).grid(row=5,column=5)


#=========================================login / signin button======================================
Button(f2,text="Login",bg="green",font=("Times 20 bold italic"),command=value).grid(row=6,column=4)   
Button(f2,text="SignIn",bg="green",font=("Times 20 bold italic"),command=roote.destroy).grid(row=6,column=5)
roote.configure(bg="cyan3")

#=============================================login page end=========================================


#==============================================registration page==========================================
roote.mainloop()
win = Tk()
win.title("Registration page")
win.geometry("1500x800")
f1=Frame(win,bg="cyan3",padx=20,pady=50,borderwidth=33,relief=SUNKEN)
f1.grid(row=1,column=5)

# ===========================================functions=======================================================================================================
def getvalues():
    tmsg.showinfo("Signed In","You Have Successfully Signed In ")
    tmsg.showinfo("Welcome To Our Cafe",f"Hey {namevalue.get()} Welcome To Our Cafe ")

    print(f" The input value of is name {namevalue.get()}")
    print(f" The input value of is phone {Phonevalue.get()}")
    # print(f" The input value of is gender {var.get()}")
    print(f" The input value of is email  {Emailvalue.get()}")
    print(f" The input value of is email  {Passwordvalue.get()}")
    print(f" The input value of is email  {ConfirmPasswordvalue.get()}")
    print(f" The input value of is payment {Paymentvalue.get()}")
    print(f" The input value of is foodservice {foodservicevalue.get()}")
#=================================================heading=======================================================================================================
Label(win,bg="cyan3",fg="crimson",text="Welcome",font=("Times 30 bold italic"),borderwidth=30,relief=SUNKEN,padx=70,pady=15).grid(row=0,column=4)
Label(win,bg="cyan3",fg="crimson",text="Cafe",font=("Times 30 bold italic"),borderwidth=30,relief=SUNKEN,padx=70,pady=15).grid(row=0,column=7)
#========================================= text for our form =========================================================================================
heading=Label(f1,bg="cyan3",text="Welcome To Our Cafe",font=("Times 30 bold italic"),fg="black").grid(row=0,column=4)
name =Label(f1,text="Username:",bg="cyan3",fg="crimson",font=("Times 20 bold italic"))
Phone =Label(f1,text="Phone:",bg="cyan3",fg="crimson",font=("Times 20 bold italic"))
# Gender =Label(f1,text="Gender:",bg="cyan3",fg="white",font=("Times 20 bold italic"))
Email =Label(f1,text="Email:",bg="cyan3",fg="crimson",font=("Times 20 bold italic"))
Password =Label(f1,text="Password:",bg="cyan3",fg="crimson",font=("Times 20 bold italic"))
ConfirmPassword =Label(f1,text="Confirm Password:",bg="cyan3",fg="crimson",font=("Times 20 bold italic"))
Payment =Label(f1,text="Payment Mode:",bg="cyan3",fg="crimson",font=("Times 20 bold italic"))
#================================== packing text for our form==============================================================================
name.grid(row=1,column=3)
Phone.grid(row=2,column=3)
# Gender.grid(row=3,column=3)
Email.grid(row=3,column=3)
Password.grid(row=4,column=3)
ConfirmPassword.grid(row=5,column=3)
Payment.grid(row=6,column=3)
#=============================== tkinter variables for storing entries====================================
namevalue = StringVar() #deta base
Phonevalue = StringVar()
# var = StringVar()
# var.set(0)
Emailvalue = StringVar()
Passwordvalue = StringVar() #detabase
ConfirmPasswordvalue = StringVar()
Paymentvalue = StringVar()
foodservicevalue = IntVar()
#==================================== Entries  for our form===============================================
nameentry =Entry(f1,textvariable=namevalue)
Phoneentry =Entry(f1,textvariable=Phonevalue)
# b1 = Radiobutton(f1,text="Male",value="Male",variable=var,bg="cyan3",fg="white",font="Helvetica 16 bold")
# b2 = Radiobutton(f1,text="Female",value="Female",variable=var,bg="cyan3",fg="white",font="Helvetica 16 bold")
Emailentry =Entry(f1,textvariable=Emailvalue)
Passwordentry = Entry(f1,textvariable=Passwordvalue)
ConfirmPasswordentry = Entry(f1,textvariable=ConfirmPasswordvalue)

Paymententry =Entry(f1,textvariable=Paymentvalue)

# =======================================packing the entry================================================
nameentry.grid(row=1,column=4)
Phoneentry.grid(row=2,column=4)
# b1.grid(row=3,column=4)
# b2.grid(row=3,column=5)
Emailentry.grid(row=5,column=4)
Passwordentry.grid(row=3,column=4)
ConfirmPasswordentry.grid(row=4,column=4)

Paymententry.grid(row=6,column=4)


def clearEnrtyBox():
    pass
def insert():

        mydb = mysql.connector.connect(host="localhost", user="root", password="", database="pp")
        mycursor = mydb.cursor()
        insert = ("INSERT INTO login (name,password) VALUES  (%s,%s)")
        values = [namevalue.get(),ConfirmPasswordvalue.get()]
        mycursor.execute(insert,values)
        # if Passwordvalue.get()==ConfirmPasswordvalue.get():
        mydb.commit()
        tmsg.showinfo(title="done", message="Account created ")

        # else:
        #     tmsg.showinfo(title="wrong", message="Account  not created ")

#================================================bg color===============================================

win.configure(bg="cyan3")
#======================================= button & paccking it and assigning it a command===============
Button(f1,text="Sign Up",command=insert,font=("Times 20 bold italic"),bg="green",fg="black",).grid(row=7,column=4)
win.mainloop()

