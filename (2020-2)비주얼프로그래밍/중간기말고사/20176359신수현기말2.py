
#2번



class Phone():
    def __init__(self, name="", telnum=""):
        self.name = name
        self.telnum = telnum        

    
class PhoneBook(Phone):
    
    def __init__(self):
        self.cnt =0

    def add(self, oneperson):
        self.cnt +=1
        phonebook.append(oneperson)

    def getBookCount(self):
        return self.cnt
    
    def getBook(self, i):
        return phonebook[i]
        
       
phonebook =[]

myPhoneBook = PhoneBook()       # 전화번호부 객체 생성하기

oneperson = Phone('홍길동', '010-5555-2222')  # 홍길동 번호 만들기

myPhoneBook.add(oneperson)                                      # 전화번호부에 추가

oneperson = Phone("강감찬", "010-2222-3333")         # 강감찬 번호 만들기

myPhoneBook.add(oneperson)                                     # 전화번호부에 추가

oneperson = Phone("심청", "010-3333-2222")            # 심청 전화번호 만들기

myPhoneBook.add(oneperson)                                      # 전화번호부에 추가


for i in range(myPhoneBook.getBookCount()) :            # 전체 등록된 번호에 대해

    print(myPhoneBook.getBook(i))                                 # 전화번호 출력하기

