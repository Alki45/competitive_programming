n=int(input())
out=[]
for i in range(n):
    a,b=input().split()
    a,b=int(a),int(b)
    list1=list(map(int,input().split()))
    if(b in list1):
        out.append("YES")
    else:
        out.append("NO")
for i in out:
    print(i)
