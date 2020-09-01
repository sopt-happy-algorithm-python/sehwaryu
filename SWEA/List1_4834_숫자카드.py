# 4834: 숫자카드

# [입력]

# 첫 줄에 테스트 케이스 개수 T가 주어진다.  ( 1 ≤ T ≤ 50 )
# 다음 줄부터 테스트케이스의 첫 줄에 카드 장수 N이 주어진다. ( 5 ≤ N ≤ 100 )
# 다음 줄에 N개의 숫자 ai가 여백없이 주어진다. (0으로 시작할 수도 있다.)  ( 0 ≤ ai ≤ 9 ) 

# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 가장 많은 카드의 숫자와 장 수를 차례로 출력한다.

T = int(input())
for j in range(1, T+1):
    num = int(input())
    N = str(input())
    cnt = []
    for j in range(10):
        cnt.append(0)

    for i in range(num):
        cnt[int(N[i])] += 1

    max = -1
    for i in range(10):
        if cnt[i] >= max:
            ans = i
            max = cnt[i]
    print("#%d %d %d" %(j, ans, cnt[ans]))
                

/**각 번호의 개수를 저장할 리스트를 만든후에 나온 카드의 번호에 해당하는 인덱스에 접근하여 갯수를 하나씩 늘린뒤에
뒤부터 검사하여 제일 많이나온 카드를 확인.**/

length = int(input())
for l in range(1, length+1):
    size = input()
    temp = list(map(int, list(input())))
    #각 숫자 카운팅하는 변수
    numcheck = [0]*10
    #각 숫자 카운팅하기
    for t in temp:  
        numcheck[t] += 1
    #숫자와 횟수
    index = 0
    maxnum = 0
    #반복문
    for i in range(9, -1, -1):
        if numcheck[i] > maxnum :
            maxnum = numcheck[i]
            index = i
    #출력
    print("#{} {} {}".format(l, index, maxnum))
