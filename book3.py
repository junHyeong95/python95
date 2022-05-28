import re
import time

class makelogin: #회원가입 클래스
    def make_id(slef, regist_user):
        regist_id = []
        while True:
            uid = str(input('회원 아이디 입력: '))
            if uid in regist_user:
                print('이미 등록된 id입니다.')
                ex = input('메인 화면으로 이동하시겠습니까? (y/n): ')
                if ex == 'y' or ex == 'Y':
                    return False
                else:
                    continue
            else:
                res_id = slef.chk_id(uid)
                if not res_id:
                    continue
                else:
                    regist_id.append(uid)
                    break
        # print(regist_id)

        while True:
            pwd = str(input('비밀번호 입력: '))
            res_pwd = slef.chk_password(pwd)
            if not res_pwd:
                continue
            else:
                regist_id.append(pwd)
                break
        # print(regist_id)
        return regist_id
    def chk_id(slef, id):
        result = True
        reg = r'^[A-Za-z0-9_]{4,20}$'
        if not re.search(reg, id):
            print('아이디 생성 기준에 부적당합니다!')
            result = False
        return result
    def chk_password(slef, pwd):
        result = True
        reg = r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[!@#$%&*?])[A-Za-z\d!@#$%&*?]{8,20}$'
        if not re.search(reg, pwd):
            print('비밀번호 기준에 부적당합니다!')
            result = False
        return result
    def edit_password(slef, uid, pwd):
        n_pwd = ''
        while True:
            pw = str(input('새로운 비밀번호 입력: '))
            if pw == pwd:
                print(f'기존 비번하고 같음!')
                continue
            else:
                res_pwd = slef.chk_password(pw)
                if not res_pwd:
                    continue
                else:
                    n_pwd = pw
                    break
        print(f'id:{uid}, n_pwd:{n_pwd}')
        return uid, n_pwd
#
def bookReturn():
    books = [{"num": 1, "제목": "안드로이드앱개발", "저자": "최전산", "출판사": "PCB", "출판년도": "2017", "제고": 0},
               {"num": 2, "제목": "파이썬", "저자": "강수라", "출판사": "연두", "출판년도": "2019", "제고": 0},
               {"num": 3, "제목": "자바스크립트", "저자": "박정식", "출판사": "SSS", "출판년도": "2018", "제고": 0},
               {"num": 4, "제목": "HTML5", "저자": "주환", "출판사": "대한", "출판년도": "2011", "제고": 0},
               {"num": 5, "제목": "컴파일러", "저자": "장진웅", "출판사": "PCB", "출판년도": "2011", "제고": 0},
               {"num": 6, "제목": "C언어", "저자": "헝말숙", "출판사": "한국", "출판년도": "2010", "제고": 0},
               {"num": 7, "제목": "프로그래밍언어론", "저자": "현정숙", "출판사": "정의출판", "출판년도": "2010", "제고": 0},
               {"num": 8, "제목": "안드로이드", "저자": "이광희", "출판사": "한국", "출판년도": "2013", "제고": 0},
               {"num": 9, "제목": "앱인벤터", "저자": "박규진", "출판사": "대한", "출판년도": "2015", "제고": 0}]
    for i in books:
        print(i) #리스트 줄바꿈하여 출력
    booknumber=int(input("반납할 책번호 입력해주세요 : "))
    choice=next((item for item in books if item['num'] == booknumber), None)
    choice['제고']=1
    print(choice['제목'], "|제고: ",choice['제고'], "|")
    for i in books:
        print(i)#리스트 줄바꿈하여 출력
    time.sleep(2)
#
def main():
    regist_user = {'haha': 'gg!!11'}
    sw = True
    a = makelogin()
    while sw:
        print('-----------------------------')
        print('1. 로그인 하기')
        print('2. 회원 아이디 생성')
        print('3. 비밀번호 변경')
        print('4. 전체 회원 아이디 목록 보기')
        print('5. 종료')
        print('-----------------------------\n')

        select_no = int(input('번호 선택(1~5): '))
        if select_no == 1:
            print("로그인을 시작합니다. ")
            x = input("ID를 입력해주십시오 : ")
            if not(x in regist_user.keys()):
                print("ID또는 비밀번호가 알맞지 않습니다. ")
                print("다시 로그인 해주세요!")
                time.sleep(1)
            else:
                y = input("비밀번호를 입력해 주십시오 : ")
                if not(y in regist_user.get(x)):
                    print("ID또는 비밀번호가 알맞지 않습니다. ")
                    print("다시 로그인 해주세요!")
                    time.sleep(1)
                else:
                    print("안녕하세요 회원님!")
                    time.sleep(1)
                    ##메인화면으로 연결 하는 코드 쓰는곳
        if select_no == 2:
            id_result = a.make_id(regist_user)
            if id_result:
                regist_user[id_result[0]] = id_result[1]
                print(regist_user)

        if select_no == 3:
            uid = str(input('회원 아이디: '))
            if uid in regist_user:
                print(f'{uid} / {regist_user[uid]}')
                n_pwd = a.edit_password(uid, regist_user[uid])
                regist_user[uid] = n_pwd
                print('비밀번호 변경 완료!\n')
            else:
                print('등록된 아이디가 아닙니다.\n')
                continue

        if select_no == 4:
            for k, v in regist_user.items():
                print(f'id: {k} / pw: {v}')
            print()

        if select_no == 5:
            sw = False

#main() #로그인 불러오기
bookReturn()