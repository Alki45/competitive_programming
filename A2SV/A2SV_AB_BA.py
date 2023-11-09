import re
n=int(input())
coin_lis=[]
for i in range(n):
    b=input()
    lis=re.split(r'AB|BA', b)
    coin_lis.append(lis.count(""))
for i in coin_lis:
    print(i)
