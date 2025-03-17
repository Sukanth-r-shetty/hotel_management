from tkinter import *
from tkinter import ttk

class Login_window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        


        self.root.geometry("1550x800+0+0") # Adjusted size for better visibility
       

if __name__ == "__main__":
    root = Tk()
    obj = Login_window(root)
    root.mainloop()
