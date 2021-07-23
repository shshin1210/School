class City:
    def __init__ (self,name ):
        self.name = name
        self.owner = -1

    def getOwner(self):
        return self.owner
    def setOwner(self,owner):
        self.owner = owner
    def city_name(self):
        return self.name

class Player:
    def __init__(self):
        self.balance = 4000
        self.location = 0

    def move(self, dice):
        self.location =(self.location +dice)%10

    def buy_city(self):
        if self.balance >= 300:
            self.balance = self.balance -300
            return True
        else:
            return False

    def pay_money(self):
        if self.balance >= 500:
            self.balance -= 500
            return True
        else:
            return False

    def get_money(self):
        self.balance += 500

    def now_location(self):
        return self.location
    def now_money(self):
        return self.balance
    
import random

city = [City('start'),City('Seoul'),City( 'Tokyo'),City('Sydney'),City('LA'),
        City('Cairo'),City('Phuket'),City('New delhi'),City('Hanoi'), City('Paris')]


dice = 0
player = [Player(),Player()]

for i in range(30):
    game = False
    
    for j in range(1,3):

        dice =random.randint(1,6)
        print("%d번"%j, "플레이어의 주사위가 %d이 나왔다"%dice)
        player[j-1].move(dice)
        now = player[j-1].now_location()

        #시작지점인 경우
        if now == 0: 
            print("start에 도착")
            
        else:
            #주인이 없을 경우
            if city[now].getOwner() == -1: #도시구입
                print("%s에 도착(주인없음)."%city[now].city_name())
                
                if player[j-1].buy_city() == True :
                    print("%d번"%j, "플레이어는 %s를 구입한다."%city[now].city_name())
                    city[now].setOwner(j)
                else :
                    print("잔고가 부족하여 구입할 수 없다.")

            #주인이 있을 경우    
            else:
                print("%s에 도착"%city[now].city_name(),"%d이 소유"%city[now].getOwner())
                
                if city[now].getOwner() != j : #소유자 != 플레이어
                    if player[j-1].pay_money() == True:#지불
                        player[city[now].getOwner()-1].get_money()
                    else:                        
                        game = True
                        break
                    
        print("%d번"%j,"플레이어의 잔고는 %d.\n"%player[j-1].now_money())
        
    if game == True:
        print("잔고 부족으로 게임 종료")
        break

if game == False:
    print('게임 30회 진행 완료')
