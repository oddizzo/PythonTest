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

print("\n")

#Sort queue from oldest to youngest
Persons.sort(reverse=True)

P2 = 1

#Entry rules
for i in Persons:
	if i >= 90:
		print("Person "+str(P2)+" is %d years old, is not allowed entry." % i)
	elif i < 18:	
		print("Person "+str(P2)+" is %d years old, is not allowed entry." % i)
	else:
		print("Person "+str(P2)+" is %d years old, is allowed entry." % i)	
	P2 += 1