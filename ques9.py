transaction = input("Enter the transactions")

transaction_list = transaction.split(",")

proper_trans_list = []
net_amount = 0

for each in transaction_list:
    each_list = each.split(" ")
    proper_trans_list.append(each_list)
    if each_list[0] == 'D':
        net_amount += int(each_list[1])
    elif each_list[0] == 'W':
        net_amount -= int(each_list[1])

print(net_amount)
