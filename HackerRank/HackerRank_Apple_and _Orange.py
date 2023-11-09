s,t=input().split()
s,t=int(s),int(t)
a,b=input().split()
a,b=int(a),int(b)
m,n=input().split()
m,n=int(m),int(n)
ma=list(map(int,input().split()))
nb=list(map(int,input().split()))
New_A=[]
New_B=[]
for i in ma:
    New_A.append(i+a)
for i in nb:
    New_B.append(i+b)
count_A=0
count_B=0

for i in New_A:
    if(i>=s and i<=t):
        count_A+=1
    else:
        continue
for i in New_B:
    if(i>=s and i<=t):
        count_B+=1
    else:
        continue
print(count_A)
print(count_B)
