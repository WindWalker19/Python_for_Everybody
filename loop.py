#A while loop with break.
while True:
	line = input("> ")
	if line == "done":
		print(line)
		break
print("Blastoff")


while True:
	line = input("> ")
	if line[0] == "#":
		continue # The continue would ask to go to the top of the loop without executing the code after it.
		print("hello")
	if line == "done":
		break
print("Blastoff")
