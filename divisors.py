value = int(input("Enter number: "))


def find_divisors(value):
	i = 1
	while i <= value and i != None:
		if (value % i==0) :
			print (i,end=" ")
		i = i + 1

find_divisors(value)