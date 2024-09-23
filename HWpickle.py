# 06testpickle.py

# open(파일명, 모드wb/rb, 인코딩)
# dump 쓰기/load 읽기
# 피클로 파일처리 import

import pickle
import time
import sys

path = 'C:/Mtest/myCalendar.pckl'


while True:
    print()
    num = int(input('1.스케줄 기록 2.스케줄 읽기 9.종료>>>'))

    if num == 1:
        file = open(path, 'ab')
        w = input('스케줄>>> ')
        pickle.dump(w, file)
        file.close()
        print(path, '피클 저장성공')
    elif num==2:
        file = open(path, 'rb')
        r = pickle.load(file)
        print(r)
        file.close()
        print(path,'피클 오픈읽기처리 성공')
    elif num == 9:
        print('파일처리 종료')
        sys.exit()
    else:
        print('작업번호 오류')
# fileName = 'C:/Mtest/movie.pckl'
# mybest = {'슈퍼맨super':9.72, '아이언맨iron':7.45, '손흥민':5.3 }

# pickle.dump(mybest, open(fileName, 'wb'))
# print(fileName, ' 피클저장 성공')
# print('*'*100)
# print()

# #피클파일 저장 dump(1,2)/ load(1,'rb')
# data = pickle.load(open(fileName, 'rb'))
# print(data)
# print(fileName, '피클 읽기 성공')