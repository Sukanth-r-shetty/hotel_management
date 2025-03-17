from tkinter import *
from PIL import Image,ImageTk  
from customer import Cust_window
from room import Roombooking
from details import detailsroom
from report import Details

          


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
        
        
        report_btn=Button(btn_frame,text="REPORT",command=self.report_hotel,width=25,font=("times new roman",15,"bold"),bg="black",fg="green",cursor="hand1")
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
        
    def report_hotel(self):
        self.new_window=Toplevel(self.root)
        self.app=Details(self.new_window)
        
        
    def logout(self):
        self.root.destroy()
        
        
        
        
if __name__=="__main__":
    root=Tk()
    obj=HotelManagementSystem(root)
    root.mainloop()
    