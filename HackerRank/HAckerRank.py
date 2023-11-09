icons=[4,3,2,1]
nn=[]
for i in icons:
    minn=min(icons)
    if(minn==icons[-1]):
        nn.append(minn)
        icons.pop(-1)
        icons.pop(-1)
print(nn,icons)

