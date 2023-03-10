from tkinter import *
from tabulate import tabulate



def distable(ephem):
    print(tabulate(ephem, headers="firstrow"))


def distablewind(ephem):
    root = Tk()

    # Create a text widget to display the table
    text_widget = Text(root)
    text_widget.pack()

    # Convert the data to a formatted table string using tabulate
    table_string = tabulate(ephem, headers="firstrow", tablefmt="pipe")


    text_widget.insert(END, table_string)

    # Start the Tkinter event loop
    root.mainloop()

    