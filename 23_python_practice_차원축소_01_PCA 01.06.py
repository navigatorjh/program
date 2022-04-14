# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 14:01:51 2022

@author: PC
"""

#23_python_practice_차원축소

# 차원 축소 

# - 분석 대상이 되는 여러 변수의 정보를 최대한 유지하면서 
#   변수의 개수를 줄이는 탐색적 분석기법 
# - 하나의 완결된 분석기법으로 사용되기보다, 다른 분석과정을 위한 전단계, 
#   분석 수행 후 개선 방법, 또는 효과적인 시각화 목적으로 사용 
# - 저차원으로 학습할 경우, 회귀/분류/클러스터링 등의 머신러닝 알고리즘이
#   더 잘 동작함



#PCA

# 1. data loading
from sklearn.datasets import load_iris
iris_x=load_iris()['data']
iris_y=load_iris()['rarget']

iris_x  #변수가 4개 --> 4차원

#2.2차원 축소
from sklearn.preprocessing import StandardScaler as standard
m_sc=standard()
m_sc.fit_transform(iris_x)
iris_x_sc=m_sc.fit_transform(iris_x)

#PCA 적용 전 스케일링 변환
#--------------------------------------------------------------------------
# 3. 주성분 갯수 설정 축소 작업(주성분 개수 : 2개로 설정)
from sklearn.decomposition import PCA
m_pca2=PCA(n_components=2)
iris_x_pca2=m_pca2.fit_transform(iris_x_sc)  # 2차원으로 축소

#----------------------------------------------------------------------------
# 4. 유도된 인공변수로 시각화 ]
import mglearn

mglearn.discrete_scatter(iris_x_pca2[:,0], iris_x_pca2[:,1], y=iris_y)

# 5. 3차원으로 축소

from sklearn.decomposition import PCA
m_pca3=PCA(n_components=3)
iris_x_pca3=m_pca3.fit_transform(iris_x_sc)  # 변수 3개(3차원)으로 축소됨 

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

# 도화지 그리기 , 축 그리기 
fig1=plt.figure()  # 도화지 
ax = Axes3D(fig1)   # 축 

# %matplotlib auto

# step 1) y == 0 인 데이터 포인트만 시각화 
ax.scatter(iris_x_pca3[iris_y==0,0],  # x 축 좌표 
           iris_x_pca3[iris_y==0,1],  # y 축 좌표 
           iris_x_pca3[iris_y==0,2],  # z 축 좌표
           c ='b',
           cmap = mglearn.cm2,
           s = 60,                    # 점의 크기(size)
           edgecolors = 'k'           # black 
           )
# step 2) y == 1 인 데이터 포인트만 시각화
ax.scatter(iris_x_pca3[iris_y==1,0],  # x 축 좌표 
           iris_x_pca3[iris_y==1,1],  # y 축 좌표 
           iris_x_pca3[iris_y==1,2],  # z 축 좌표
           c ='r',
           cmap = mglearn.cm2,
           s = 60,                    # 점의 크기(size)
           edgecolors = 'k'           # black 
           )
# step 3) y == 2 인 데이터 포인트만 시각화
ax.scatter(iris_x_pca3[iris_y==2,0],  # x 축 좌표 
           iris_x_pca3[iris_y==2,1],  # y 축 좌표 
           iris_x_pca3[iris_y==2,2],  # z 축 좌표
           c ='y',
           cmap = mglearn.cm2,
           s = 60,                    # 점의 크기(size)
           edgecolors = 'k'           # black 
           )

# 모델 적용 (KNN_최근접 이웃)
from sklearn.neighbors import KNeighborsClassifier as knn

m_knn1 = knn()
m_knn2 = knn()

from sklearn.model_selection import train_test_split

# train_x1, test_x1, train_y1, test_y1 = train_test_split(iris_x_pca2, iris_y)
# train_x2, test_x2, train_y2, test_y2 = train_test_split(iris_x_pca3, iris_y)

train_x1, test_x1, train_y1, test_y1 = train_test_split(iris_x_pca2, iris_y, random_state=0)
train_x2, test_x2, train_y2, test_y2 = train_test_split(iris_x_pca3, iris_y, rnadom_state=0)

# random_state=0
# 초기값 설정 seed 값 고정

m_knn1.fit(train_x1, train_y1) #
m_knn1.score(train_x1, train_y1)


m_pca2.explained_variance_ratio_ #각 인공변수의 분산 설명력
#array([0.72962445, 0.22850762])
sum(m_pca2.explained_variance_ratio_) #0.9581320720000164


m_knn2.fit(train_x2, train_y2)
m_knn2.score(test_x2, test_y2)

m_pca3.explained_variance_ratio_
#array([0.72962445, 0.22850762, 0.03668922])
sum(m_pca3.explained_variance_ratio_) # 0.99










