#Don't know what the formula is for q=(sqrt(2*c*d))/h and what are the inputs

c = int(input("Enter the value of C"))
d = int(input("Enter the value of D"))
h = int(input("Enter the value of H"))

import math

q = math.sqrt(2*c*d)/h
print("Value of Q as per formula is: "+str(q))