x = int(input())
num = []
for c in range(x):
    n = int(input())
    array = list(map(int, input().split()))
    remainders = set()
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                remainder = (array[i] + array[j] + array[k]) % 10
                remainders.add(remainder)
                break
    if 3 in remainders:
        num.append("YES")
    else:
        num.append("NO")
for i in num:
    print(i)
