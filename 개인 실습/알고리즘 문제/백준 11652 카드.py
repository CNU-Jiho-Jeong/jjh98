import sys
input = sys.stdin.readline # sys.stdin.readline 을 번거롭게 계속 써주는 것을 피하기 위해 input 변수를 사용하였다. 

n = int(input()) # 일반적인 input() 함수가 아니라 sys.stdin.readline()이다. input 변수를 sys.stdin.readline()로 지정해주었기 때문이다. 
card_dic = {} # 이 문제에서 딕셔너리를 활용했다. 딕셔너리의 장점은 key와 value를 같이 묶어서 활용할 수 있다는 것이다.

for i in range(n) :
    card = int(input()) # 카드의 정수 값을 입력받는다. 
    if card in card_dic :
        card_dic[card] += 1 # 딕셔너리에 한 번이상은 집어넣은 카드의 정수값은 value만 1 올려준다.
    else :
        card_dic[card] = 1 # 카드의 정수값을 key로 설정한 후, 정수값 개수를 value로 설정하여 딕셔너리에 집어넣는다.

result = sorted(card_dic.items(),key = lambda x : (-x[1],x[0])) 
# sorted(정렬할 데이터, key 파라미터)
# key 파라미터: 어떤 것을 기준으로 정렬할 것인가?에 대한 기준. 즉, 기준을 정해 줄 수 있는 파라미터
# lambda 인자(매개변수):표현식(인자를 이용한 동작) : 일반함수를 가볍게 만든 함수라고 생각하자. ex) lambda x:x*2
# 여기서는 lambda가 key 파라미터를 위해 쓰였다. 즉, 기준을 설정하기 위해 쓰였는데, 그 기준을 value(x[1])는 내림차순(-)으로 , key(x[0])는 오름차순(+)으로 설정한 것이다. 그리고 이를 result에 담는다.
print(result[0][0])
# result[0][0] -> 첫번째 [0]는 첫번째 item을 나타내는 것이고, 두번째 [0]는 첫번째 item의 첫번째 요소, 즉 정수 값이다. 그리고 이는 가장 많은 개수인 정수 값 중 가장 작은 정수이다.
