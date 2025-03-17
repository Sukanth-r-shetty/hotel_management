from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1550x800+-10+0")
        
        
        ####vrible3====================
        
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQcn=StringVar()
        self.var_securityAns=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
        #================bg imag==========
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\Dell\OneDrive\Desktop\hotel management systaem\restaurant-background-66dqs6aozq74vmqn.jpg")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)
        #===================left image
        self.bg1=ImageTk.PhotoImage(file=r"C:\Users\Dell\OneDrive\Desktop\hotel management systaem\health.jpg")
        left_lbl=Label(self.root,image=self.bg1)
        left_lbl.place(x=150,y=50,width=400,height=500)
        #main frame==============
        frame=Frame(self.root,bg="white")
        frame.place(x=550,y=50,width=600,height=500)
        
        
        
        Register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="green",bg="white")
        Register_lbl.place(x=20,y=20)
        
        #=============lbel and entry============
        fname=Label(frame,text="First Name",font=("times new roman",16,"bold"),bg="white")
        fname.place(x=50,y=100)
        
        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",16,"bold"))
        fname_entry.place(x=50,y=130,width=225)
        
        
        lname=Label(frame,text="Last Name",font=("times new roman",16,"bold"),bg="white")
        lname.place(x=300,y=100)
        
        lname_entry=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",16,"bold"))
        lname_entry.place(x=300,y=130,width=225)
        
        #==============contc
        
        contact=Label(frame,text="Contact Number",font=("times new roman",16,"bold"),bg="white")
        contact.place(x=50,y=180)
        
        contact_entry=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",16,"bold"))
        contact_entry.place(x=50,y=210,width=225)
        
        #===emil
           
        email=Label(frame,text="Email",font=("times new roman",16,"bold"),bg="white")
        email.place(x=300,y=180)
        
        email_entry=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",16,"bold"))
        email_entry.place(x=300,y=210,width=225)
        
        #+scry
        secur=Label(frame,text="Select Security Question",font=("times new roman",16,"bold"),bg="white")
        secur.place(x=50,y=260)
        
        self.combo_security=ttk.Combobox(frame,textvariable=self.var_securityQcn,font=("times new roman",16,"bold"),state="readonly")
        self.combo_security["values"]=("Select","Your Birthplace name","Your Favourite Teacher name","Your Bestfriend Name")
        self.combo_security.place(x=50,y=290,width=225)
        self.combo_security.current(0)
        
        
        
        # secur_entry=ttk.Entry(frame,font=("times new roman",16,"bold"))
        # secur_entry.place(x=50,y=290,width=225)
        
        #sec_ans===========
        secur_ans=Label(frame,text="Security Answer",font=("times new roman",16,"bold"),bg="white")
        secur_ans.place(x=300,y=260)
        
        self.secur_ans_entry=ttk.Entry(frame,textvariable=self.var_securityAns,font=("times new roman",16,"bold"))
        self.secur_ans_entry.place(x=300,y=290,width=225)
        
        #pass===========
        pswrd=Label(frame,text="Password",font=("times new roman",16,"bold"),bg="white")
        pswrd.place(x=50,y=340)
        
        self.pswrd_entry=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",16,"bold"))
        self.pswrd_entry.place(x=50,y=370,width=225)
        
        #===confrm pass===
        conf_pswrd=Label(frame,text="Confirm Pssword",font=("times new roman",16,"bold"),bg="white")
        conf_pswrd.place(x=300,y=340)
        
        self.conf_pswrd_entry=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",16,"bold"))
        self.conf_pswrd_entry.place(x=300,y=370,width=225)
        
        #====check btn
        self.var_check=IntVar()
        
        self.checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree The Terms & Conditions",font=("times new roman",10,"bold"),onvalue=1,offvalue=0)
        self.checkbtn.place(x=50,y=410)
        
        #button
        loginbtn=Button(frame,text="LOGIN NOW",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="blue",activeforeground="white",activebackground="blue")
        loginbtn.place(x=270,y=450,width=200,height=35) 
        
        
        self.registerbtn=Button(frame,text="REGISTER NOW",command=self.register_data,font=("times new roman",15,"bold"),borderwidth=0,fg="white",bg="red",activeforeground="white",activebackground="red")
        self.registerbtn.place(x=50,y=450,width=200,height=35) 
        
        
            #########fnution declatron
            
            
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQcn.get()=="Select":
            messagebox.showerror("Error","All fields are required ")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Please match password and confirm password")
               
        elif self.var_check.get()==0:
            messagebox.showerror("Error","please agree to term and condition")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Shetty994511",database="hotel_management")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exist,please try using another email")
            else:
                # my_cursor.execute("INSERT INTO register (fname, lname, contact, email, securityqcn, securityans, password) VALUES (%s,%s,%s,%s,%s,%s,%s)",(
                #                                                                                                                                         self.var_fname.get(),
                #                                                                                                                                         self.var_lname.get(),
                #                                                                                                                                         self.var_contact.get(),
                #                                                                                                                                         self.var_email.get(),
                #                                                                                                                                         self.var_securityQcn.get(),
                #                                                                                                                                         self.var_securityAns.get(),
                #                                                                                                                                         self.var_pass.get()
                #                                                                                                                                     ))

                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_fname.get(),
                                                                                        self.var_lname.get(),
                                                                                        self.var_contact.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_securityQcn.get(),
                                                                                        self.var_securityAns.get(),
                                                                                        self.var_pass.get()
                                                                                    ))


            conn.commit()
            conn.close()
            messagebox.showinfo("Success","registration succesfull") 
        

        
        
        
        
if __name__=="__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()