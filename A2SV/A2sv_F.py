x = int(input())
num = []
for c in range(x):
    n = int(input())
    array = list(map(int, input().split()))
    found = False
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if (array[i] + array[j] + array[k]) % 10 == 3:
                    found = True
                    break
            if found:
                break
        if found:
            break
    if found:
        num.append("YES")
    else:
        num.append("NO")
for i in num:
    print(i)
