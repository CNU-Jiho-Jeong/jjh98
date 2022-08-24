n=int(input())

arr = list(map(int,input().split())) # map 함수 사용(인자로 int 함수와 리스트가 주어진다.)
arr = list(set(arr))
# set 함수: 중괄호 사용. 하지만 딕셔너리와 다르게 value 만 있음. 순서가 없고, 중복을 허용하지 않는다. 그리고 변할 수 있는 객체이다.
# 여기서는 set 함수를 사용하여 중복을 제거했다. 그리고나서 리스트화.
arr.sort()
#리스트화 하고 순서대로 정렬 -> 이제 순서대로 출력만하면 된다. 
for i in arr:
    print(i,end=' ')