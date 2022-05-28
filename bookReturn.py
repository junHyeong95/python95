import time

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

bookReturn()