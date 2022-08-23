import sys
input = sys.stdin.readline

N = int(input()) # 총 회원 수 (문자열 입력 횟수)
li = [] # 입력 받은 문자열을 공백 기준으로 쪼개어 만든 리스트를 받는 리스트
li_1 = [] # 입력 받은 문자열의 정수 부분과 인덱스로 이루어진 리스트를 받는 리스트
li_2 = [] # 회원들 나이가 증가하는 순으로, 나이가 같으면 먼저 가입한 사람이 앞에 오는 순으로 정렬된 리스트들을 가지는 리스트


for i in range(N):
    li.append(input().split()) # 입력 받은 문자열을 정수 부분과 문자부분으로 나누어 리스트를 만들고, 그 리스트를 li에 넣는다.
    li_1.append([int(li[i][0]), i]) # 입력 받은 문자열의 정수부분과 인덱스로 이루어진 리스트를 li_1에 넣는다.
    # 정수부분은 문자열이므로 int를 사용해 정수화해준다. 

result = sorted(li_1, key = lambda x : (x[0], x[1])) 
# 백준 카드 문제에서 쓴 람다를 활용한 정렬 기법을 사용하였다.
# 정수 부분을 오름차순(즉, 회원들 나이가 증가하는 순)으로 / 그리고 그 다음 인덱스를 오름차순(즉, 먼저 가입한 순)으로

for i in range(N): # 다음을 N번 반복한다
    li_2.append([str(result[i][0]), li[result[i][1]][1]]) 
    # result의 정수 부분과, li에서 result의 인덱스에 해당하는 문자열(회원 이름)로 이루어진 리스트를 li_2에 입력한다.
    # join을 써주기 위해 정수 부분은 str 함수를 사용하여 문자열로 만든다.
    print(" ".join(li_2[i])) # 공백 한 칸을 기준으로 정수 부분과 회원 이름을 합쳐준다. 그리고 이를 출력한다.