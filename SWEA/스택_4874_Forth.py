def operator(op, n1, n2):
    return {'+':n1+n2, '-':n1-n2, '*':n1*n2, '/':n1//n2}[op]

def calculator(code):
    stack = []

    for token in code:
        if token == '.':
            if len(stack) == 1:
                return stack.pop()
            # stack에 숫자가 남은 경우
            else:
                return 'error'

        if token.isdigit():
            stack.append(token)
        else:
            try:
                num2, num1 = int(stack.pop()), int(stack.pop())
                stack.append(operator(token, num1, num2))
            # stack에 숫자가 부족한 경우
            except IndexError:
                return 'error'


T = int(input())

for test_case in range(1, T+1):
    # 연산코드 입력
    operation_code = list(input().split())
    ans = calculator(operation_code)

    print('#{} {}'.format(test_case, ans))
