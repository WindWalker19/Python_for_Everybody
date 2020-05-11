x = input("Enter the number : ")
#if we only give int(x) in below line we are not having x as int, but it would result x as int only for that line. So we need 
# intitalize the x as int(x) so x is converted to int.
# Else is not a mandatory. It may consider also as last option or default result.
x = int(x)

if x <= 10:
 	print(x,"is smaller")	
elif x >= 20:
	print(x,"is greater")
else:
	print(x,"is a number between 10 and 20.")

# try/except
# It will try some bit of code and see if it works if not it would do something else.(Eliminates traceback).

