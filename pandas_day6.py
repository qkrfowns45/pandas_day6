# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 21:35:33 2021

@author: qkrfo
"""

#UCI 머신러닝 저장소에서 데이터셋을 다운로드 받을 수 있다. 여기서는 임의의 csv파일을 사용
import pandas as pd

# read_csv() 함수로 df 생성
df = pd.read_csv('./auto-mpg.csv', header=None)

# 열 이름을 지정
df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']

# 데이터프레임 df의 내용을 일부 확인 
print(df.head())     # 처음 5개의 행
print('\n')
print(df.tail())     # 마지막 5개의 행

# df의 모양과 크기 확인: (행의 개수, 열의 개수)를 튜플로 반환 
print(df.shape)
print('\n')

# 데이터프레임 df의 내용 확인 
print(df.info())
print('\n')

# 데이터프레임 df의 자료형 확인 
print(df.dtypes)
print('\n')

# 시리즈(mpg 열)의 자료형 확인 
print(df.mpg.dtypes)
print('\n')

# 데이터프레임 df의 기술통계 정보 확인 describe는 숫자정보만 표현 모든 데이터는 all으로 표현 
print(df.describe())
print('\n')
print(df.describe(include='all'))
print('\n')

# 데이터프레임 df의 각 열이 가지고 있는 원소 개수 확인 
print(df.count())
print('\n')

# df.count()가 반환하는 객체 타입 출력
print(type(df.count()))
print('\n')

# 데이터프레임 df의 특정 열이 가지고 있는 고유값 확인 
unique_values = df['cylinders'].value_counts() 
print(unique_values)
print('\n')

# value_counts 메소드가 반환하는 객체 타입 출력
print(type(unique_values))
print('\n')

# 평균값 
print(df.mean())
print('\n')
print(df['mpg'].mean())
print(df.mpg.mean())
print('\n')
print(df[['mpg','weight']].mean())

# 중간값 
print(df.median())
print('\n')
print(df['mpg'].median())

# 최대값 
print(df.max())
print('\n')
print(df['mpg'].max())

# 최소값 
print(df.min())
print('\n')
print(df['mpg'].min())

# 표준편차 
print(df.std())
print('\n')
print(df['mpg'].std())

# 상관계수 
print(df.corr())
print('\n')
print(df[['mpg','weight']].corr())






