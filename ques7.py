string = input("Enter the string: ")
upper = 0
lower = 0

for i in range(len(string)):
    if string[i].isupper():
        upper += 1
    elif string[i].islower():
        lower += 1

print("Upper: "+str(upper))
print("Lower: "+str(lower))