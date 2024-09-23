import time
import sys

class EmpMenu:
    def __init__(self, path):
        self.menu = dict()
        self.path = path

    def save_to_file(self):
        with open(self.path, 'w', encoding='UTF-8') as file:  
            for name, price in self.menu.items():
                file.write(f'{name}[{price}]\n')

    def menuInsertnew(self):
        name = input('이름입력key>>>')
        price = input('가격입력value >>>')
        self.menu[name] = price
        print(name, '등록 성공했습니다')
        self.save_to_file()  

    def menuAllprint(self):
        for k, v in self.menu.items():
            print(k, ' ', v)
        print()

    def menuEditupdate(self):
        name = input('편집대상 키값 입력>>> ')
        if self.menu.get(name) is None:
            print('편집대상 딕트가 key 없습니다')
        else:
            price = input('변경가격 재입력value >>>')
            self.menu[name] = price
            print(name, '가격수정편집 성공했습니다')
            self.save_to_file()  

    def menuDelete(self):
        name = input('삭제대상 키값 입력>>> ')
        if self.menu.get(name) is None:
            print('삭제대상 딕트가 key 없습니다')
        else:
            self.menu.pop(name)
            print(name, '데이터삭제 성공했습니다')
            time.sleep(0.3)
            for k, v in self.menu.items():
                print(k, ' ', v)
            self.save_to_file()  

    def menuFindsearch(self):
        key = input('조회검색 key 입력>>> ')
        if self.menu.get(key) is None:
            print(key, '데이터가 없습니다')
        else:
            print(key, self.menu[key], '데이터 조회성공했습니다')

    def menuFileOpen(self):
        try:
            with open(self.path, 'r', encoding='UTF-8') as file:  
                content = file.read()
                print(content)
        except FileNotFoundError:
            print("파일을 찾을 수 없습니다.")
        except Exception as e:
            print(f"파일을 여는 중 오류 발생: {e}")

    def menuExit(self):
        print('딕트처리를 종료합니다\n')
        sys.exit()

#-------------------------------------------------------------------
#-------------------------------------------------------------------
path = 'C:/Mtest/menu.txt'  # 파일 경로 수정
menu_manager = EmpMenu(path)

while True:
    print()
    num = int(input('1등록 2출력 3수정 4삭제 5조회 6파일열기 9종료>>'))
    if num == 9:
        menu_manager.menuExit()
    elif num == 1:
        menu_manager.menuInsertnew()
    elif num == 2:
        menu_manager.menuAllprint()
    elif num == 3:
        menu_manager.menuEditupdate()
    elif num == 4:
        menu_manager.menuDelete()
    elif num == 5:
        menu_manager.menuFindsearch()
    elif num == 6:
        menu_manager.menuFileOpen()
    else:
        print('처리번호를 잘못 입력하셨네요\n')