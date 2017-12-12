def is_prime(n):
	prime = False
	if(n == 1):
		prime = False
		return prime;
	elif(n == 2 or n == 3):
		prime = True
		return prime
	counter=1
	primeplus = 6*counter +1
	primeminus = 6*counter -1

	while primeminus <= n:
		if(primeplus==n or primeminus==n):
			prime = True
			return prime
		counter = counter+1
		primeplus = 6*counter +1
		primeminus = 6*counter -1
	if(prime == False):
		return prime
	
	
		
def prime_upto(n):
	counter=1
	primeplus = 6*counter +1
	primeminus = 6*counter -1
	primeupto = []
	if(n >= 2):
		primeupto.append(2)
		
	if(n >= 3):
		primeupto.append(3)
	while(primeminus <= n):
		primeupto.append(primeminus)
		if(primeplus<= n):
			primeupto.append(primeplus)
		counter = counter + 1
		primeplus = 6*counter +1
		primeminus = 6*counter -1
	return primeupto
	
def prime_first(n):
	counter = 1
	primes=0
	primefirst = []
	first = True
	primeminus = 6*counter -1
	primeplus = 6*counter +1
	while(primes<n):
		primeminus = 6*counter -1
		primeplus = 6*counter +1
		if(first == True):
			if(n>=2):
				primefirst.append(2)
				primes = primes + 1
			if(n>=3):
				primefirst.append(3)
				primes = primes + 1
			first= False
		if(primes < n):
			primefirst.append(primeminus)
			primes = primes + 1
			if(primes < n):
				primefirst.append(primeplus)
				primes = primes+1
				counter = counter+1
				
	return primefirst
	
n = input("Enter a value to test: ")
print "Is n prime?"
print(is_prime(n))
print "prime up to n:"
print(prime_upto(n))
print "first n primes: "
print(prime_first(n))