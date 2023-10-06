# a-z alphabets and lowercase || ^[a-z]
# 0-9 numbers || [0-9]
# . , , @ , _ count = 1  || [\._]
# . position should be last 3rd or 4th || [.]\w{rnage to search from}
# ? = not more than 1 
# \w - search 
import re
regex  = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"

email = input("Enter Email\n")

if(re.search(regex, email)):
    print("Valid")
else:
    print("Not Valid")
