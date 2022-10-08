import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split())) # map 함수 인자로 int 함수와 리스트를 받음. 그리고 정수화된 리스트를 다시 리스트화

arr2 = sorted(list(set(arr))) # set로 중복제거(서로 다른 좌표의 개수여야 하므로) -> list로 리스트화 -> 정렬된 리스트 복제본을 arr2로. 
dic = {arr2[i] : i for i in range(len(arr2))} 
# 딕셔너리 활용
# arr2의 요소가 key, 요소의 인덱스가 value => 인덱스가 곧  'Xi > Xj를 만족하는 서로 다른 좌표의 개수'.
# 예를 들면, 인덱스가 0이면 가장 작은 수이므로(중복이 제거된), 그 수보다 작은 좌표의 개수는 0, 즉 인덱스이다.
for i in arr:
    print(dic[i], end = ' ') # 이제 딕셔너리에서 순서대로 출력만 하면된다. 
