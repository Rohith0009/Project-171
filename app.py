from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from datetime import datetime
import pytz
import time

root = Tk()
root.configure(bg="pale green")
root.title("World Clock")
root.geometry("1000x600")

Heading = Label(root, text="World Clock", font=("Arial", 40), bg="pale green")
Heading.place(anchor=CENTER, relx=0.5, rely=0.07)

values = ["CET","EET","EST","EAT","IST","CST","GST","PKT","WIB","BST"]

countryLabel = Label(root, text="Select The Timezone:", font=("Arial", 25), bg="pale green")
countryLabel.place(anchor=CENTER, relx=0.33, rely=0.3)

DropDown = ttk.Combobox(root, values=values, state="readonly", font=("Arial", 25))
DropDown.place(anchor=CENTER, relx=0.67, rely=0.3)

LabelTime = Label(root, text="", font=("Arial", 25), bg="pale green")
LabelTime.place(anchor=CENTER, relx=0.5, rely=0.5)

LabelDate = Label(root, text="", font=("Arial", 25), bg="pale green")
LabelDate.place(anchor=CENTER, relx=0.5, rely=0.6)

class ShowTime:
    def Show(self):
        TimeZone = DropDown.get()
        TimeCode = ""
        if TimeZone == "CET":
            TimeCode = "Europe/Paris"

        elif TimeZone == "EET":
            TimeCode = "Africa/Cairo"

        elif TimeZone == "EST":
            TimeCode = "America/New_York"
            
        elif TimeZone == "EAT":
            TimeCode = "Europe/Moscow"
            
        elif TimeZone == "IST":
            TimeCode = "Asia/Kolkata"
            
        elif TimeZone == "CST":
            TimeCode = "Asia/Singapore"
            
        elif TimeZone == "GST":
            TimeCode = "Asia/Dubai"
            
        elif TimeZone == "PKT":
             TimeCode = "Asia/Karachi"
       
        elif TimeZone == "WIB":
            TimeCode = "Asia/Bangkok"
        
        else:
            TimeCode = "Asia/Muscat"
            
        home = pytz.timezone(TimeCode)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M:%S %p")
        LabelTime["text"] = f"Current Time: {current_time}"
        LabelTime.after(300, self.Show)
        current_date = local_time.strftime("%d-%m-%Y")
        LabelDate["text"] = f"Current Date: {current_date}"

Time = ShowTime()

showTime = Button(root, text="Show Date/Time", font=("Arial",25), bg="pale turquoise", command=Time.Show)
showTime.place(anchor=CENTER, relx=0.5, rely=0.4)


root.mainloop()
