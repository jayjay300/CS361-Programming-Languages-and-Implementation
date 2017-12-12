list = ["welcome","to","late","night","homework","theater"]

def readlist(list):
	counter = mylen(list)
	for x in range(0,counter):
		print list[x]
		x = x+1



def reverse(list):
	counter = mylen(list)
	counter = counter -1;
	while(counter>=0):
		print list[counter]
		counter = counter-1
# could've just used reverse function but oh well


def mylen(list):
	counter=0
	for x,value in enumerate(list):
			counter = counter+1
	return counter
	
	
	
	
readlist(list)
print "REVERSE REVERSE "
reverse(list)
print " "
print mylen(list)