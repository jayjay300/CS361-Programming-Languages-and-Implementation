def set_first_elem_to_zero(l):
	l[0] = 0
	return l
a = ["green","red","blue"]
print "original a"
print a
l = [1, 1, 2, 3]
b = a
b[1] = "black"
print "contents of list a after b is changed: "
print a
c = a[:]
c[2] = "orange"
print "contents of list a after c is changed: "
print a
print "here's the original l"
print l
print "here's the output of the function"
print(set_first_elem_to_zero(l))
print "here's l outputted by itself after the function call"
print l