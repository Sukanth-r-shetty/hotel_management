from tkinter import*
from PIL import Image,ImageTk 
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox
class Cust_window:
        
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x500+250+225")
        #====================varibale===================
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))
                
        self.var_cust_name=StringVar()
        self.var_mother=StringVar()
        self.var_gender=StringVar()
        self.var_email=StringVar()
        self.var_nationality=StringVar()
        self.var_ID_proof=StringVar()
        self.var_post=StringVar()
        self.var_mobile=StringVar()
        self.var_ID_number=StringVar()
        self.var_address=StringVar()

        
        #============title=============
        lbl_title=Label(self.root,text="ADD CUSTOMER DETAILS",font=("times new roman",15,"bold"),bg="black",fg="gold")
        lbl_title.place(x=-200,y=0,width=1550,height=50)
        
        #==================LOGO===========
        img2=Image.open(r"C:\Users\Dell\OneDrive\Desktop\hotel management systaem\logohotel.jpg")
        img2 = img2.resize((150,50),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        lbling=Label(self.root,image=self.photoimg2)
        lbling.place(x=0,y=0,width=150,height=50)
        #=====================labelframe==================
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="CUSTOMER DETAILS",padx=2,font=("times new roman",12,"bold"))
        labelframeleft.place(x=5,y=50,width=375,height=450)
        
        #l=================label and entry=================
        lbl_cust_ref=Label(labelframeleft,text="Customer_Ref",font=("times new roman",10,"bold"),padx=2,pady=4)
        lbl_cust_ref.grid(row=0,column=0)
                                  
        entry_ref=ttk.Entry(labelframeleft,width=29,textvariable=self.var_ref,font=("times new roman",10,"bold"))   
        entry_ref.grid(row=0,column=1)                       
        #cust name
        lbl_cust_ref=Label(labelframeleft,text="Customer Name:",font=("times new roman",10,"bold"),padx=2,pady=4)
        lbl_cust_ref.grid(row=1,column=0)
                                  
        entry_ref=ttk.Entry(labelframeleft,width=29,textvariable=self.var_cust_name,font=("times new roman",10,"bold"))   
        entry_ref.grid(row=1,column=1)
        #mother name
        lbl_cust_ref=Label(labelframeleft,text="Mother name:",font=("times new roman",10,"bold"),padx=2,pady=4)
        lbl_cust_ref.grid(row=2,column=0)
        
   
        
                                  
        entry_ref=ttk.Entry(labelframeleft,width=29,textvariable=self.var_mother,font=("times new roman",10,"bold"))   
        entry_ref.grid(row=2,column=1)  
        #gender combo
        lbl_cust_ref=Label(labelframeleft,text="Gender:",font=("times new roman",10,"bold"),padx=2,pady=4)
        lbl_cust_ref.grid(row=3,column=0)
        combo_gender=ttk.Combobox(labelframeleft,width=27,textvariable=self.var_gender,font=("times new roman",10,"bold"),state="readonly")   
        combo_gender["value"]=("male","female","other")
        combo_gender.grid(row=3,column=1)
                                  
            
        
        #post code
        lbl_cust_ref=Label(labelframeleft,text="Post Code:",font=("times new roman",10,"bold"),padx=2,pady=4)
        lbl_cust_ref.grid(row=4,column=0)
                                  
        entry_ref=ttk.Entry(labelframeleft,width=29,textvariable=self.var_post,font=("times new roman",10,"bold"))   
        entry_ref.grid(row=4,column=1)
        
        #mobile num
        lbl_cust_ref=Label(labelframeleft,text="Mobile Number:",font=("times new roman",10,"bold"),padx=2,pady=4)
        lbl_cust_ref.grid(row=5,column=0)
                                  
        entry_ref=ttk.Entry(labelframeleft,width=29,textvariable=self.var_mobile,font=("times new roman",10,"bold"))   
        entry_ref.grid(row=5,column=1)  
        
        #email
        lbl_cust_ref=Label(labelframeleft,text="Email ID:",font=("times new roman",10,"bold"),padx=2,pady=4)
        lbl_cust_ref.grid(row=6,column=0)
                                  
        entry_ref=ttk.Entry(labelframeleft,width=29,textvariable=self.var_email,font=("times new roman",10,"bold"))   
        entry_ref.grid(row=6,column=1)   
        
        #nationality
        lbl_cust_ref=Label(labelframeleft,text="Nationlity:",font=("times new roman",10,"bold"),padx=2,pady=4)
        lbl_cust_ref.grid(row=7,column=0)
        
        combo_nationality=ttk.Combobox(labelframeleft,width=27,textvariable=self.var_nationality,font=("times new roman",10,"bold"),state="readonly")   
        combo_nationality["value"]=("indian","astraulian","british","american","other")
        combo_nationality.grid(row=7,column=1)
                                  

        
        #idproof type combbox
        
        lbl_cust_ref=Label(labelframeleft,text="ID proof type:",font=("times new roman",10,"bold"),padx=2,pady=4)
        lbl_cust_ref.grid(row=8,column=0)
        
        combo_ID=ttk.Combobox(labelframeleft,width=27,textvariable=self.var_ID_proof,font=("times new roman",10,"bold"),state="readonly")   
        combo_ID["value"]=("Aadhar","voter ID","Passport","PAN card","other")
        combo_ID.grid(row=8,column=1)
                                  
 
        
        #id number
        lbl_cust_ref=Label(labelframeleft,text="ID Number:",font=("times new roman",10,"bold"),padx=2,pady=4)
        lbl_cust_ref.grid(row=9,column=0)
                                  
        entry_ref=ttk.Entry(labelframeleft,width=29,textvariable=self.var_ID_number,font=("times new roman",10,"bold"))   
        entry_ref.grid(row=9,column=1)   
        
        #adress
        lbl_cust_ref=Label(labelframeleft,text="Address:",font=("times new roman",10,"bold"),padx=2,pady=4)
        lbl_cust_ref.grid(row=10,column=0)
                                  
        entry_ref=ttk.Entry(labelframeleft,width=29,textvariable=self.var_address,font=("times new roman",10,"bold"))   
        entry_ref.grid(row=10,column=1)  

