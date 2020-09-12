T = int(input())

for i in range(1, T+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    for j in range(M):
        a = lst.pop(0)
        lst.append(a)
    print (f'#{i} {lst[0]}')
