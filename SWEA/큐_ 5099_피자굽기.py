T = int(input())

for i in range(1, T+1):
    N, M = map(int, input().split())
    cheese = list(map(int, input().split())) # 치즈 리스트 데이터
    stove = [] # 화덕 안에 있는 피자 데이터
    
    for j in range(N):
        stove.append([cheese[j], j + 1]) # 화덕 큐에 치즈 양 데이터와 피자 넘버 같이 저장
    print(stove[0][0]//2)
        
    k = 0
    while len(stove) != 1:
        stove[0][0] = stove[0][0] // 2
        
        if stove[0][0] == 0:
            if N + k < M:
                stove.pop(0)
                # cheese 리스트의 새로운 피자 화덕 안에 넣기
                stove.append([cheese[N+k], N+k+1])
                k += 1
            else:
                stove.pop(0)
                
        # 0이 아닐시 다시 리스트의 뒤에 추가
        else:
            stove.append(stove.pop(0))
            
    print(f'#{i} {stove[0][1]}')
