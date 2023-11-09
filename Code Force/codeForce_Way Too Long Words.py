n=int(input())
a=[]
for i in range(n):
    b=input()
    if(len(b)>10):
        leng=str(len(b)-2)
        c=b[0]+leng+b[-1]
        a.append(c)
    else:
        a.append(b)
for i in a:
    print(i)
