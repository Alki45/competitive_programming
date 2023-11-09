n=int(input())
les=[]
output="NO"
for i in range(n):
    les.append(i)
for i in range(len(les)):
    if(i%2==0):
        for j in range(i,n,1):
            if(les[i]+les[j]==n):
                if((les[i]%2==0) and (les[j]%2==0)):
                    output="YES"
                    break
                else:
                    output="NO"
                    break
print(output)
