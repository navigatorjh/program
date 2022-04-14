# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 15:31:49 2021

@author: student
"""

# 문자열 메서드 
# 문자열 처리와 관련된 메서드 

# 1. 기본 메서드 : 벡터 연산 불가 (매 원소마다 반복 불가)

'abc'.upper()
'a/b/c'.split('/')
'a/b/c'.split('/')[1]

l1=['abc','def']
l2=['a/b/c','d/e/f']


l1.upper() # 불가
l2.split() # 불가 

list(map(lambda x: x.upper(),l1))
# ['ABC', 'DEF']

list(map(lambda x: x.split('/'), l2))

# pandas 메서드 : 벡터화 내장(매 원소마다 반복 가능)
# Series, DataFrame 

# 1) split 

from pandas import Series, DataFrame

l1
# ['abc', 'def']
Series(l1)
# 0    abc
# 1    def
# dtype: object

s1 = Series(l1)

l2
# ['a/b/c', 'd/e/f']
Series(l2)
# 0    a/b/c
# 1    d/e/f
# dtype: object
s2=Series(l2)

s2.str.split('/')
# 0    [a, b, c]
# 1    [d, e, f]
# dtype: object

# 2) 대소 치환 
s1
# 0    abc
# 1    def
# dtype: object

s1.str.upper()
s1.str.lower()
s1.str.title()

# 3) replace
s1.str.replace('a','A')
# 0    Abc
# 1    def
# dtype: object

s1.str.replace('a', '') # very ^ 100 
# 0     bc
# 1    def
# dtype: object

# 예제 - 천단위 구분기호 처리 

s3 = Series(['1,200','3,000','4,000'])
s3.sum()
# 천 단위 구분기호 때문에 문자로 입력된 값이라 문자열 결합으로 인식됨 
# 구분기호 문제네? 문자로 인식되어 있네? 더해줘야 되네
 
s3.str.replace(',','').astype('int').sum()

s3 = Series(['1,200','3,000','4,000'])
s3 = s3.str.replace(',','')
sum(list(map(lambda x: int(x), s3)))

# 4) 패턴 확인 : startswith, endswith, contains 
s1
# 0    abc
# 1    def
# dtype: object
s1.str.startswith('a')
# 0     True
# 1    False
# dtype: bool
s1[s1.str.startswith('a')]  # s1 각 원소에서 'a'로 시작하는 원소 추출 
# 0    abc
# dtype: object
s1[s1.str.endswith('c')] # s1 각 원소에서 'c'로 끝나는 원소 추출 
s1[s1.str.contains('e')] # s1 각 원소에서 'e'를 포함하는 원소 추출

# 문자열 크기 len()
s1.str.len()
# 0    3
# 1    3
# dtype: int64

# count 포함 개수 
Series(['aabbbb','abcdadd']).str.count('a')
# 0    2
# 1    2
# dtype: int64

# 제거 함수 (공백, 문자)
Series(['      cd     ','        df       '])
Series(['      cd     ','        df       ']).str.strip()
Series(['      cd     ','        df       ']).str.strip().str.len()

s1
# 0    abc
# 1    def
# dtype: object

s1.str.strip('a') # 문자열 제거 
Series(['aaabaaabcd','abcdaa']).str.strip('a')
# 문자열 제거(중간값 삭제 불가)
# 0    baaabcd
# 1        bcd
# dtype: object
Series(['aaabaaabcd','abcdaa']).str.replace('a','')
# 문자열 제거(중간값 삭제 가능)

# find(위치값 return)
s3 = Series(['abc@drwill.kr','abcdef@drwill.com'])
s3.str.find('@')

# 문자열 색인(추출)
'abcde'[0:3]  # 문자열 색인
s3
s3[0:3]     # Series에서 1번째, 2번째, 3번째 원소 추출 
s3.str[0:3] # Series에서 각 원소마다 1번째, 2번째, 3번째 문자열 추출 

# 이메일 아이디 추출 
s4 = Series(['drwill@naver.com','zzuyu@drwill.kr'])
s4
# 0    drwill@naver.com
# 1     zzuyu@drwill.kr
# dtype: object

vno=s4.str.find('@')
vno
s4.str[0:5]
list(map(lambda x, y : x[0:y], s4, vno))
# ['drwill', 'zzuyu']
# y 추출 범위

s4 = Series(['drwill@naver.com', 'zzuyu@drwill.kr'])
s4.map(lambda x : x[:x.find('@')])
s4.str.find('@')


s4.str[0:s4.str.find('@')]
s4.str[0:s4.str.find('@')[0]]
s4.str[0:s4.str.find('@')[1]]
s4.str[0:s4.str.find('@')[1]][0]
s4.str[0:s4.str.find('@')[1]][1]

# pad : 문자열 삽입 
s1.str.pad(5,       # 총 자리수 
           'left',  # 삽입 방향
           '!')     # 삽입 글자

s1
# 0    abc
# 1    def
# dtype: object

s1.str.pad(5, 'right', '^')
# 0    !!abc
# 1    !!def
# dtype: objec

s1.str.pad?

s5 = Series(["I love you","You know"])
s5
s5.str.pad(20, 'right', '^')

# 문자열 결합
'a' + 'b'
'a'*3

s5= Series(['abc','def','123'])
s5.str.cat()
s5.str.cat(sep=',')
s5.str.cat(sep='/')

s6 = Series([['a','b','c'],['d','e','f']])
s6
s6.str.join(sep='')      # Series 내 각 원소 내부의 문자열을 결합 (공백)
s6.str.join(sep=',')     # Series 내 각 원소 내부의 문자열을 결합 (,)


Series(['a','b','c'],index = ['drwill','zzuyu','hyory'])
Series(['a','b','c'],['drwill','zzuyu','hyory'])
Series?
