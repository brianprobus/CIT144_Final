# group project GUI

from tkinter import *

class LoanCalculator:
    
    window = Tk() # Create a window
    window.title("Loan Calculator")# Set title
    window.geometry("300x150")

    Label(window, text = "mortgage Amount").grid(row = 1, 
            column = 1, sticky = W)
    Label(window, text = "APR").grid(row = 2, 
           column = 1, sticky = W)
    Label(window, text = "Payment Term").grid(row = 3, 
          column = 1, sticky = W)

    # drop down menu
    mb=  Menubutton (window, text="Fixed Rates", relief=RAISED )
    mb.grid(row = 3, column = 2)
    mb.menu  =  Menu (mb, tearoff = 0)
    mb["menu"]  =  mb.menu
    
    tenVar  = IntVar()
    fithteenVar = IntVar()
    twentyVar  = IntVar()
    thirtyVar  = IntVar()

    mb.menu.add_checkbutton (label="10 Year",
                              variable = tenVar)
    mb.menu.add_checkbutton (label="15 Year",
                              variable = fithteenVar)
    mb.menu.add_checkbutton (label="20 Year",
                              variable = twentyVar)
    mb.menu.add_checkbutton (label="30 Year",
                              variable = thirtyVar)

            
    Entry(window, justify = RIGHT).grid(row = 1, column = 2)
    Entry(window, justify = RIGHT).grid(row = 2, column = 2)
    
    
    Button(window, text = "Calculate").grid(row = 4, column = 1)

    window.mainloop()
    
LoanCalculator()
