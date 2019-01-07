age = int(raw_input("Enter age : "))

if age>=18 :
    print "IN if"
    print "You can vote !!\n"

#indented statements after if count as 1 block of code

elif age >= 21:
    print "You can drink\n"

else :
    print "Still too small\n"
    
print "OUT if\n"
#out of indentation -> diff block

gender = raw_input("Enter gender M/F : ")

if (age>=18 and (gender=='M' or gender=='m')) :
    print "know your beer well\n"

else :
	print "Aww.. My sweet summer child\n"


name = raw_input("Enter name : ")

if (name == "amey"):
	print "He's the owner\n"
