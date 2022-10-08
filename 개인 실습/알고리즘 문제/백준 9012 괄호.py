import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    stack = [] 
    a=input()
    for j in a:
        if j == '(':
            stack.append(j) # j가 ( 라면 스택에 넣어준다
        elif j == ')':
            if stack: # j가 ) 일 때 스택 안에 문자가 존재한다면,
                stack.pop() # 스택 맨 뒤의 요소를 빼준다. 
            else:  # 스택이 비어있으면
                print("NO") # )에 대응되는 (가 없다는 소리이므로 "NO"를 출력한다. 
                break # 반복문 탈출
    else: # for 문에서 한번도 break가 난 적이 없다면 else문을 실행한다.
        if not stack: # break으로 끊기지 않고 스무스하게 스택이 비게 되면 정상적인 괄호인 거라 판별할 수 있다.
            print("YES")
        else: 
        # 요게 중요한데, break가 안 걸렸다 하더라도 스택에 괄호가 들어있을 수 있다. 하지만 이 경우는 for 문을 다 돌았음에도 불구하고, 즉 입력한 문자열에 존재하는 모든 )와 대응되는 (를 전부 제거했음에도 불구하고 스택이 비지 않은 것이므로 입력한 문자열이 정상적인 괄호가 아닌 것이다.
            print("NO")
 
    # for - else 문: 보통 else 는 if와 많이 쓰지만 파이썬에서는 for문과 쓰이기도 한다. 이 경우, for문이 break 등으로 끊기지 않고 끝까지 수행되었을 때 else문을 실행한다. 
