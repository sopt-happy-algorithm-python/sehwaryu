import itertools

N, M = map(int, input().split())
num_list = [i for i in range(1, N+1)]
    
for num in itertools.combinations_with_replacement(num_list, M):
    for i in num:
        print(i, end = ' ')
    print(end = '\n')
