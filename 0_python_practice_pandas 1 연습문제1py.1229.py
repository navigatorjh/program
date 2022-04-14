# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 14:14:38 2021

@author: PC
"""
# 판다스 연습문제
run my_modules

df1 = pd.read_csv("./data/cancer_test.csv")
df1.columns
df1.dtypes

df1.head()
df1.info()
df1.describe()

# 1. radius_mean, texture_mean, texture_se, smoothness_se
# NA 인 행을 제거한 후 총 행의 수 리턴

df1['radius_mean'].isnull().sum()    
df1[' texture_mean'].isnull().sum()
df1['texture_se'].isnull().sum()
df1['smoothness_se'].isnull().sum()

