
string = input("Enter the string")
num = 0
alpha = 0
sym = 0
space = 0

for i in range(len(string)):
    if string[i].isalpha():
        alpha += 1
    elif string[i].isdigit():
        num += 1
    elif string[i].isspace():
        space += 1
    else:
        sym += 1

print("Alphabet: "+str(alpha))
print("Digit: "+str(num))
print("Symbols: "+str(sym))