import sys
input = sys.stdin.readline

def sum_num(s): # 모든 자릿수의 합(숫자만)을 구하는 함수
    res = 0 # 초기값 0
    for i in s: # 문자열 구성요소들 중
        if i.isdigit(): 
        # isdigit() 함수 : 단일 글자가 숫자 모양으로 생겼으면 무조건 숫자로 판별.
        # 구성요소가 숫자 모양으로 생겼으면 (즉 True이면)
            res += int(i) # 해당 요소 정수화 + res에 더해준다. => 반복하여 모든 자릿수의 합을 구함 
    return res
    
n = int(input()) # 기타의 갯수
serial = [input().rstrip() for _ in range(n)] 
# 기타의 갯수만큼 시리얼 번호들을 리스트에 넣어준다. 
# 문자열의 오르쪽 공백들을 제거해준다. 
# 인덱스가 따로 필요하지 않으므로 i대신 간단히 _를 썼다. 

serial.sort(key = lambda x:(len(x), sum_num(x), x)) #람다를 써서 정렬해준다. 1순위는 문자열의 길이가 짧은 순, 2순위는 모든 자릿수의 합(숫자만)이 작은 순, 마지막으로 사전 순이다. 사전 순은 따로 지정할 필요없다. sort가 알아서 해준다. 


for s in serial:
    print(s) # 기준에 맞게 정렬된 리스트의 요소들을 차례차례 출력한다. 
