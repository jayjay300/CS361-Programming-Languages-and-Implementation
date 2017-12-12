import re
list= []
f = open('email.txt', 'rt')
fstr = f.read()
f.close() 
list = re.findall(r'[\"(a-zA-Z\d\"]?[a-zA-Z\d.]*[@][a-zA-z\d.]*[.]+[.com|.co.uk|.es|.be]+', fstr)
## simply cannot get a regex to work that ignores all commas. 
## while researching I found many accepted examples match less than mine do
##email regex seems to be a common problem in computer science.
##here is one provided by GOOGLE EDUCATION [\w.-]+@[\w.-]+
print list