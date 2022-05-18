value = int(input("Enter number: ")) #get user input


def find_divisors(value): #function to find the divisors
	i = 1
	while i <= value and i != None:
		if (value % i==0) :
			print (i,end=" ")
		i = i + 1


def countMultiples(value): #function to find multiples
    res = 0;
    for i in range(1, value + 1):
        if (i % 3 == 0 or i % 7 == 0):
            print (i,end=" ")
            res += 1;
  
    

print("Divisors: ") #print divisors
find_divisors(value)

print("\nCount of multiples of 3 or 7 or both: ") #print multiples
countMultiples(value)

print("Adding a change to the file for terminal practice.")

print("Now adding this but from a new branch that was this time. FROM TERMINAL!")
