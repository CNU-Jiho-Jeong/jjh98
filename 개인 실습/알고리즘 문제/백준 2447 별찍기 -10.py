# 프랙탈: 자기 유사성을 갖는 기하학적 구조
# 이 문제는 부분의 구조를 가지고 계속 반복하여 전체의 구조를 만드는 프렉탈 구조 문제이다. 
# '***'를 하나의 요소로 이해하자

def draw_stars(n):
  if n==1: # 재귀적인 방법으로 n을 1까지 도달하게 한 다음 ['*']를 리턴해준다. 
    return ['*']

  Stars=draw_stars(n//3)
  L=[]

  for star in Stars:
    L.append(star*3)
  for star in Stars:
    L.append(star+' '*(n//3)+star)
  for star in Stars:
    L.append(star*3)
# n이 3일 때, 총 3개의 for 문을 ['*']로 돌렸을 때, L == ['***','* *', '***']
# n이 9일 때, 총 3개의 for 문을 ['*']로 돌렸을 때, 
'''
L == [['*********',

       '* ** ** *',

       '*********',

       '***   ***',

       '* *   * *',

       '***   ***',

       '*********',

       '* ** ** *',

       '*********']
'''
  return L

N=int(input())
print('\n'.join(draw_stars(N))) # join으로 리스트의 요소를 붙인다. 이때 \n(줄바꿈)을 써서 붙여주면 된다.  
