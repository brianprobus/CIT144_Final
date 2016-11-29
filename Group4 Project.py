
mortgageAmount = eval(input('What is the original amount of your mortgage? ')) #Thinking a GUI text-box for this
apr = eval(input('What is your anual interest rate? ')) #Also a GUI text-box for this
paymentTerm = eval(input('Is your mortgage a 10, 15, 20, or 30 year fixed? ')) #Maybe a drop-down GUI box?


numberOfMonths = paymentTerm * 12
monthlyInterest = (apr * .01) / 12
monthlyPayment = (mortgageAmount * (monthlyInterest * (1 + monthlyInterest)**numberOfMonths)) / ((1 + monthlyInterest)**numberOfMonths - 1)

if paymentTerm == 10:
	paymentsRemaining = 119
elif paymentTerm == 15:
	paymentsRemaining = 179
elif paymentTerm == 20:
	paymentsRemaining = 239
elif paymentTerm == 30:
	paymentsRemaining = 359

totalInterest = 0
principal = mortgageAmount


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
	



#######################
### export to Excel ###   Still working on the export, thinking maybe a button that says "export to excel" that will run this code
#######################


#from xlwt import Workbook

#headerStyle = easyxf('pattern: pattern solid, fore_colour grey;')
#wb = Workbook()
#sheet1 = wb.add_sheet('Amortization Schedule')
 

#This writes the header

#sheet1.write(0,0,'Payments Remaining', headerStyle)
#sheet1.write(0,1,'Payment', headerStyle)
#sheet1.write(0,2,'Principal', headerStyle)
#sheet1.write(0,3,'Interest', headerStyle)
#sheet1.write(0,4,'Total Interest', headerStyle)
#sheet1.write(0,5,'Balance', headerStyle)


#This is the body

#if paymentTerm == 10:
#	paymentsRemaining = 119
#elif paymentTerm == 15:
#	paymentsRemaining = 179
#elif paymentTerm == 20:
#	paymentsRemaining = 239
#else:
#	paymentsRemaining = 359


#totalInterest = 0
#principal = mortgageAmount
#r = 1 #This starts the row at 2


#while paymentsRemaining >= 0:
#	c = 0 #This restarts the column at A each time
#	interestPaid = principal * apr / 12
#	principalPaid = monthlyPayment - interestPaid
#	totalInterest += interestPaid
#	principal -= principalPaid
#	sheet1.write(r,c,paymentsRemaining) #Replaces the print function with write to xls function
#	c += 1 #moving column over one each time
#	sheet1.write(r,c,monthlyPayment)
#	c += 1
#	sheet1.write(r,c,principalPaid)
#	c += 1	
#	sheet1.write(r,c,interestPaid)
#	c += 1
#	sheet1.write(r,c,totalInterest) 
#	c += 1
#	sheet1.write(r,c,principal) 
#	paymentsRemaining -= 1
#	r += 1 #This moves the row down every iteration of the loop


#wb.save('Amortization Schedule Export.xls')


