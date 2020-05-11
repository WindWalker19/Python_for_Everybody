#Handling Exceptions in python
val = input("Enter a number: ")
try:
	val = int(val)
except:
	val = -1
if(val >= 0):
	print("Nice work")
elif(val < 0):
	print("It is not a number.")
