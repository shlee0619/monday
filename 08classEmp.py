#08classEmp.py

class Emp:
    user_id = 'blue'
    user_pwd = '1234'
    #member변수 = global variable = public variable

    def __init__(self, id, pwd):
        self.user_pwd = pwd
        self.user_id= id

        
    def insert(self, age):
        print('전역변수 user_id', self.user_id)
        print('전달이름 user_pwd', self.user_pwd)
        print('전달 나이', age)
        print('신규등록  insert(self키워드)')

    def delete(self):
        print('삭제')
        print('딕트del, delete where 조건')

ob = Emp('sky', '7789')
ob.insert(7)
ob.delete()