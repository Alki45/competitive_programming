s="07:05:45PM"
l1=[]
for i in range(len(s)-2):
        l1.append(s[i])

if (s[-2]=="P"):
    time="".join(l1[:2])
    l1[:2]=str(int(time)+12)
    
print ("".join(l1))
