s,t,a,b=input().split()
s,t,a,b=int(s),int(t),int(a),int(b)
n=max(s,t)*max(a,b)
S_T=s+t
A_B=a+b
ST=[]
AB=[]
for i in range(n):
    if(S_T==A_B):
        output="YES"
        break
    else:
        S_T+=t
        A_B+=b
        ST.append(S_T)
        AB.append(A_B)
if (ST[-1]==AB[-1] and len(ST)==len(AB)):
    ouput="YES"
print(output)

