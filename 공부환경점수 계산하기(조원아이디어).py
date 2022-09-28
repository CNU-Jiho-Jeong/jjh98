import pandas as pd

list = []

for i in range(84): # 카페 카테고리 데이터가 84개가 있다.(1번~84번까지)
    df = pd.read_excel("C:/Users/User/Desktop/%d.xlsx"%(i+1), engine = "openpyxl")
    
    df['LABEL-4']=df['LABEL-3'].str.slice(13,16) 
    df['LABEL-4']=df['LABEL-3'].map(lambda x:x[13:16]) 
    df['LABEL-4']=pd.to_numeric(df['LABEL-4']) 
    a = df['LABEL-4'].sum() # 카테고리 체크 수 총합
    
    df_cond = df[df['LABEL-2'].str.contains('좌석|청결|집중')] 
    b = df_cond.sum() # 각 기준 카테고리 체크 수 총합
    
    list.append(b/a) # 반복문을 돌면서 각 카페의 공부환경 점수를 넣어준다.

cafe = pd.DataFrame() # cafe라는 데이터 프레임 생성
cafe['공부환경점수'] = list # 공부환경점수 열을 만들고, 그 열의 값들을 리스트로 해준다.

cafe # 그럼 끝~