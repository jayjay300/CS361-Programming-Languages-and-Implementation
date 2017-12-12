

def rec(n,l,prod):
	if(l == 0):
		prod = prod * n[0]
		return prod
	else:
		prod = prod * n[l]
		return rec(n,l-1,prod)

	
	
def iter(n):
	prod = 1
	l = len(n)
	for x in range(0,l):
		prod=prod * n[x]
	return prod

n = [5,7,9,6]
l =len(n)-1
prod = 1
print ("iteration")
print(iter(n))
print("recursion")
print(rec(n,l,prod))