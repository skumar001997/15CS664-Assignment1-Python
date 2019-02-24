a = []
for i in range(1000,3001):
    st = str(i)
    if int(st[0]) % 2 == 0 and int(st[1]) % 2 == 0 and int(st[2]) % 2 == 0 and int(st[3]) % 2 == 0:
        a.append(int(st))
print(a)