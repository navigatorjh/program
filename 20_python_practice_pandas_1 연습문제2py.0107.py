# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 15:13:41 2022

@author: PC
"""

# 단축키
#f9 라인단위 실행
# ctrl+1: 선택 영역 주석처리

run my_modules

#card.csv 파일 읽기

import pandas as pd

pd.read_csv('./data/card.csv', encoding='cp949')
card=pd.read_csv('./data/card.csv',encoding='cp949')
#NUM을 인덱스로 사용
card=card.set_index('NUM')

#문제) 일자별 총 지출 금액을 구해서, 마지막 컬럼에 추가
# (천 단위 구분기호 제거 후 숫자 컬럼 변경하시오)

# 행/세, 열/가 (행은 세로방향, 열은 가로방향)
card.sum()
card.sum(axis=0) # default : axis=0 세로방향 
card.sum(axis=1)
# axis=1 :  서로 다른 열끼리 (가로방향) sum() 합해라 
# 문자 타입이라 문자열 결합 
'hi'+'drwill'

#',' 문자 제거 >>> 숫자 변경
# 천단위 구분기호 제거 >> 숫자 컬럼 변경
'19,400'.replace(',','') #'19400'
int('19,400'.replace(',',''))

'19,400'.replace(',','').astype('int')
# 문자열에 사용불가(array, Series, DataFrame 사용가능)

f1 = lambda x : int(x.replace(',',""))
card=card.applymap(f1)

# applymap : 2차원 데이터 셋(DataFrame)에 함수 적용 위해 사용

# int('19,400'.replace(',',''))
# 이 행위(형변환 함수)를 전체에 적용할 대 사용해요

# 일자별 총합 (새로운 열 생성)
card['총합'] = card.sum(axis=1)
card

#식료품 컬럼에만 적용

card_new=pd.read_csv('./data/card.csv', encoding='cp949')
card_new=card_new.set_index('NUM')

# -식료품 컬럼에만 적용
f2 = lambda x: int(x.replace(",",""))
card['식료품'].applymap(f2)
# 1차원 데이터 셋(Series)  에 적용불가
card_new['식료품'] = card_new['식료품'].map(f2)

card_new['의복'] = card_new['의복'].str.replace[",",""]
# 여전히 dtype 은 object (객체)

card_new['의복'] = card_new['의복'].str.replace[",",""].astype('int')
#일괄적으로 적용하려면  astype() 사용할 것

card_new['책값'].replace(",","")
# 값 치환 메서드(특정 값과 정확히 일치하는 값을 변경하거나 삭제)
# ','와 완전히 일치하는 값을 변경 또는 삭제

card_new['책값'].replace("28,000","") # 정확히 일치하는값 삭제

# 2) 일자별로 각 품목별 지출 비율을 출력핫에ㅛ(%로 출력하세요)
pd.read_csv('./data/card.csv', encoding= '949')
card = card.set_index('NUM')

f1 = lambda x : int(x.replace(",",""))
card = card.applymap(f1)

#첫번째 행에 대해 확인
card.iloc[0,:]
card.iloc[0,:].sum # 첫째 날 지출 총 합

(card.iloc[0,:] / card.iloc[0,:].sum())*100



#apply  메서드 이용, 각 일자별로 적용 (썩은 물 전용)
f2 = lambda x: (x / x.sum())*100
card.apply(f2.axis=1) #가로방향

# 결과 해석
# - 의복비가 지출이 심함 (일개별 출력 지출 중 의복비 비중이 50% 이상)
# insight (통찰) 의복비 비중을 줄일 필요성이 있음(주관적 의견)

#형 (데이터 타입) 변환 : 함수, astype 메서드
# 적용함수 : map 함수, map 메서드, apply 메서트, appltmap 메서드
#치환함수 : 문자열 메서드, 벡터화 내장된 문자열 메서드, 값 치환 메서드
#색인
#컬럼 추가, 컬럼 내용 변경

#문제) 각 구매 마다 포인트 확인하고, POINT 컬럼생성
# POINT 는 주문금액 5000 미만 1%, 5만 이상 10만 미만 2%, 10만 이상 3% 
# 문제 풀이 포인트 : 조건에 다른 치환 혹은 연산
 
df1 = pd.read_csv("./data/ex_test.csv", encoding'cp949')

if df1["주문금액"] < 50000:
    df1['주문금액']*0.01
    
# if 문은 여러 개의 T/F (boolean) 연산 불가

for i in df1['주문금액'] :
    if i < 50000:
        i * 0.01
    elif i < 100000:
        i*0.02
    else:
        i*0.03
    
# 아무 결과 값 없음

# sol1) for + if    

result = []    

for i in df1['주문금액'] :
    if i < 50000:
        result.append(i*0.01)
    elif i < 100000:
        result.append(i*0.02)        
    else:
        result.append(i*0.03)
        
#print(result)
print(np.round(result,2))        
    
df1['point'] = np. round(result,2)
df1['point']    
df1    
    
# sol2) np.where(벡터 연산 가능한 조건 연산 함수)
# sql에서 copy 함

# sql : select * from db_name where 조건절
# where(조건, 참 리턴, 거짓 리턴)

#np.where(df1['주문금액<50000, df1['주문금액' * 0.01, df1'주문금액']*0.02)    
np.where(df1['주문금액']<50000, #첫번째 조건
         df1['주문금액']<*0.01, #첫번째 조건이 참이면 연산하세요.
         np.where(df1['주문금액']<100000,  #두번째 조건
                  df1['주문금액']<*0.02,   #두번째 조건이 참이면 연산
                  df1['주문금액']<*0.03,))  #두번째 조건이 거짓이면 연산

# 첫번째 조건이 거짓이면, 새로운 조건 추가
    
df1['point2'] = np.where(df1['주문금액']<50000, #첫번째 조건
         df1['주문금액']<*0.01, #첫번째 조건이 참이면 연산하세요.
         np.where(df1['주문금액']<100000,  #두번째 조건
                  df1['주문금액']<*0.02,   #두번째 조건이 참이면 연산
                  df1['주문금액']<*0.03,))  #두번째 조건이 거짓이면 연산    
    
# 2. 회원번호별 총 주문금액과 총 포인트 금액 확인
df1.groupby('회원번호')[['주문금액','point']].sum()
   
# [ 연습문제 - Y 값을 서로 다른 숫자로 변경] 
# 출제의도 : 조건에 다른 치환
# 출제의도 : 조건에 다른 치환

DataFrame({'Y':['a','a','b','b','c','a','a','b'],
           'X1' : 1,2,4,4,6,3,5,4],
           'X2' : 10,30,43,34,43,43,94,32})  
   
df2

#하나 식 사용자가 치환
df['Y'].replace({'a':0,'b':1, 'c':2})

# 자동 변환 함수
from sklearn.preprocessing import LabelEncoder

m_lb=LabelEncoder() 
m_lb.fit_transform(df2['Y'])   
#   
    
# [연습문제 - 조건에 따른 값의 수정]
# df2에서 x1이 5이상일 경우, X1 평균으로 수정(최빈값, 중앙값, 최소값)   
    
df2['X1'][df2]['X1']>=5]   
    
   
    
   
df2.iloc[df2['X1']>=5, 'X1'] #추천

df2
m1 = df2['X1'].mean()
m2 = df2['X1'].median()
m3 = df2['X1'].mode() #c최빈값
m4 = df2['X1'].mode()[0]
m5 = df2['X1'].min() #최소값   
m6 = df2['X1'].max()    
   
    
import statistics as stat
stat.mode(df2['X1']) # 4: 하나의 상수로 리턴해 줌

df2   
df2.loc[df[;X1]>=5, 'X1']
df2.loc[df[;X1]>=5, 'X1'] =m3 #최빈값ㅇ로 치환하겠다는 의미
# NA 로 수정이 됨(문제 발생)

df2.loc[df[;X1]>=5, 'X1'] =m4
df2











    
   