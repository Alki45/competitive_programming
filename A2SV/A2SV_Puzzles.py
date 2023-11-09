n,m=input().split()
n,m=int(n),int(m)
puzzles=list(map(int,input().split()))
puzzles.sort() 
min_difference =max(puzzles)-min(puzzles)
for i in range(m - n + 1):
        difference = puzzles[i + n - 1] - puzzles[i]  
        min_difference = min(min_difference, difference)  
print( min_difference)

