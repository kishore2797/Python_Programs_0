n = 8
for i in range(1,n+1):
    print(("#"*i).rjust(n," "))

for i,j in zip(range(1,n+1),range(n-1,-1,-1)):
    print((" "*j)+("#"*i))
