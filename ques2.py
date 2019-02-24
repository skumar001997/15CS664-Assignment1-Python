def sqr(n):
    return n*n


n = int(input("Enter the number:"))
a = []
for i in range(1,n+1):
    a.append(str(i)+":"+str(sqr(i)))
print(a)