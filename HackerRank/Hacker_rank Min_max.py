arr=[1,2,3,4,5]
Max=list(sorted(arr))
Max.pop(0)
Min=list(sorted(arr))
Min.pop(-1)
Val=[sum(Min),sum(Max)]
print(Val)
