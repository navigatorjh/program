# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# 단축키  
# f9 라인단위 실행 
# ctrl+1 : 선택 영역 주석처리 

# 변수 생성 
# 변수 : 값을 저장하기 위한 객체(object)
# 변수 명명 규칙 
# - 대소 구분, 숫자 시작 불가(숫자 포함 가능), 특수기호(!@#) 삽입불가(_dict : _ 사용가능)
# - 예약어(함수명, 함수 내 인자명, 패키지 이름... if, for, while )

vsum = 1
vsum

v1 = 'abcd'
v1

# 모듈(module)
# 패키지(package)
# import 모듈 호출(loading)

round(1.5)
# trunc(1.5) 불가

# 1) 모듈 호출 : 하위 함수 (모듈명.함수명)
import math 
import math as ma  #as (alias : 별칭)

ma.trunc(1.5)

# 2) 모듈 내 함수 직접 호출 : 함수명만 사용 가능 
from math import trunc
trunc(1.5)

# 산술연산 
3+2 
3/1.5
10-2
5*3 

9//2 # 몫
9%2  # 나머지 

3**2 # 거듭제곱
math.pow(3,2) # 3의 제곱

# 파이썬 기본 구조 
# 1. 리스트(list)   [ ]  cf. R : c()
# - 기본 자료 구조 (여러 상수를 동시 전달)
# - 1차원 
# - 서로 다른 데이터 타입 가능

# 1) 리스트 생성 
l1 = [1,2,3,4]
l1
type(l1)
l2 = [1,2,3,'4']
type(l2)

t1 = (1,2,3,4) # tuple : 상수 (변하지 않는 값-> 변경이 불가능한 값)
type(t1)
t2 = 1,2,3,4

# 2) 색인(indexing)
l1
l1[0]
l1[1]
l1[-1]  # reverse indexing
l1[-2]

l1[0:1] # n:m --> n부터 m-1 까지 
l1[0:2]

# 여러 숫자 전달 불가 
l2[0,2] 
l2[[0:2]]

# 3) 수정 
l1[0] = 10
l1

# 4) 연산
l1 + 1 # 리스트와 정수(int) 연산 불가
l1 > 1 # 조건 전달 불가 
# TypeError: can only concatenate list (not "int") to list
# TypeError: '>' not supported between instances of 'list' and 'int'

# 리스트 확장
[1,2,3] + [10,20,30]
# [1, 2, 3, 10, 20, 30]

# 원소(element) 추가 
l1 + [5]
# [10, 2, 3, 4, 5]

l1.append(6)
l1
# [10, 2, 3, 4, 6]

# 문자열 더하고 곱하기 
'a'+'b'
'a'*3

# 튜플(상수) 수정
t1
t1[0] = 10 
# TypeError: 'tuple' object does not support item assignment

# 5) 삭제 
del(l1[0]) #첫번째 원소 삭제 
l1
del(l1)    # 객체 삭제
l1

# 리스트 내 모든 원소 삭제 

l2 = []
l2

# 함수(function)와 메서드 (method)
# 메서드 : 함수의 일부
# 인수 전달 방식이 달라요 

sum([1,2,3]) # 함수 : 인수 전달이 모두 괄호 안에서 진행 

import numpy as np 
a1 = np.array([1,2,3])
a1.sum()
# 메서드 
# - 객체(object)에서 호출 가능한 형태의 함수(값을 객체가 가지고 있어요)

