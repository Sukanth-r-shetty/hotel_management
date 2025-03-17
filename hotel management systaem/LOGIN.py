from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from register import Register
import mysql.connector
from customer import Cust_window
from room import Roombooking
from details import detailsroom
from hotel import HotelManagementSystem


def main():
    win=Tk()
    app=LoginWindow(win)
    win.mainloop()
    

class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        


        # Full screen setup
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{screen_width}x{screen_height}+-10+0")

        # Load and resize background image
        img = Image.open(r"C:\Users\Dell\OneDrive\Desktop\hotel management systaem\login_img.jpg")
        img = img.resize((screen_width, screen_height), Image.LANCZOS)
        self.bg = ImageTk.PhotoImage(img)

        # Display background
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, width=screen_width, height=screen_height)

        # Create login frame
        frame = Frame(self.root, bg="black")
        frame.place(x=450, y=120, width=340, height=450)

        # Load and resize profile/user icon
        img1 = Image.open(r"C:\Users\Dell\OneDrive\Desktop\hotel management systaem\OIP.jpg")
        img1 = img1.resize((100, 100), Image.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1)

        # Display profile/user icon (fixed version)
        lblimg1 = Label(self.root, image=self.photoimage1, bg="black", borderwidth=0)
        lblimg1.place(x=570, y=155, width=100, height=100)  # Corrected placement
        
        
        
        get_started=Label(frame,text="GET STARTED",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_started.place(x=80,y=140)
        
        
        #label
        username_lbl=Label(frame,text="USER NAME",font=("times new roman",15,"bold"),fg="white",bg="black")
        username_lbl.place(x=50,y=190)
        
        self.txtuser= ttk.Entry(frame,font=("times new roman",15,"bold")) 
        self.txtuser.place(x=50,y=220,width=250)
        
        
        password_lbl=Label(frame,text="PASSWORD",font=("times new roman",15,"bold"),fg="white",bg="black")
        password_lbl.place(x=50,y=250)
        
        self.txtpassword= ttk.Entry(frame,font=("times new roman",15,"bold")) 
        self.txtpassword.place(x=50,y=280,width=250)   
        
        
        
        ####button
        loginbtn=Button(frame,text="LOGIN",command=self.login,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="blue",activeforeground="white",activebackground="blue")
        loginbtn.place(x=110,y=330,width=120,height=35) 
        
        
        registerbtn=Button(frame,text="REGISTER",command=self.register_window,font=("times new roman",8,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=20,y=370,width=120,height=35) 
        
        forgetbtn=Button(frame,text="FORGOT PASSWORD",command=self.forgot_pass_window,font=("times new roman",8,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        forgetbtn.place(x=50,y=400,width=120,height=35)               
    
    
    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)
        
    def login(self):
        if self.txtuser.get()=="" or self.txtpassword.get()=="":
            messagebox.showerror("Error","All field is required")
            
        elif self.txtuser.get()=="sukanthshetty" and self.txtpassword.get()=="Shetty@123":
            messagebox.showinfo("Success","Welcome to Shetty Lunch Home")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Shetty994511",database="hotel_management")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                        self.txtuser.get(),
                                                                        self.txtpassword.get()
                                                                    ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","invalid username & password")
            else:
                open_main=messagebox.askyesno("yesNo","access only admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=HotelManagementSystem(self.new_window)
                else:
                    if not open_main:
                        return
                conn.commit()
                conn.close()
                
             #==resr paswrd==============
    def reset_pass(self):
        if self.combo_security.get()=="Select":
            messagebox.showerror("Error","Select Security Question")
            
        elif self.secur_ans_entry.get()=="":
            messagebox.showerror("Error","please enter the answer",parent=self.root2)
        elif self.new_passwrd_entry.get()=="":
            messagebox.showerror("Error","please enter new password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Shetty994511",database="hotel_management")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s and securityqcn=%s and securityans=%s")
            
            value=(self.txtuser.get(),self.combo_security.get(),self.secur_ans_entry.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter correct answer",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.new_passwrd_entry.get(),self.txtuser.get())
                my_cursor.execute(query,value)
                
                conn.commit()
                conn.close()
                messagebox.showerror("Info","Your pass word has been reset,please login new password",parent=self.root2)
                self.root.destroy()
            
            
            
            
                
                
                
    #rforget pass window=======================            
    def forgot_pass_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("error","please enter the email adress to reset password")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Shetty994511",database="hotel_management")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            # print(row)
            
            if row==None:
                messagebox.showerror("my Error","Please enter the valid user name")
            
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x440+440+130")
                # (x=450, y=120, width=340, height=450)
                
                l=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),fg="red",bg="white")
                l.place(x=0,y=10,relwidth=1)
                
                secur=Label(self.root2,text="Select Security Question",font=("times new roman",16,"bold"),bg="white")
                secur.place(x=50,y=80)
        
                self.combo_security=ttk.Combobox(self.root2,font=("times new roman",16,"bold"),state="readonly")
                self.combo_security["values"]=("Select","Your Birthplace name","Your Favourite Teacher name","Your Bestfriend Name")
                self.combo_security.place(x=50,y=110,width=250)
                self.combo_security.current(0)
        

        
                #sec_ans===========
                secur_ans=Label(self.root2,text="Security Answer",font=("times new roman",16,"bold"),bg="white")
                secur_ans.place(x=50,y=150)
                
                self.secur_ans_entry=ttk.Entry(self.root2,font=("times new roman",16,"bold"))
                self.secur_ans_entry.place(x=50,y=180,width=250)
        #ne wpasword
                new_passwrd=Label(self.root2,text="New Password",font=("times new roman",16,"bold"),bg="white")
                new_passwrd.place(x=50,y=220)
                
                self.new_passwrd_entry=ttk.Entry(self.root2,font=("times new roman",16,"bold"))
                self.new_passwrd_entry.place(x=50,y=250,width=250)
                
                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman",15,"bold"),fg="white",bg="green")
                btn.place(x=100,y=290)
        

             
            
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
        
        self.fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",16,"bold"))
        self.fname_entry.place(x=50,y=130,width=225)
        
        
        lname=Label(frame,text="Last Name",font=("times new roman",16,"bold"),bg="white")
        lname.place(x=300,y=100)
        
        self.lname_entry=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",16,"bold"))
        self.lname_entry.place(x=300,y=130,width=225)
        
        #==============contc
        
        contact=Label(frame,text="Contact Number",font=("times new roman",16,"bold"),bg="white")
        contact.place(x=50,y=180)
        
        self.contact_entry=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",16,"bold"))
        self.contact_entry.place(x=50,y=210,width=225)
        
        #===emil
           
        email=Label(frame,text="Email",font=("times new roman",16,"bold"),bg="white")
        email.place(x=300,y=180)
        
        self.email_entry=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",16,"bold"))
        self.email_entry.place(x=300,y=210,width=225)
        
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
        loginbtn=Button(frame,text="LOGIN NOW",command=self.return_login,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="blue",activeforeground="white",activebackground="blue")
        loginbtn.place(x=270,y=450,width=200,height=35) 
        
        
        registerbtn=Button(frame,text="REGISTER NOW",command=self.register_data,font=("times new roman",15,"bold"),borderwidth=0,fg="white",bg="red",activeforeground="white",activebackground="red")
        registerbtn.place(x=50,y=450,width=200,height=35) 
        
        
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
    def return_login(self):
        self.root.destroy()
            
class HotelManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("SHETTY LUNCH HOME")
        self.root.geometry("1550x800+0+0")
        
        #==========IMAGE1===========================
        img1=Image.open(r"C:\Users\Dell\OneDrive\Desktop\hotel management systaem\hotel1.png")
        img1 = img1.resize((1550,140),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        lbling=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lbling.place(x=0,y=0,width=1550,height=140)
        
        #=======================LOGO++++++++++++++
        img2=Image.open(r"C:\Users\Dell\OneDrive\Desktop\hotel management systaem\logohotel.jpg")
        img2 = img2.resize((250,140),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        lbling=Label(self.root,image=self.photoimg2,relief=RIDGE)
        lbling.place(x=0,y=0,width=250,height=140)
        
        #+========================title===================================
        
        
        lbl_title=Label(self.root,text="SHETTY LUNCH HOME",font=("times new roman",45,"bold"),bg="black",fg="gold")
        lbl_title.place(x=-50,y=140,width=1550,height=50)
        
        
        #=======================main frame================
        
        
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=-50,y=190,width=1550,height=620)
        
        
        
        #============================menu===================
        
        lbl_menu=Label(main_frame,text="MENU",font=("times new roman",20,"bold"),bg="black",fg="yellow",bd=4,relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=300,height=30)
        
        
        #==========================btn frame===================
        
        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=30,width=300,height=200)
        
        #=========================button=======================
        cust_btn=Button(btn_frame,text="CUSTOMER",command=self.cust_details,width=25,font=("times new roman",15,"bold"),bg="black",fg="green",cursor="hand1")
        cust_btn.grid(row=0,column=0)
        
        room_btn=Button(btn_frame,text="ROOM",width=25,command=self.roombooking,font=("times new roman",15,"bold"),bg="black",fg="green",cursor="hand1")
        room_btn.grid(row=25,column=0)
        
        
        details_btn=Button(btn_frame,command=self.details_room,text="DETAILS",width=25,font=("times new roman",15,"bold"),bg="black",fg="green",cursor="hand1")
        details_btn.grid(row=50,column=0)
        
        
        report_btn=Button(btn_frame,text="REPORT",width=25,font=("times new roman",15,"bold"),bg="black",fg="green",cursor="hand1")
        report_btn.grid(row=75,column=0)
        
        
        logout_btn=Button(btn_frame,text="LOGOUT",command=self.logout,width=25,font=("times new roman",15,"bold"),bg="black",fg="green",cursor="hand1")
        logout_btn.grid(row=100,column=0)
        
        
        #================RGHT SIDE IMAGE===========================
        img3=Image.open(r"C:\Users\Dell\OneDrive\Desktop\hotel management systaem\hotel4.jpg")
        img3 = img3.resize((1020,440),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        lbling=Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
        lbling.place(x=300,y=0,width=1020,height=440)
        #======================dewn images==============================
        img5=Image.open(r"C:\Users\Dell\OneDrive\Desktop\hotel management systaem\hotel5.jpg")
        img5 = img5.resize((250,200),Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        
        lbling=Label(self.root,image=self.photoimg5,bd=0,relief=RIDGE)
        lbling.place(x=0,y=430,width=250,height=200)
        
    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Cust_window(self.new_window)
        
    def roombooking(self):
        self.new_window=Toplevel(self.root)
        self.app=Roombooking(self.new_window)
        

    def details_room(self):
        self.new_window=Toplevel(self.root)
        self.app=detailsroom(self.new_window)
        
    def logout(self):
        self.root.destroy()
        
        
        
    
        

        
        
                    

        
        
        
        
        
        
        
        
        
        

if __name__ == "__main__":
    main()
