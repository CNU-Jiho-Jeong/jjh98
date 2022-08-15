import sys

N = int(sys.stdin.readline()) 
# input() 함수처럼 입력받는 함수. 단, 반복문으로 여러줄을 입력 받아야 할 때는 input() 대신 sys.stdin.readline()을 사용해서 시간초과를 방지한다.
# 이 문제의 경우 input() 함수를 쓰면 시간초과 에러가 발생한다.

queue = []

for i in range(N):
    cmd = sys.stdin.readline().split() # 공백 기준으로 split()으로 터트려 리스트화 해준다.(사실상 push 때문에 이렇게 해줌) 

    if cmd[0] == "push": # push 명령일 경우
        queue.insert(0, cmd[1]) # queue에도 insert 활용 가능 / cmd[1]은 넣어줄 정수 
        # 큐는 push 작업을 하므로 리스트의 0번째 자리에 새로운 요소가 추가되어야 한다. 그래서 insert로 0번째 자리에 정수를 넣어준다. 
    elif cmd[0] == "pop": #pop 명령일 경우
        if len(queue) != 0: 
            print(queue.pop()) # queue에도 pop 활용 가능 / 큐는 선입선출 구조를 따르므로, 삭제하는 쪽은 삽입하는 쪽과 반대이다. 즉, 큐의 가장 앞에 있는 정수를 '삭제'하는 경우에는 맨 마지막 인덱스가 큐에서 가장 앞에 있는 정수가 되는 것이다. 그래서 pop()을 써주어 맨 마지막 인덱스 요소를 빼내는 것이다.
        else: print(-1)

    elif cmd[0] == "size": # size 명령일 경우
        print(len(queue)) # queue에도 len 사용 가능

    elif cmd[0] == "empty": # empty 명령일 경우
        if len(queue) == 0: 
            print(1)
        else: 
            print(0)

    elif cmd[0] == "front": # front 명령일 경우
        if len(queue) == 0: 
            print(-1)
        else: 
            print(queue[-1]) # 큐의 가장 앞에 있는 정수를 '출력'하는 경우에는, 맨 마지막 인덱스가 큐에서 가장 앞에 있는 정수가 되는 것이다. (큐가 선입선출 구조임을 기억하자)

    elif cmd[0] == "back": # back 명령일 경우
        if len(queue) == 0: 
            print(-1)
        else: 
            print(queue[0]) # 큐의 가장 뒤에 있는 정수를 '출력'하는 경우에는, 맨 처음 인덱스가 큐에서 가장 뒤에 있는 정수가 되는 것이다. (큐가 선입선출 구조임을 기억하자)
    