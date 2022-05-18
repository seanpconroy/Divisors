value = int(input("Enter number: "))


def find_divisors(value):
	i = 1
	while i <= value and i != None:
		if (value % i==0) :
			print (i,end=" ")
		i = i + 1


def countMultiples(value):
    res = 0;
    for i in range(1, value + 1):
        if (i % 3 == 0 or i % 7 == 0):
            print (i,end=" ")
            res += 1;
  
    

print("Divisors: ")
find_divisors(value)

print("\nCount of multiples of 3 or 7 or both: ")
countMultiples(value)

