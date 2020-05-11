#3.1 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string and float() to convert the string to a number. Do not worry about error checking the user input - assume the user types numbers properly.
hrs = input("Enter Hours:")
Normal_rate = input("Enter the rate: ")
Increased_rate = input("Enter the increase rate: ")
try:
	NR = float(Normal_rate)
	IR = float(Increased_rate)
	h = float(hrs)
	gross_pay = 0
#Ends the program using the quit function.
except:
	print("Invalid input or input is not a number.")
	quit()
#paying for normaltime.
if(h == 40):
    gross_pay = h * NR
#Paying for overtime.
elif(h > 40):
    nh = 40
    eh = h - nh
    gross_pay = (nh * NR) + (eh * NR * IR)
print(gross_pay)