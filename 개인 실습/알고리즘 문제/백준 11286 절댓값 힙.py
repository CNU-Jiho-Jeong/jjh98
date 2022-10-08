import sys
import heapq

n = int(input())
q1 = [] # 음수를 넣을 큐
q2 = [] # 양수를 넣을 큐

for i in range(n):
    a = int(sys.stdin.readline())
    if a < 0:
        heapq.heappush(q1, -a) # 절대값이 가장 작은 값을 출력할 예정이므로, 즉 절대값이 기준이 되므로, 음수를 양수로 바꾸어 넣어준다.
    elif a > 0:
        heapq.heappush(q2, a) # 양수이므로 그대로 넣어준다.
    else:
        if not q1: # q1이 비어있는 경우
            if not q2: # q1, q2 모두 비어있는 경우
                print(0) # 배열이 아예 비어있으므로 0 출력
            else: # q1만 비어있는 경우
                print(heapq.heappop(q2)) # heapq.heappop : heap에서 가장 작은 원소를 pop & 리턴 / q1이 비어있으므로 q2에서 가장 작은 원소를 pop&리턴
        elif not q2: # q2만 비어있는 경우
            print(-heapq.heappop(q1)) # q2가 비어있으므로 q1에서 가장 작은 워소를 pop&리턴. 리턴시 -를 붙인다. (q1에는 절댓값이 입력된 상태이다. 문제에서 요구하는 것은 절댓값 출력이 아닌 원래의 수 출력이다.)
        else: # q1, q2 모두 차있는 경우
            tmp1 = -heapq.heappop(q1) # q1에서 가장 작은 원소를 pop&리턴. 리턴시 -를 붙인다.
            tmp2 = heapq.heappop(q2) # q2에서 가장 작은 원소를 pop&리턴

            if abs(tmp1) > abs(tmp2): # 절대값 비교. 
                print(tmp2) # 작은 절대값 출력
                heapq.heappush(q1, -tmp1) # q1의 원소는 제거할 필요가 없으므로 다시 넣어준다. 

            else:
                print(tmp1) # 작은 절대값 혹은 동일한 절대값 출력
                heapq.heappush(q2, tmp2) # q2의 원소는 제거할 필요가 없으므로 다시 넣어준다. 
