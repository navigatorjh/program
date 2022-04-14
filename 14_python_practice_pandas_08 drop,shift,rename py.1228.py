# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 13:14:50 2021

@author: PC
"""

# 14. drop, shift, rename

# 기타 메소드

import numpy as np
import pandas as pd
from pandas import Series, DataFrame

run my_modules

#1. drop
# - 특정 행, 컬럼 제거
# - 이름 전달

emp=pd.read_csv("./data/emp.csv")
emp
'''
   empno  ename  deptno   sal
0      1  smith      10  4000
1      2  allen      10  4500
2      3   ford      20  4300
3      4  grace      10  4200
4      5  scott      30  4100
5      6   king      20  4000
'''
# scott 퇴사
emp.loc[emp['ename'] == 'scott' ] #scott 관련된 record
emp['ename'] == 'scott' #조건문

emp.loc[emp['ename'] == 'scott',:]
emp.loc[~(emp['ename'] == 'scott'),:] 

emp.drop?

emp
emp.drop(4, axis=0) # 행기준, 4번째 idx 제외

#[예제]
# emp 데이터셋에서 sal 컬럼 제외 (iloc)

emp.drop('sal', axis=1)
emp.iloc[:,0:3]
emp.iloc[:,0:-1]

emp.loc[:, "empno":"deptno"]

emp.drop(['ename','deptno'], axis=1)

# shift
# - 행 또는 열을 이동
# - 전일자 대비 증감율

emp['sal']

'''
0    4000
1    4500
2    4300
3    4200
4    4100
5    4000
Name: sal, dtype: int64
'''

emp['sal'].shift() # default :axis= 0

'''
0       NaN
1    4000.0
2    4500.0
3    4300.0
4    4200.0
5    4100.0
Name: sal, dtype: float64
'''
# [예제 - 다음 데이터 프레임에서 전일자 대비 증감율 출력]
s1 = Series([3000,3500,4200,2800,3600], 
       index=['2021/01/01','2021/01/02','2021/01/03','2021/01/04','2021/01/05'])
s1

'''
2021/01/01    3000
2021/01/02    3500
2021/01/03    4200
2021/01/04    2800
2021/01/05    3600
dtype: int64
'''

#1월 2일 증감율 >> (3500-3000)/3000
s1.shift()

'''
2021/01/01       NaN
2021/01/02    3000.0
2021/01/03    3500.0
2021/01/04    4200.0
2021/01/05    2800.0
dtype: float64
'''

(s1-s1.shift())/s1.shift() * 100

'''
2021/01/01          NaN
2021/01/02    16.666667
2021/01/03    20.000000
2021/01/04   -33.333333
2021/01/05    28.571429
dtype: float64
'''

# 3. rename
# - 행, 퀄엄명 변경

emp
emp.colimns = 'emptno', 'ename', 'deptno', 'salary']
emp

emp.rename?

emp.rename({'salary':'sal', 'deptno':'dept_no'}, axis=1)


# [예제] emp 데이터에서 ename 을 index로 설정 후 scott을 SCOOT 변경해 보세요

emp_new=emp.set_index('ename')
emp_new=emp.rename({"scott":"SCOTT"}, axis=0)
emp_new




##동료(fellow), 답안
emp.set_index('ename').rename({'scott':'SCOTT'})

emp.index = emp['ename']
emp.rename({"scott":"SCOTT"}, axis=0)






