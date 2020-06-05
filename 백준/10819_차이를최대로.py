from itertools import permutations

n = int(input())
lst = list(map(int, input().split(' ')))
arr = permutations(lst)
ans = 0

for i in arr:
    sums = 0
    for j in range(n-1):
        sums += abs(i[j]-i[j+1])
    ans = max(ans, sums)
print(ans)
