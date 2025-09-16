import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

from tkcalendar import DateEntry
from tkcalendar import *

import datetime

def get_date_time():
    global date
    global zone
    global time
    global place

    date = date_entry.get()
    date_obj = datetime.datetime.strptime(date, '%m/%d/%y')  # convert to datetime object
    date = date_obj.strftime('%Y/%m/%d')  # format the date as 'yyyy/mm/dd'

    zone = zone_entry.get()
    time = time_entry.get()
    place = place_entry.get()
    

def exit_button():
    root.destroy()
    

root = tk.Tk()
root.title("Nyagrodha")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

bg_image = Image.open("marc.jpg")
bg_image = bg_image.resize((screen_width, screen_height), Image.ANTIALIAS)
bg_image = ImageTk.PhotoImage(bg_image)

# Create a label with the background image
bg_label = tk.Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Set the width and height of the main window to the screen resolution
root.geometry("%dx%d" % (screen_width, screen_height))



date_entry = DateEntry(root, width=12, background='green',
                       foreground='white', borderwidth=2)
date_entry.pack(padx=10, pady=10)


time_label = ttk.Label(root, text="Time (HH:MM:SS):")
time_label.pack(padx=10, pady=10)

time_entry = ttk.Entry(root)
time_entry.pack(padx=10, pady=5)

zone_label = ttk.Label(root, text="Timezone (eg. +5:30):")
zone_label.pack(padx=10, pady=10)

zone_entry = ttk.Entry(root)
zone_entry.pack(padx=10, pady=5)

place_label = ttk.Label(root, text="Place of Birth:")
place_label.pack(padx=15, pady=15)


place_entry = ttk.Entry(root)
place_entry.pack(padx=10, pady=5)



calc_button = ttk.Button(root, text="Calculate", command=get_date_time)
calc_button.pack(pady=20)

exit_button_ = ttk.Button(root, text="Show Chart", command=exit_button)
exit_button_.pack(pady=20)




root.mainloop()

class person:
    def __init__(self, da, zo, ti, pl):
        self.da = da
        self.zo = zo
        self.ti = ti
        self.pl = pl
    def dat(self):
        return self.da
    def zon(self):
        return self.zo
    def tim(self):
        return self.ti
    def pla(self):
        return self.pl
    

person_ = person(date, zone, time, place)
