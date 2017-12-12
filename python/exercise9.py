def extractsub(listoflists):
	finallist = []
	length = len(listoflists)
	for x in range(0,length):
		length2 = len(listoflists[x])
		sublist = listoflists[x]
		for y in range(0,length2):
			finallist.append(sublist[y])
			y=y+1
		x = x+1
	return finallist		
			
		
listoflists = [[1,3],[3,6]]
print(extractsub(listoflists))