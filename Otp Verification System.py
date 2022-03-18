from tkinter import *
import tkinter.messagebox as tsmg
import requests
import random
import json

#importing the module

root=Tk()

rand=random.randint(1,999999)

msg=f"Your One Time Password(OTP) is {rand}"

def sms_send(a,msg):
    url="https://www.fast2sms.com/dev/bulk"
    params={
  
#  Unique API and setting the params 
#get your api key on https://www.fast2sms.com/dashboard/dev-api
  
        "authorization":"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        "sender_id":"SMSINI",
        "message":msg,
        "language":"english",
        "route":"p",
        "numbers":a
    }
    rs=requests.get(url,params=params)

  #creating the send method and using the if else loop
def send():
    a=num.get()
    if(a==""):
        tsmg.showerror("Error","Enter Your Mobile Number")
    elif (len(a)<10):
        tsmg.showerror("Error","Invalid Mobile Number")
        num.set("")
    else:
        b=tsmg.askyesno("Info",f"Your Number is {a}")
        if(b==True):
            sms_send(a,msg)
        else:
            num.set("")

#creating the check method and using the if else loop 

def check():
    c=otp.get()
    if(c==""):
        tsmg.showerror("Error","Enter OTP")
    else:
        if(str(rand)==c):
            tsmg.showinfo("Info","Successful")
        else:
            tsmg.showerror("Error","Invalid OTP")
            num.set("")
            otp.set("")

#creating the interface 


root.geometry("500x500")
root.title("OTP Verification System")


num=StringVar()
otp=StringVar()

f1=Frame(root)
Label(f1,text="Check Your OTP",font="SegoeUI 30 bold",fg="purple").pack(padx=5,pady=10)
f1.pack(fill=BOTH)

f2=Frame(root)
Label(f2,text="Enter Your Number",font="SegoeUI 20 bold",fg="teal").pack(padx=5,pady=5)
e1=Entry(f2,textvariable=num,font="SegoeUI 14 bold",fg="black",bg="white",relief=SUNKEN,borderwidth=4,justify="center").pack(ipady=5)
f2.pack(fill=BOTH,padx=5,pady=10)

f3=Frame(root)
Label(f3,text="Enter OTP",font="SegoeUI 20 bold",fg="teal").pack(padx=5,pady=5)
e2=Entry(f3,textvariable=otp,font="SegoeUI 14 bold",fg="black",bg="white",relief=SUNKEN,borderwidth=5,justify="center").pack(ipady=5)
f3.pack(fill=BOTH,padx=5,pady=10)

f4=Frame(root)
Button(f4,text="Send OTP",command=send,font="SegoeUI 10 bold",fg="purple").pack(padx=20,pady=10,side=LEFT)
Button(f4,text="Check OTP",command=check,font="SegoeUI 10 bold",fg="purple").pack(padx=40,pady=10,side=LEFT)
f4.pack()


root.mainloop()
