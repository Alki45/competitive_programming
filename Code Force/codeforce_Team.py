n=int(input())
lis=[]
for i in range(n):
    a,b,c=input().split()
    a,b,c=int(a),int(b),int(c)
    lis.append([a,b,c])
for i in lis:
    if(lis[0][0]==i[1]):
        print("YOOOOO")
