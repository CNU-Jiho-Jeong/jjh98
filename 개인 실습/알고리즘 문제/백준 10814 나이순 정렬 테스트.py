import sys
input = sys.stdin.readline

N = int(input())
li = []
li_1 = []
li_2 = []


for i in range(N):
    li.append(input().split())
    li_1.append([int(li[i][0]), i])

result = sorted(li_1, key = lambda x : (x[0], x[1]))

for i in range(N):
    li_2.append([str(result[i][0]), li[result[i][1]][1]])
    print(" ".join(li_2[i]))
