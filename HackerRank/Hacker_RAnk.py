n=[1,7,2,4]
k=3
count=0
new=[]
for i in range(len(n)):
    for j in range(i+1,len(n)):
        if((n[i]+n[j])%k!=0):
            count+=1
            new.append([n[i],n[j]])
print(count,new)
