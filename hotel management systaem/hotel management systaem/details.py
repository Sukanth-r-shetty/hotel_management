from tkinter import*
from PIL import Image,ImageTk 
from tkinter import ttk
from time import strftime
from datetime import datetime
import mysql.connector
import random
from tkinter import messagebox


class detailsroom:
        
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x500+250+225")
        
        
        lbl_title=Label(self.root,text="ROOM BOOKING DETAILS",font=("times new roman",15,"bold"),bg="black",fg="gold")
        lbl_title.place(x=-200,y=0,width=1550,height=50)
        
        #==================LOGO===========
        img2=Image.open(r"C:\Users\Dell\OneDrive\Desktop\hotel management systaem\logohotel.jpg")
        img2 = img2.resize((150,50),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        lbling=Label(self.root,image=self.photoimg2)
        lbling.place(x=0,y=0,width=150,height=50)
        
         #=====================labelframe==================
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="NEW ROOM ADD",padx=2,font=("times new roman",12,"bold"))
        labelframeleft.place(x=5,y=50,width=490,height=300) 
        
        
        #FLOOR        
        lbl_floor=Label(labelframeleft,text="Floor",font=("times new roman",15,"bold"),padx=2,pady=4)
        lbl_floor.grid(row=0,column=0)

        
        self.var_floor=StringVar()                         
        entry_floor=ttk.Entry(labelframeleft,textvariable=self.var_floor,width=20,font=("times new roman",15,"bold"))   
        entry_floor.grid(row=0,column=1,sticky=W) 
        
        #rommnumber
        lbl_room_no=Label(labelframeleft,text="Room_No",font=("times new roman",15,"bold"),padx=2,pady=4)
        lbl_room_no.grid(row=1,column=0)
        

        
        self.var_RoomNo=StringVar()                          
        entry_room_no=ttk.Entry(labelframeleft,textvariable=self.var_RoomNo,width=20,font=("times new roman",15,"bold"))   
        entry_room_no.grid(row=1,column=1,sticky=W) 
        
        
        #rommntype
        lbl_room_type=Label(labelframeleft,text="Room_type",font=("times new roman",15,"bold"),padx=2,pady=4)
        lbl_room_type.grid(row=2,column=0)

        
        self.var_RoomType=StringVar()                          
        entry_room_type=ttk.Entry(labelframeleft,textvariable=self.var_RoomType,width=20,font=("times new roman",15,"bold"))   
        entry_room_type.grid(row=2,column=1,sticky=W) 
          
        
        
        
        
        
        #btn frame and entry
        
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=200,width=370,height=40)


        btnadd=Button(btn_frame,text="Add",command=self.add_data,fg="gold",bg="black",font=("times new roman",13,"bold"),padx=20)
        btnadd.grid(row=0,column=0)

        btnupdate=Button(btn_frame,text="Update",command=self.update,fg="gold",bg="black",font=("times new roman",13,"bold"),padx=20)
        btnupdate.grid(row=0,column=1)
        
        btndelete=Button(btn_frame,text="Delete",command=self.mdelete,fg="gold",bg="black",font=("times new roman",13,"bold"),padx=20)
        btndelete.grid(row=0,column=2)
        
        btnreset=Button(btn_frame,text="Reset",command=self.reset,fg="gold",bg="black",font=("times new roman",13,"bold"),padx=20)
        btnreset.grid(row=0,column=3) 
        
        #=============table frajme search system=================
        tableframe=LabelFrame(self.root,bd=2,relief=RIDGE,text="SHOW ROOM DETAILS",padx=2,font=("times new roman",10,"bold"))
        tableframe.place(x=500,y=50,width=500,height=300)
    
        scroll_x=ttk.Scrollbar(tableframe,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(tableframe,orient=VERTICAL)
        
            
        self.room_table=ttk.Treeview(tableframe,column=("Floor","RoomNo","RoomType"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)
        
        
        
        self.room_table.heading("Floor",text="Floor")
        self.room_table.heading("RoomNo",text="Room No")
        self.room_table.heading("RoomType",text="Room Type")

        self.room_table["show"]="headings"
        
        self.room_table.column("Floor",width=100)        
        self.room_table.column("RoomNo",width=100)
        self.room_table.column("RoomType",width=100)        

         

        
        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
        
 #add data
    def add_data(self):
        if self.var_floor.get()=="" or self.var_RoomType.get()=="":
            messagebox.showerror("Error","All fiels are required",parent=self.root)
        else:
            try:
                    
                conn=mysql.connector.connect(host="localhost",username="root",password="Shetty994511",database="hotel_management")
                my_cursor=conn.cursor()
                my_cursor.execute("INSERT INTO details VALUES (%s, %s, %s)", ( 
                                                                                            self.var_floor.get(),
                                                                                            self.var_RoomNo.get(),
                                                                                            self.var_RoomType.get(),


                                                                                        )) 
                conn.commit()
                self.fetch_data()
                conn.close() 
                messagebox.showinfo("success","New Room Added Successfully ",parent=self.root)
            except Exception as es:
                
                messagebox.showwarning("warning",f"some thing went wrong:{str(es)}",parent=self.root)
        #fetch data
    def fetch_data(self):
            conn=mysql.connector.connect(host="localhost",username="root",password="Shetty994511",database="hotel_management")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from details")
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
        
    
        self.var_floor.set(row[0]),
        self.var_RoomNo.set(row[1]),
        self.var_RoomType.set(row[2])
#updatw

    def update(self):
        if self.var_floor.get()=="":
            messagebox.showerror("Error","Please enter the mobile number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Shetty994511",database="hotel_management")
            my_cursor=conn.cursor()
            my_cursor.execute("update details set Floor=%s,RoomType=%s where RoomNo=%s",(
                                                                                                                                            
                                                                                                                                            self.var_floor.get(),
                                                                                                                                            self.var_RoomType.get(),
                                                                                                                                            self.var_RoomNo.get()
                                                                                                                                          

                                                                                                                                        ))
                              
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("update","New room details has been updated success fully",parent=self.root)
            
    def mdelete(self):
        mdelete=messagebox.askyesno("Hotel Management System","Do You Want To Delete The Room Details",parent=self.root)
        if mdelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="Shetty994511",database="hotel_management")
            my_cursor=conn.cursor()
            query="delete from details  where RoomNo=%s"
            value=(self.var_RoomNo.get(),)
        
            my_cursor.execute(query,value)
        else:
           if not mdelete:
                   return
        conn.commit()
        self.fetch_data()
        conn.close()
        
        #reset
    def reset(self):
        self.var_floor.set(""),
        self.var_RoomNo.set(""),
        self.var_RoomType.set(""),

        

     





        
        
        
        
        
        
if __name__ == "__main__":
    root=Tk()
    obj=detailsroom(root)
    root.mainloop()