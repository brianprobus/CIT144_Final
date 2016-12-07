from tkinter import *

class LoanCalculator:
    def __init__ (self):    
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
        

        self.mortgageAmount = StringVar()        
        Entry(window, textvariable = self.mortgageAmount, justify = RIGHT).grid(row = 1, column = 2)
        self.apr = StringVar()
        Entry(window, textvariable = self.apr, justify = RIGHT).grid(row = 2, column = 2)
        
        
        Button(window, text = "Calculate", command = self.computePayments).grid(row = 4, column = 1)

        window.mainloop()

    def computePayments(self):
        #mortgageAmount = eval(input('What is the original amount of your mortgage? ')) #Thinking a GUI text-box for this
        #apr = eval(input('What is your anual interest rate? ')) #Also a GUI text-box for this
        paymentTerm = 10

        numberOfMonths = paymentTerm * 12
        monthlyInterest = (int(self.apr.get()) * .01) / 12
        monthlyPayment = (int(self.mortgageAmount.get()) * (monthlyInterest * (1 + monthlyInterest)**numberOfMonths)) / ((1 + monthlyInterest)**numberOfMonths - 1)

        if paymentTerm == 10:
                paymentsRemaining = 119
        elif paymentTerm == 15:
                paymentsRemaining = 179
        elif paymentTerm == 20:
                paymentsRemaining = 239
        elif paymentTerm == 30:
                paymentsRemaining = 359

        totalInterest = 0
        principal = int(self.mortgageAmount.get())


        amSchHeader = ['Pmts left','|','Payment','|','Principal','|','Interest','|','Total Interest','|','Balance']


        print(' ')


        i = 0
        for i in range(len(amSchHeader)):                 
            print(amSchHeader[i],end=' ')
            i += 1

        print(' ')

        ### Still working on format, it's close, but still needs some work

        while paymentsRemaining >= 0:
                interestPaid = principal * monthlyInterest
                principalPaid = monthlyPayment - interestPaid
                totalInterest += interestPaid
                principal -= principalPaid
                print('  ',format(paymentsRemaining,"03"),'     ', "{:.2f}".format(monthlyPayment),'  ',"{:.2f}".format(principalPaid), \
                      '    ', "{:.2f}".format(interestPaid),'     ', "{:.2f}".format(totalInterest),'       ', "{:.2f}".format(principal))
                paymentsRemaining -= 1
	

    
    
LoanCalculator()

