P1 = 1
Persons = []

#Enter Persons Age
for i in range(1, 18):
	q = int(input("Enter age of person %d: " % i))
	if i == 17:
		Persons.append(Persons[14]+q)
	else:	
		Persons.append(q)

print("\n")

#Print Persons Age
for i in Persons:
	print("Person "+str(P1)+" is %d years old." % i)
	P1 += 1

print("\n")

#Show X
print("X is equal to "+str(Persons[16]))