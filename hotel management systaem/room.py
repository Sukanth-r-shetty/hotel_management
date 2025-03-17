from tkinter import*
from PIL import Image,ImageTk 
from tkinter import ttk
from time import strftime
from datetime import datetime
import mysql.connector
import random
from tkinter import messagebox


class Roombooking:
        
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x500+250+225")
        
        
        
        #============variable=================
        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomavailable=StringVar()
        self.var_meal=StringVar()
        self.var_noofdays=StringVar()
        self.var_paidtax=StringVar()
        self.var_actualtotal=StringVar()
        self.var_total=StringVar()
        #==========title==========================
        
        lbl_title=Label(self.root,text="ROOM BOOKING DETAILS",font=("times new roman",15,"bold"),bg="black",fg="gold")
        lbl_title.place(x=-200,y=0,width=1550,height=50)
        
        #==================LOGO===========
        img2=Image.open(r"C:\Users\Dell\OneDrive\Desktop\hotel management systaem\logohotel.jpg")
        img2 = img2.resize((150,50),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        lbling=Label(self.root,image=self.photoimg2)
        lbling.place(x=0,y=0,width=150,height=50)
        
                #=====================labelframe==================
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="ROOM BOOKING DETAILS",padx=2,font=("times new roman",12,"bold"))
        labelframeleft.place(x=5,y=50,width=375,height=450)       
        
        
        #l=================label and entry=================
        
        #customer_conatct
        
        lbl_cust_contact=Label(labelframeleft,text="Customer contact",font=("times new roman",10,"bold"),padx=2,pady=4)
        lbl_cust_contact.grid(row=0,column=0)

        
                                  
        entry_cust_contact=ttk.Entry(labelframeleft,width=20,textvariable=self.var_contact,font=("times new roman",10,"bold"))   
        entry_cust_contact.grid(row=0,column=1,sticky=W) 
        
        #fetch data btn
        btnfetch=Button(labelframeleft,command=self.Fetch_contact,text="Fetch data",fg="gold",bg="black",font=("times new roman",8,"bold"),padx=20)
        btnfetch.place(x=260,y=4)
        
        
        
        #check in date
        lbl_check_in=Label(labelframeleft,text="Check in date",font=("times new roman",10,"bold"),padx=2,pady=4)
        lbl_check_in.grid(row=1,column=0)
                                  
        entry_check_in=ttk.Entry(labelframeleft,width=29,textvariable=self.var_checkin,font=("times new roman",10,"bold"))   
        entry_check_in.grid(row=1,column=1)
        
        #mcheck out date
        lbl_check_out=Label(labelframeleft,text="Check out date",font=("times new roman",10,"bold"),padx=2,pady=4)
        lbl_check_out.grid(row=2,column=0)
        
        entry_check_out=ttk.Entry(labelframeleft,width=29,textvariable=self.var_checkout,font=("times new roman",10,"bold"))   
        entry_check_out.grid(row=2,column=1) 
        
         
        #room type
        lbl_room_type=Label(labelframeleft,text="Room type",font=("times new roman",10,"bold"),padx=2,pady=4)
        lbl_room_type.grid(row=3,column=0)
        
        
        conn=mysql.connector.connect(host="localhost",username="root",password="Shetty994511",database="hotel_management")
        my_cursor=conn.cursor()
        my_cursor.execute("select RoomType from details")
        ide=my_cursor.fetchall()
        
        combo_room_type=ttk.Combobox(labelframeleft,width=27,textvariable=self.var_roomtype,font=("times new roman",10,"bold"),state="readonly")   
        combo_room_type["value"]=ide
        combo_room_type.current(0)
        combo_room_type.grid(row=3,column=1)
        
        #available room
        lbl_available_room=Label(labelframeleft,text="Available room",font=("times new roman",10,"bold"),padx=2,pady=4)
        lbl_available_room.grid(row=4,column=0)
                                  
        # entry_available_room=ttk.Entry(labelframeleft,width=29,textvariable=self.var_roomavailable,font=("times new roman",10,"bold"))   
        # entry_available_room.grid(row=4,column=1)
        conn=mysql.connector.connect(host="localhost",username="root",password="Shetty994511",database="hotel_management")
        my_cursor=conn.cursor()
        my_cursor.execute("select RoomNo from details")
        rows=my_cursor.fetchall()
            
        combo_RoomNo=ttk.Combobox(labelframeleft,width=27,textvariable=self.var_roomavailable,font=("times new roman",10,"bold"),state="readonly")   
        combo_RoomNo["value"]=rows
        combo_RoomNo.current(0)
        combo_RoomNo.grid(row=4,column=1)
        
        #meal
        lbl_meal=Label(labelframeleft,text="Meal",font=("times new roman",10,"bold"),padx=2,pady=4)
        lbl_meal.grid(row=5,column=0)
                                  
        entry_meal=ttk.Entry(labelframeleft,width=29,textvariable=self.var_meal,font=("times new roman",10,"bold"))   
        entry_meal.grid(row=5,column=1)  
        
                
        #_no_of_days
        lbl_no_of_days=Label(labelframeleft,text="No. of days",font=("times new roman",10,"bold"),padx=2,pady=4)
        lbl_no_of_days.grid(row=6,column=0)
                                  
        entry_no_of_days=ttk.Entry(labelframeleft,width=29,textvariable=self.var_noofdays,font=("times new roman",10,"bold"))   
        entry_no_of_days.grid(row=6,column=1)   
    
        #n_paid_tax
        lbl_paid_tax=Label(labelframeleft,text="Paid tax",font=("times new roman",10,"bold"),padx=2,pady=4)
        lbl_paid_tax.grid(row=7,column=0)
        
        entry_paid_tax=ttk.Entry(labelframeleft,width=29,textvariable=self.var_paidtax,font=("times new roman",10,"bold"))   
        entry_paid_tax.grid(row=7,column=1)   
        
                #_subtotal
        lbl_subtotal=Label(labelframeleft,text="Subtotal",font=("times new roman",10,"bold"),padx=2,pady=4)
        lbl_subtotal.grid(row=8,column=0)
        
        entry_subtotal=ttk.Entry(labelframeleft,width=29,textvariable=self.var_actualtotal,font=("times new roman",10,"bold"))   
        entry_subtotal.grid(row=8,column=1)   
                #n_total
        lbl_total=Label(labelframeleft,text="Total",font=("times new roman",10,"bold"),padx=2,pady=4)
        lbl_total.grid(row=9,column=0)
        
        entry_total=ttk.Entry(labelframeleft,width=29,textvariable=self.var_total,font=("times new roman",10,"bold"))   
        entry_total.grid(row=9,column=1)  
        
        #bill button
        btnadd=Button(labelframeleft,text="Bill",fg="gold",command=self.total,bg="black",font=("times new roman",10,"bold"),padx=20)
        btnadd.grid(row=10,column=0)
        
        
        
        #btn frame and entry
        
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=300,width=370,height=40)


        btnadd=Button(btn_frame,text="Add",command=self.add_data,fg="gold",bg="black",font=("times new roman",13,"bold"),padx=20)
        btnadd.grid(row=0,column=0)

        btnupdate=Button(btn_frame,text="Update",command=self.update,fg="gold",bg="black",font=("times new roman",13,"bold"),padx=20)
        btnupdate.grid(row=0,column=1)
        
        btndelete=Button(btn_frame,command=self.mdelete,text="Delete",fg="gold",bg="black",font=("times new roman",13,"bold"),padx=20)
        btndelete.grid(row=0,column=2)
        
        btnreset=Button(btn_frame,text="Reset",command=self.reset,fg="gold",bg="black",font=("times new roman",13,"bold"),padx=20)
        btnreset.grid(row=0,column=3) 
        
        #========right side image============
        img3=Image.open(r"C:\Users\Dell\OneDrive\Desktop\hotel management systaem\roompic.jpg")
        img3 = img3.resize((630,140),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        lbling=Label(self.root,image=self.photoimg3,bd=4,relief=RIDGE)
        lbling.place(x=650,y=50,width=630,height=140)
        
        #=============table frajme search system=================
        tableframe=LabelFrame(self.root,bd=2,relief=RIDGE,text="view details and search system",padx=2,font=("times new roman",10,"bold"))
        tableframe.place(x=385,y=190,width=630,height=450)

        lbl_searchby=Label(tableframe,text="Search by",font=("times new roman",15,"bold"),bg="red",fg="white")
        lbl_searchby.grid(row=0,column=0)
        
        self.search_var=StringVar()
        combo_searchby=ttk.Combobox(tableframe,textvariable=self.search_var,width=19,state="readonly")
        combo_searchby["values"]=("Contact","Room")
        combo_searchby.grid(row=0,column=1)
        
        self.txt_search=StringVar()
        txtsearch=ttk.Entry(tableframe,textvariable=self.txt_search,font=("times new roman",15,"bold"),width=15,)
        txtsearch.grid(row=0,column=2,padx=2)
        
        btnsearch=Button(tableframe,text="Search",command=self.search,fg="gold",bg="black",font=("times new roman",13,"bold"),width=10)
        btnsearch.grid(row=0,column=3)

        btnshowall=Button(tableframe,text="Showall",command=self.fetch_data,fg="gold",bg="black",font=("times new roman",13,"bold"),width=10)
        btnshowall.grid(row=0,column=4)
        
        
        #====================show data table======================
        
        details_table=Frame(tableframe,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=600,height=160)
        
        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.room_table=ttk.Treeview(details_table,column=("contact","checkin","checkout","roomtype","roomavailable","meal","Noofdays"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)
        
        self.room_table.heading("contact",text="Contact")
        self.room_table.heading("checkin",text="Checkin")
        self.room_table.heading("checkout",text="Checkout")
        self.room_table.heading("roomtype",text="Room type")
        self.room_table.heading("roomavailable",text="Room No")
        self.room_table.heading("meal",text="Meal")
        self.room_table.heading("Noofdays",text="NoOfDays")
        
        self.room_table["show"]="headings"
        
        self.room_table.column("contact",width=100)        
        self.room_table.column("checkin",width=100)
        self.room_table.column("checkout",width=100)        
        self.room_table.column("roomtype",width=100)
        self.room_table.column("roomavailable",width=100)        
        self.room_table.column("meal",width=100)
        self.room_table.column("Noofdays",width=100)
         

        
        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
        
        
        #add data
    def add_data(self):
        if self.var_contact.get()=="" or self.var_checkin.get()=="":
            messagebox.showerror("Error","All fiels are required",parent=self.root)
        else:
            try:
                    
                conn=mysql.connector.connect(host="localhost",username="root",password="Shetty994511",database="hotel_management")
                my_cursor=conn.cursor()
                my_cursor.execute("INSERT INTO room VALUES (%s, %s, %s, %s, %s, %s, %s)", ( 
                                                                                            self.var_contact.get(),
                                                                                            self.var_checkin.get(),
                                                                                            self.var_checkout.get(),
                                                                                            self.var_roomtype.get(),
                                                                                            self.var_roomavailable.get(),
                                                                                            self.var_meal.get(),
                                                                                            self.var_noofdays.get()

                                                                                        )) 
                conn.commit()
                self.fetch_data()
                conn.close() 
                messagebox.showinfo("success","Room has been booked successfully",parent=self.root)
            except Exception as es:
                messagebox.showwarning("warning",f"some thing went wrong:{str(es)}",parent=self.root)
                
        #fetch data
    def fetch_data(self):
            conn=mysql.connector.connect(host="localhost",username="root",password="Shetty994511",database="hotel_management")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from room")
            rows=my_cursor.fetchall()
            if len(rows)!=0:
                self.room_table.delete(*self.room_table.get_children())
                for i in rows:
                    self.room_table.insert("",END,values=i)
                conn.commit()
            conn.close()
      #get cursor      
    def get_cursor(self,event=""):
        cursor_row=self.room_table.focus()
        content=self.room_table.item(cursor_row)
        row=content["values"] 
        
    
        self.var_contact.set(row[0]),
        self.var_checkin.set(row[1]),
        self.var_checkout.set(row[2]),
        self.var_roomtype.set(row[3]),
        self.var_roomavailable.set(row[4]),
        self.var_meal.set(row[5]),
        self.var_noofdays.set(row[6])
        
        #updatw

    def update(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please enter the mobile number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Shetty994511",database="hotel_management")
            my_cursor=conn.cursor()
            my_cursor.execute("update room set check_in=%s,check_out=%s,roomtype=%s,roomavailable=%s,meal=%s,noofdays=%s where contact=%s ",(
                                                                                                                                            
                                                                                                                                            self.var_checkin.get(),
                                                                                                                                            self.var_checkout.get(),
                                                                                                                                            self.var_roomtype.get(),
                                                                                                                                            self.var_roomavailable.get(),
                                                                                                                                            self.var_meal.get(),
                                                                                                                                            self.var_noofdays.get(),
                                                                                                                                            self.var_contact.get()

                                                                                                                                        ))
                              
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("update","room details has been updated success fully",parent=self.root)
    def mdelete(self):
        mdelete=messagebox.askyesno("Hotel Management System","Do You Want To Delete The Customer",parent=self.root)
        if mdelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="Shetty994511",database="hotel_management")
            my_cursor=conn.cursor()
            query="delete from room  where contact=%s"
            value=(self.var_contact.get(),)
        
            my_cursor.execute(query,value)
        else:
           if not mdelete:
                   return
        conn.commit()
        self.fetch_data()
        conn.close()
        
        #reset
    def reset(self):
        self.var_contact.set(""),
        self.var_checkin.set(""),
        self.var_checkout.set(""),
        self.var_roomtype.set(""),
        self.var_roomavailable.set(""),
        self.var_meal.set(""),
        self.var_noofdays.set("")
        self.var_paidtax.set("")
        self.var_actualtotal.set("")
        self.var_total.set("")
        

     



        
        
        
        #================all DATAV FETCH======================
    def Fetch_contact(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please Enter Contact Number",parent=self.root)
        else:
                conn=mysql.connector.connect(host="localhost",username="root",password="Shetty994511",database="hotel_management")
                my_cursor=conn.cursor()
                query=("select name from customer where mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                
            ###########################################
                
                if row==None:
                        messagebox.showerror("Error","This number is not found",parent=self.root)
                else:
                        conn.commit()
                        conn.close()
                        #name========================
                        showdataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                        showdataframe.place(x=385,y=50,width=265,height=145)
                        
                        lblname=Label(showdataframe,text="Name:",font=("arial",8,"bold"))
                        lblname.place(x=0,y=0)
                        
                        
                        lbl=Label(showdataframe,text=row,font=("arial",7,"bold"))
                        lbl.place(x=70,y=0)
                        #gender================
                        conn=mysql.connector.connect(host="localhost",username="root",password="Shetty994511",database="hotel_management")
                        my_cursor=conn.cursor()
                        query=("select gender from customer where mobile=%s")
                        value=(self.var_contact.get(),)
                        my_cursor.execute(query,value)
                        row=my_cursor.fetchone()
                        
                        lblgender=Label(showdataframe,text="Gender:",font=("arial",8,"bold"))
                        lblgender.place(x=0,y=25)
                        
                        
                        lbl2=Label(showdataframe,text=row,font=("arial",7,"bold"))
                        lbl2.place(x=70,y=25)
                        #email=========================
                        conn=mysql.connector.connect(host="localhost",username="root",password="Shetty994511",database="hotel_management")
                        my_cursor=conn.cursor()
                        query=("select email from customer where mobile=%s")
                        value=(self.var_contact.get(),)
                        my_cursor.execute(query,value)
                        row=my_cursor.fetchone()
                        
                        lblgender=Label(showdataframe,text="Email:",font=("arial",8,"bold"))
                        lblgender.place(x=0,y=50)
                        
                        
                        lbl3=Label(showdataframe,text=row,font=("arial",7,"bold"))
                        lbl3.place(x=70,y=50)
                        
                        #nationality==========================
                        conn=mysql.connector.connect(host="localhost",username="root",password="Shetty994511",database="hotel_management")
                        my_cursor=conn.cursor()
                        query=("select nationality from customer where mobile=%s")
                        value=(self.var_contact.get(),)
                        my_cursor.execute(query,value)
                        row=my_cursor.fetchone()
                        
                        lblnationality=Label(showdataframe,text="Nationality:",font=("arial",8,"bold"))
                        lblnationality.place(x=0,y=75)
                        
                        
                        lbl4=Label(showdataframe,text=row,font=("arial",7,"bold"))
                        lbl4.place(x=80,y=75)
                        #address======================================
                        conn=mysql.connector.connect(host="localhost",username="root",password="Shetty994511",database="hotel_management")
                        my_cursor=conn.cursor()
                        query=("select address from customer where mobile=%s")
                        value=(self.var_contact.get(),)
                        my_cursor.execute(query,value)
                        row=my_cursor.fetchone()
                        
                        lbladdress=Label(showdataframe,text="Address:",font=("arial",8,"bold"))
                        lbladdress.place(x=0,y=100)
                        
                        
                        lbl5=Label(showdataframe,text=row,font=("arial",7,"bold"))
                        lbl5.place(x=60,y=100)
    #serach system
    
    def search(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Shetty994511", database="hotel_management")
        my_cursor = conn.cursor()
        
        # my_cursor.execute("select * from room where "+str(self.search_var.get())+"LIKEX'%"+str(self.txt_search.get())+"%'")
        # rows=my_cursor.fetchall()
        
        query = "SELECT * FROM room WHERE {} LIKE %s".format(self.search_var.get())
        search_value = "%" + str(self.txt_search.get()) + "%"
        my_cursor.execute(query, (search_value,))
        rows = my_cursor.fetchall()
        
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()

                        
    def total(self):
        indate=self.var_checkin.get()
        outdate=self.var_checkout.get()
        indate=datetime.strptime(indate,"%d/%m/%Y") 
        outdate=datetime.strptime(outdate,"%d/%m/%Y")   
        self.var_noofdays.set(abs(outdate-indate).days)   
        
        if (self.var_meal.get()=="breakfast" and self.var_roomtype.get()=="luxury"):
            q1=float(100)
            q2=float(700)
            q3=float(self.var_noofdays.get()) 
            q4=float(q1+q2)
            q5=float(q3+q4)
            tax="Rs."+str("%.2f"%((q5)*0.18))       
            ST="Rs."+str("%.2f"%((q5)))     
            TT="Rs."+str("%.2f"%(q5+((q5)*0.18)))
            self.var_paidtax.set(tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
            # self.var_paidtax=StringVar()
            # self.var_actualtotal=StringVar()
            # self.var_total=StringVar()
            
        elif (self.var_meal.get()=="breakfast" and self.var_roomtype.get()=="single"):
            q1=float(100)
            q2=float(400)
            q3=float(self.var_noofdays.get()) 
            q4=float(q1+q2)
            q5=float(q3+q4)
            tax="rs."+str("%.2f"%((q5)*0.18))       
            ST="rs."+str("%.2f"%((q5)))     
            TT="rs."+str("%.2f"%(q5+((q5)*0.18)))
            self.var_paidtax.set(tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
        elif (self.var_meal.get()=="breakfast" and self.var_roomtype.get()=="double"):
            q1=float(100)
            q2=float(500)
            q3=float(self.var_noofdays.get()) 
            q4=float(q1+q2)
            q5=float(q3+q4)
            tax="rs."+str("%.2f"%((q5)*0.18))       
            ST="rs."+str("%.2f"%((q5)))     
            TT="rs."+str("%.2f"%(q5+((q5)*0.18)))
            self.var_paidtax.set(tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
        elif (self.var_meal.get()=="lunch" and self.var_roomtype.get()=="double"):
            q1=float(200)
            q2=float(500)
            q3=float(self.var_noofdays.get()) 
            q4=float(q1+q2)
            q5=float(q3+q4)
            tax="rs."+str("%.2f"%((q5)*0.18))       
            ST="rs."+str("%.2f"%((q5)))     
            TT="rs."+str("%.2f"%(q5+((q5)*0.18)))
            self.var_paidtax.set(tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
        elif (self.var_meal.get()=="lunch" and self.var_roomtype.get()=="single"):
            q1=float(200)
            q2=float(400)
            q3=float(self.var_noofdays.get()) 
            q4=float(q1+q2)
            q5=float(q3+q4)
            tax="rs."+str("%.2f"%((q5)*0.18))       
            ST="rs."+str("%.2f"%((q5)))     
            TT="rs."+str("%.2f"%(q5+((q5)*0.18)))
            self.var_paidtax.set(tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
        elif (self.var_meal.get()=="lunch" and self.var_roomtype.get()=="luxury"):
            q1=float(200)
            q2=float(700)
            q3=float(self.var_noofdays.get()) 
            q4=float(q1+q2)
            q5=float(q3+q4)
            tax="rs."+str("%.2f"%((q5)*0.18))       
            ST="rs."+str("%.2f"%((q5)))     
            TT="rs."+str("%.2f"%(q5+((q5)*0.18)))
            self.var_paidtax.set(tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
        elif (self.var_meal.get()=="dinner" and self.var_roomtype.get()=="luxury"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofdays.get()) 
            q4=float(q1+q2)
            q5=float(q3+q4)
            tax="rs."+str("%.2f"%((q5)*0.18))       
            ST="rs."+str("%.2f"%((q5)))     
            TT="rs."+str("%.2f"%(q5+((q5)*0.18)))
            self.var_paidtax.set(tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
        elif (self.var_meal.get()=="dinner" and self.var_roomtype.get()=="single"):
            q1=float(300)
            q2=float(400)
            q3=float(self.var_noofdays.get()) 
            q4=float(q1+q2)
            q5=float(q3+q4)
            tax="rs."+str("%.2f"%((q5)*0.18))       
            ST="rs."+str("%.2f"%((q5)))     
            TT="rs."+str("%.2f"%(q5+((q5)*0.18)))
            self.var_paidtax.set(tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
            
        elif (self.var_meal.get()=="dinner" and self.var_roomtype.get()=="double"):
            q1=float(300)
            q2=float(500)
            q3=float(self.var_noofdays.get()) 
            q4=float(q1+q2)
            q5=float(q3+q4)
            tax="rs."+str("%.2f"%((q5)*0.18))       
            ST="rs."+str("%.2f"%((q5)))     
            TT="rs."+str("%.2f"%(q5+((q5)*0.18)))
            self.var_paidtax.set(tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
        elif (self.var_meal.get()=="breakfast" and self.var_roomtype.get()=="duplex"):
            q1=float(100)
            q2=float(1000)
            q3=float(self.var_noofdays.get()) 
            q4=float(q1+q2)
            q5=float(q3+q4)
            tax="rs."+str("%.2f"%((q5)*0.18))       
            ST="rs."+str("%.2f"%((q5)))     
            TT="rs."+str("%.2f"%(q5+((q5)*0.18)))
            self.var_paidtax.set(tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
            
        elif (self.var_meal.get()=="lunch" and self.var_roomtype.get()=="duplex"):
            q1=float(200)
            q2=float(800)
            q3=float(self.var_noofdays.get()) 
            q4=float(q1+q2)
            q5=float(q3+q4)
            tax="rs."+str("%.2f"%((q5)*0.18))       
            ST="rs."+str("%.2f"%((q5)))     
            TT="rs."+str("%.2f"%(q5+((q5)*0.18)))
            self.var_paidtax.set(tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
        elif (self.var_meal.get()=="dinner" and self.var_roomtype.get()=="duplex"):
            q1=float(300)
            q2=float(800)
            q3=float(self.var_noofdays.get()) 
            q4=float(q1+q2)
            q5=float(q3+q4)
            tax="rs."+str("%.2f"%((q5)*0.18))       
            ST="rs."+str("%.2f"%((q5)))     
            TT="rs."+str("%.2f"%(q5+((q5)*0.18)))
            self.var_paidtax.set(tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
        
        
            
        

                            
                        



                        
        

        
      

















if __name__ == "__main__":
    root=Tk()
    obj=Roombooking(root)
    root.mainloop()