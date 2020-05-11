counter = 0
total = 0
while (True):
	try:
		a = input("Enter the number: ")
		a = float(a)
		total = total + a
		counter = counter + 1
		
	except:
		if (a == "done"):
			break
		else:
			print("Invalid input")
			continue
average = total/counter
print(total,counter,average)
