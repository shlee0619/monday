# 06testpickle.py

# open(파일명, 모드wb/rb, 인코딩)
# dump 쓰기/load 읽기
# 피클로 파일처리 import

import pickle
import time

fileName = 'C:/Mtest/movie.pckl'
mybest = {'슈퍼맨super':9.72, '아이언맨iron':7.45, '손흥민':5.3 }

pickle.dump(mybest, open(fileName, 'wb'))
print(fileName, ' 피클저장 성공')
print('*'*100)
print()

#피클파일 저장 dump(1,2)/ load(1,'rb')
data = pickle.load(open(fileName, 'rb'))
print(data)
print(fileName, '피클 읽기 성공')