# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 14:55:43 2021

@author: PC
"""

# 16. NA 결측치 처리, 중복값 제거 (KING!!! IMPORTANT)

# NA (결측치) 처리 
# 숫자형 NA (float type), 문자형 NA

run my_modules

s1 = Series([1,2,3,np.nan])
s2 = Series(['a','b','c',np.nan])

# 1. NA 수정
s1.mean()   #NaN 값 제외하고 평균값 산출함 >> 2.0
s1.fillna(0) #fillna 사용한 치환 >> 제일 많이 활용함
'''
0    1.0
1    2.0
2    3.0
3    0.0
dtype: float64
'''

s2.replace(np.nan, 'a') #replace
'''
0    a
1    b
2    c
3    a
dtype: object

'''

#조건 색인을 해서 NA 처리 가능
s1. isnull()
s1[s1. isnull()] = 0
s1

# 2. NA 로의 수정

Series(['서울','.','대전','.','대구','.','부산'])
s3 = Series(['서울','.','대전','.','대구','.','부산'])
s3. replace('.',np.nan)

# 3. NA를 이전 값/ 이후 값 수정
s3.fillna(method ='ffill')    #NA를 앞에 있는 값으로 치환
s3.ffill()                    #NA를 앞에 있는 값으로 치환

s4 = s3. replace('.',np.nan)
s4

s4.fillna(method ='ffill')   
s4.ffill()


# 4. NA를 갖는 행, 열 제거
df1 = DataFrame(np.arange(1,17).reshape(4,4), columns=list('ABCD'))
df1

'''
    A   B   C   D
0   1   2   3   4
1   5   6   7   8
2   9  10  11  12
3  13  14  15  16

'''
df1.iloc[0,0] = np.nan
df1.iloc[1,[0,1]] = np.nan
df1.iloc[2,[0,1,2]] = np.nan
df1.iloc[3,:]= np.nan

df1.dropna() # NA 를 하나라도 초함된 행 제거
df1.dropna(how='any')  # NA를 하나라도 포함한 행 제거
df1.dropna(how='all')  # NA모든 값이 NA인 행 제거 (결축치 처리시 반드시 사용할 것)

df1.dropna(thresh=2) # NA 아닌 값이 최소 2개 이상이면 제거하지 않음 (실무에서 유용)
df1.dropna(axis=1, how='any')
# 특정 컬럼이 모두 NA로만 구성되어 있으면 해당 컬럼 제거

df1
df1.dropna(subset=['C'])
# C컬럼에 NA가 있는 행 제거 (실무에서 유용)

#중복값 처리
s1 = Series([1,1,2,3,4,])
s1
s1.unique()   #유일한 값 확인
#  array([1, 2, 3, 4], dtype=int64)

s1.duplicated()   #중복된 값 확인(boolean으로 반환)
s1.drop_duplicates()

'''
0    1
2    2
3    3
4    4
'''

df2 = DataFrame({'A':[1,1,3,4], 'B':[10,10,30,40]})
df2
'''
   A   B
0  1  10
1  1  10
2  3  30
3  4  40
'''

df2.drop_duplicates()
'''
   A   B
0  1  10
2  3  30
3  4  40
'''


df3 = DataFrame({'A':[1,1,3,4],'B':[10,10,30,40], 'c':[100,200,300,400]})
df3
'''
 A   B    c
0  1  10  100
1  1  10  200
2  3  30  300
3  4  40  400
'''
df3.drop_duplicates()

# 모든 컬럼의 값이 일치하는 행 제거
df3.drop_duplicates(subset=['A','B'])
'''
   A   B    c
0  1  10  100
2  3  30  300
3  4  40  400
'''
# A, B 컬럼 값이 일치하는 행 제거

df3.drop_duplicates(subset=)


























