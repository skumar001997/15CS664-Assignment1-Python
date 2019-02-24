binary_numbers = input("Enter the list of 4 digit Binary numbers")
binary_numbers_list = binary_numbers.split(",")
int_binary_no_list = []
divisiblity = []

for each in binary_numbers_list:
    int_binary_no_list.append(int(each))
    number = (int(each[0])*2**3)+(int(each[1])*2**2)+(int(each[2])*2**1)+(int(each[3])*2**0)
    if number%5==0:
        divisiblity.append("Divisible")
    else:
        divisiblity.append("Not Divisible")

print(int_binary_no_list)
print(divisiblity)
