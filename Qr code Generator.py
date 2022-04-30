from cgitb import text
from distutils.command.config import config
import tkinter
import qrcode
from PIL import Image,ImageTk
from resizeimage import resizeimage
from tkinter import*
class Qr_Generator:
  def __init__(self,root):
    self.root=root
    self.root.geometry("900x500+200+50")
    self.root.title("Qr Generator | Developed By Subhash Jha ")
    self.root.resizable(False,False)

    title=Label(self.root,text="Qr Code generator ",font=("times new roman",40),bg='Green',anchor='w').place(x=0,y=0,relwidth=1)

    self.var_emp_code=StringVar()
    self.var_emp_name=StringVar()
    self.var_emp_department=StringVar()
    self.var_emp_class=StringVar()

    emp_Frame=Frame(self.root,bd=2,relief=RIDGE)
    emp_Frame.place(x=50,y=100,width=500,height=380)

    emp_title=Label(emp_Frame,text="Student Details",font=("goudy old style",20),bg='green',fg='white').place(x=0,y=0,relwidth=1)
    lbl_emp_code=Label(emp_Frame,text="Student PID",font=("times new roman",15,"bold"),bg='white').place(x=20,y=60)
    lbl_name=Label(emp_Frame,text="Name",font=("times new roman",15,"bold"),bg='white').place(x=20,y=100)
    lbl_department=Label(emp_Frame,text="Department",font=("times new roman",15,"bold"),bg='white').place(x=20,y=140)
    lbl_class=Label(emp_Frame,text="Class",font=("times new roman",15,"bold"),bg='white').place(x=20,y=180)

    txt_emp_code=Entry(emp_Frame,font=("times new roman",15),textvariable=self.var_emp_code,bg='lightyellow').place(x=200,y=60)
    txt_name=Entry(emp_Frame,font=("times new roman",15),textvariable=self.var_emp_name,bg='lightyellow').place(x=200,y=100)
    txt_department=Entry(emp_Frame,font=("times new roman",15),textvariable=self.var_emp_department,bg='lightyellow').place(x=200,y=140)
    txt_class=Entry(emp_Frame,font=("times new roman",15),textvariable=self.var_emp_class,bg='lightyellow').place(x=200,y=180)

    btn_generate=Button(emp_Frame,text="Generate QR",command=self.generate,font=("times new roman",18,'bold'),bg='green',fg='white').place(x=90,y=250,width=180,height=30)
    btn_clear=Button(emp_Frame,command=self.clear,text="Clear",font=("times new roman",18,'bold'),bg='green',fg='white').place(x=280,y=250,width=120,height=30)

    self.msg=""
    self.lbl_msg=Label(emp_Frame,text=self.msg,font=("times new roman",20),bg='white',fg="green")
    self.lbl_msg.place(x=0,y=310,relwidth=1)



    qr_Frame=Frame(self.root,bd=2,relief=RIDGE)
    qr_Frame.place(x=600,y=100,width=250,height=380)

    emp_title=Label(qr_Frame,text="Student Qr Code",font=("goudy old style",20),bg='green',fg='white').place(x=0,y=0,relwidth=1)
    
    self.qr_code=Label(qr_Frame,text="No Qr \n Not Available ",font=('times new roman',15),bg="green",fg='white',bd=1,relief=RIDGE)
    self.qr_code.place(x=35,y=100,width=180,height=180)
  def clear(self):
    self.var_emp_code.set('')
    self.var_emp_name.set('')
    self.var_emp_department.set('')
    self.var_emp_class.set('')
    self.msg=''
    self.lbl_msg=config(text=self.msg)

  def generate(self):
     if self.var_emp_class.get()==''or self.var_emp_code.get()==''or self.var_emp_department.get()==''or self.var_emp_name.get()=='':
         self.msg="All Fields are Required!!"
         self.lbl_msg=config(text=self.msg,fg='green')
     else:
         qr_data=(f"Student PID:{self.var_emp_code.get()}\n Student Name: {self.var_emp_name.get()}\n department:{self.var_emp_department.get()}\n Class:{self.var_emp_class.get()}")
         qr_code=qrcode.make(qr_data)
         print(qr_code)
         qr_code=resizeimage.resize_cover(qr_code,[180,180])
         self.im=ImageTk.PhotoImage(qr_code)
         self.qr_code.config(image=self.im)
         self.msg="Qr Generated Successfully"
         self.lbl_msg=config(text=self.msg,fg='green')



root = Tk()
obj=Qr_Generator(root)
root.mainloop()