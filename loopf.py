# for loop stores i value as each value in the loop.
#for instance it takes i takes all the vlaues one time.
for i in range(1,10):
	print(i)
print("blastoff")

friends = ["J","K","L"]
for friend in friends:
	print(friend)


#try to find the largest value.
# a is a list.
a = [1,2,3,4,5,10,3,11,14,25,12,14,12,11,0]
k=0
for i in a:
	#k = 0 #This is a bad place to define k as it prints the last value of the tuple.
	if (i > k):
		k = i # Here we swap the value with k.
print (k)

#smallest num in a 
def small():
	num = [1,21,22,11,1,2,12,122,0,40]
	j = num[0]
	k = num[-1]
	for i in num:
		if (i < j):
			j = i
	print(j)
	print("The last element in the list is:", k)

def total():
	total = 0
	sum = 0
	num = [23,12,122,44,5]
	b = (1,2,3,4) # this is a tuple.
	for i in num:
		total = total + i
		sum = sum + 1
	avg = total/ sum
	print(avg)
	print(total)

def smallest():
	j_smallest = None #None means empty.
	num = [1,21,22,11,1,2,12,122,0,40,-1]
	for i in num:
		if j_smallest is None:
			j_smallest = i
		elif i < j_smallest:
			j_smallest = i
	print(j_smallest)

total()
small()
smallest()