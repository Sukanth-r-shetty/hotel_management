from tkinter import *

class Details:
    def __init__(self, root):
        self.root = root
        self.root.title("SHETTY LUNCH HOME")
        self.root.geometry("1550x800+0+0")  # Set window size

        # Create a Text widget to display the report
        self.text_area = Text(self.root, wrap=WORD, font=("Arial", 16), height=40, width=150)
        self.text_area.pack(expand=True, fill=BOTH)  # Fill entire screen

        # Insert the report text
        report_text = """Shetty Lunch Home is an ancient top-rated restaurant which is located at several places. 
The quality of the food we serve is the highest and delicious. 
We also carry Swiggy and other online orders. 
The restaurant is very peaceful and a live band occurs daily from 6 PM. 
There is also room facilities avaliable and staffs will be available 24x7
for more details 
contact:1111111111
email:xyzg@mail.com"""

        self.text_area.insert("1.0", report_text)  # Insert text into the Text widget
        self.text_area.config(state=DISABLED)  # Make text non-editable

        # Add an exit button
        self.exit_button = Button(self.root, text="Exit", font=("Arial", 14), command=self.root.destroy)
        self.exit_button.pack(pady=10)

if __name__ == "__main__":
    root = Tk()
    obj = Details(root)
    root.mainloop()
