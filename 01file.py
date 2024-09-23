# 01file.py

# 임포트 문장 X import file~~~\
# pathName = '경로/파일.txt'
# 리턴변수 = open(파일명, 모드w/r/a, 인코딩)
# 리턴변수.close()
# open() 대체 with open() as ff
import time

pathName = 'C:/Mtest/sample.txt'
wfile = open(pathName, 'a', encoding='UTF-8')
name = input('이름입력>>> ')
age = input('나이입력>>> ')
juso = input('주소입력>>> ')

wfile.write(name + '\n')
wfile.write(age + '\n')
wfile.write(juso + '\n')
wfile.close() #추천권장

print(pathName,'파일저장성공')
print()

print('-'*780)
pathName2 = 'C:/Mtest/kakao.txt'
with open(pathName2, 'a', encoding='UTF-8') as myfile:
    name = input('이름입력>>> ')
    age = input('나이입력>>> ')
    juso = input('주소입력>>> ')

    myfile.write(name + '\n')
    myfile.write(age + '\n')
    myfile.write(juso + '\n')

#생략가능 myfile.close()
print(pathName2, '파일저장성공')
print()