#=======================buutons======================
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=300,width=370,height=40)


        btnadd=Button(btn_frame,text="Add",command=self.add_data,fg="gold",bg="black",font=("times new roman",13,"bold"),padx=20)
        btnadd.grid(row=0,column=0)

        btnupdate=Button(btn_frame,text="Update",command=self.update,fg="gold",bg="black",font=("times new roman",13,"bold"),padx=20)
        btnupdate.grid(row=0,column=1)
        
        btndelete=Button(btn_frame,text="Delete",command=self.mdelete,fg="gold",bg="black",font=("times new roman",13,"bold"),padx=20)
        btndelete.grid(row=0,column=2)
        
        btnreset=Button(btn_frame,text="Reset",command=self.reset,fg="gold",bg="black",font=("times new roman",13,"bold"),padx=20)
        btnreset.grid(row=0,column=3)

#=============table frajme search system=================
        tableframe=LabelFrame(self.root,bd=2,relief=RIDGE,text="view details and search system",padx=2,font=("times new roman",10,"bold"))
        tableframe.place(x=385,y=50,width=630,height=450)

        lbl_searchby=Label(tableframe,text="Search by",font=("times new roman",15,"bold"),bg="red",fg="white")
        lbl_searchby.grid(row=0,column=0)
        
        self.search_var=StringVar()
        combo_searchby=ttk.Combobox(tableframe,textvariable=self.search_var,width=19,state="readonly")
        combo_searchby["values"]=("mobile","ref")
        combo_searchby.grid(row=0,column=1)
        
        self.txt_search=StringVar()
        txtsearch=ttk.Entry(tableframe,textvariable=self.txt_search,font=("times new roman",15,"bold"),width=15,)
        txtsearch.grid(row=0,column=2,padx=2)
        
        btnsearch=Button(tableframe,text="Search",fg="gold",command=self.search,bg="black",font=("times new roman",13,"bold"),width=10)
        btnsearch.grid(row=0,column=3)

        btnshowall=Button(tableframe,text="Showall",command=self.fetch_data,fg="gold",bg="black",font=("times new roman",13,"bold"),width=10)
        btnshowall.grid(row=0,column=4)
        
        
        #====================show data table======================
        details_table=Frame(tableframe,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=600,height=300)
        
        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.cust_details_table=ttk.Treeview(details_table,column=("ref","name","mother","gender","email","nationality","idproof","post","mobile","idnumber","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.cust_details_table.xview)
        scroll_y.config(command=self.cust_details_table.yview)
        
        self.cust_details_table.heading("ref",text="Refer No")
        self.cust_details_table.heading("name",text="Name")
        self.cust_details_table.heading("mother",text="Mother Name")
        self.cust_details_table.heading("gender",text="Gender")
        self.cust_details_table.heading("email",text="Email ID")
        self.cust_details_table.heading("nationality",text="Nationality")
        self.cust_details_table.heading("idproof",text="ID proof")
        self.cust_details_table.heading("post",text="Post")
        self.cust_details_table.heading("mobile",text="Mobile Number")
        self.cust_details_table.heading("idnumber",text="ID number")
        self.cust_details_table.heading("address",text="Address")
        
        self.cust_details_table["show"]="headings"
        self.cust_details_table.column("ref",width=100)
        self.cust_details_table.column("name",width=100)        
        self.cust_details_table.column("mother",width=100)
        self.cust_details_table.column("gender",width=100)        
        self.cust_details_table.column("email",width=200)
        self.cust_details_table.column("nationality",width=100)
        self.cust_details_table.column("idproof",width=100)        
        self.cust_details_table.column("post",width=100)
        self.cust_details_table.column("mobile",width=100)        
        self.cust_details_table.column("idnumber",width=100)
        self.cust_details_table.column("address",width=200)

        
        
        self.cust_details_table.pack(fill=BOTH,expand=1)
        self.cust_details_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
    
    
    def add_data(self):
        if self.var_mobile.get()=="" or self.var_mother.get()=="":
            messagebox.showerror("Error","All fiels are required",parent=self.root)
        else:
            try:
                    
                conn=mysql.connector.connect(host="localhost",username="root",password="Shetty994511",database="hotel_management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",( 
                                                                        self.var_ref.get(),
                                                                        self.var_cust_name.get(),
                                                                        self.var_mother.get(),
                                                                        self.var_gender.get(),
                                                                        self.var_email.get(),
                                                                        self.var_nationality.get(),
                                                                        self.var_ID_proof.get(),
                                                                        self.var_post.get(),
                                                                        self.var_mobile.get(),
                                                                        self.var_ID_number.get(),
                                                                        self.var_address.get()
                                                                )) 
                conn.commit()
                self.fetch_data()
                conn.close() 
                messagebox.showinfo("success","customer has been added",parent=self.root)
            except Exception as es:
                messagebox.showwarning("warning",f"some thing went wrong:{str(es)}",parent=self.root)
        
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Shetty994511",database="hotel_management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from customer")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.cust_details_table.delete(*self.cust_details_table.get_children())
            for i in rows:
                self.cust_details_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    def get_cursor(self,event=""):
        cursor_row=self.cust_details_table.focus()
        content=self.cust_details_table.item(cursor_row)
        row=content["values"] 
        
        self.var_ref.set(row[0]),
        self.var_cust_name.set(row[1]),
        self.var_mother.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_email.set(row[4]),
        self.var_nationality.set(row[5]),
        self.var_ID_proof.set(row[6]),
        self.var_post.set(row[7]),
        self.var_mobile.set(row[8]),
        self.var_ID_number.set(row[9]),
        self.var_address.set(row[10])





    def update(self):
        if self.var_mobile.get()=="":
            messagebox.showerror("Error","Please enter the mobile number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Shetty994511",database="hotel_management")
            my_cursor=conn.cursor()
            my_cursor.execute("update customer set name=%s,mother=%s,gender=%s,email=%s,nationality=%s,idproof=%s,post=%s,mobile=%s,id_number=%s,address=%s where ref=%s ",(
                                                                                                                                                                        
                                                                                                                                                                        self.var_cust_name.get(),
                                                                                                                                                                        self.var_mother.get(),
                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                        self.var_nationality.get(),
                                                                                                                                                                        self.var_ID_proof.get(),
                                                                                                                                                                        self.var_post.get(),
                                                                                                                                                                        self.var_mobile.get(),
                                                                                                                                                                        self.var_ID_number.get(),
                                                                                                                                                                        self.var_address.get(),
                                                                                                                                                                        self.var_ref.get()
                                                                                                                                                                ))
                              
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("update","customer details has been updated success fully",parent=self.root)
    def mdelete(self):
        mdelete=messagebox.askyesno("Hotel Management System","Do You Want To Delete The Customer",parent=self.root)
        if mdelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="Shetty994511",database="hotel_management")
            my_cursor=conn.cursor()
            query="delete from customer  where ref=%s"
            value=(self.var_ref.get(),)
        
            my_cursor.execute(query,value)
        else:
           if not mdelete:
                   return
        conn.commit()
        self.fetch_data()
        conn.close()
        
        
    def reset(self):
        # self.var_ref.set(""),
        self.var_cust_name.set(""),
        self.var_mother.set(""),
        # self.var_gender.set(""),
        self.var_email.set(""),
        # self.var_nationality.set(""),
        # self.var_ID_proof.set(""),
        self.var_post.set(""),
        self.var_mobile.set(""),
        self.var_ID_number.set(""),
        self.var_address.set("")
        

        x=random.randint(1000,9999)
        self.var_ref.set(str(x))
        
        
    def search(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Shetty994511", database="hotel_management")
        my_cursor = conn.cursor()
        
        search_by = self.search_var.get()
        search_value = self.txt_search.get()

        if search_by == "" or search_value == "":
            messagebox.showerror("Error", "Please select a search criteria and enter a value", parent=self.root)
        else:
            query = f"SELECT * FROM customer WHERE {search_by} LIKE %s"
            my_cursor.execute(query, (f"%{search_value}%",))
            rows = my_cursor.fetchall()

            if len(rows) != 0:
                self.cust_details_table.delete(*self.cust_details_table.get_children())
                for row in rows:
                    self.cust_details_table.insert("", "end", values=row)
                conn.commit()
            else:
                messagebox.showinfo("Not Found", "No matching records found.", parent=self.root)

        conn.close()

            
                                        
                                          
        
            

                              
                              
                              
                              
                              
                              
                              








if __name__ == "__main__":
    root=Tk()
    obj=Cust_window(root)
    root.mainloop()