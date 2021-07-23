#1사용자로부터 숫자 하나를 입력 받은 후, 그 절대값을 화면에
#출력하라. 사용자가 0을 입력할 때까지 이 과정을 반복하라

while True:

    num = int(input('숫자를 입력하세요'))

    if num <0:
        print(-num)
        continue
    
    if num >0:
        print (num)
        continue
    
    if num ==0:
        break

#2 리스트에서 데이터 찾기 
    
place = ['흑석동','사당동','상도동','노량진동','규동']


while True:
    
    search = input('동을 입력하세요')

    if search in place :
        print(place.index(search)+1,'번째 동입니다')
        continue
    
    if search not in place :
        place.append(search)
        print('새로운 동명입니다.',len(place),"째 동으로 등록합니다.")
        continue
    
    
#3

#식당에 다음의 메뉴가 있다. 메뉴를 선택하면 가격을 알려주
#는 프로그램을 작성하라. 다음의 자료를 이용하라.
#‘noodle’:500원, ‘ham’:200원, ‘egg’:100원, ‘spaghetti’:900원



menu = ['noodle','ham','egg','spaghetti']

price = [500,200,100,900]



while True:
    
    
    food = input('안녕하세요 다음의 메뉴 중 원하는 메뉴를 선택하세요\n(noodle,ham,egg,spaghetti)')
       
    if food in menu:
        n = menu.index(food)
        print(price[n],"원입니다")
        continue
    
    if food not in menu:
        print('그런 메뉴는 없습니다')
        continue

   

#4
#사용자로부터 N 개의 숫자를 입력 받은 후, 오름차순으로 정
#렬하여 화면에 출력하라. 0을 입력하면 입력을 종료한다.

number = []
cnt=0

print('데이터를 입력하세요(입력을 마치려면 0을 입력하세요)')
while True:
    
    data = int(input())

    if data != 0:
        number.append(data)
        cnt+=1
        continue
    
    if data == 0:
        break

number.sort()
        
print(number,'(',cnt,'개)')


#5
#2부터 100000 사이의 소수(prime number)가 몇 개인지 화면에 표시하라.
#소수를 화면에 표시할 필요는 없다. 최종 개수만 표시하면 된다.
#정답은 10초 내에 나와야 한다.

n=100000

answer = set(range(2,n+1))

for i in range(2,n+1):
    if i in answer:
        answer -= set(range(i*2,n+1,i))


print(len(answer),'개')


#6 이자 원금 계산하기

money = float(input('원금을 입력하세요(원)'))

r = int(input('금리를 입력하세요(%)'))



print('원금', money,'원 금리', r,'%입니다')

interest = (1 +r/100)

n=0

for n in range (1,21):
    result = (int((money*(interest)**n)*10))/10
    n +=1
    print('기간',n-1,'년 합계:', result)


#7 가위바위보 게임
    
import random
game = ['가위','바위','보']

n=0
i=0
j=0
l=0
k=0

while True:
    com = random.choice(game)
    n +=1

    if i ==3 or j==3:
        break
    
    print('(라운드',n,')')
    print('컴퓨터가 결정했습니다.')
    user = input('무엇을 내시겠습니까?(가위,바위,보)')

    if com == user:
        print('컴퓨터는',com,'당신은',user,'비겼습니다')
        continue
    
    if (com =='가위' and user =='보') or (com=='보' and user=='바위') or (com=='바위' and user =='가위'):
        print('컴퓨터는',com,'당신은',user,'컴퓨터가 이겼습니다')
        i+=1
        k+=1
        print('컴퓨터:', i,'승',l,'패', '당신:',j,'승',k,'패')
        continue
            
    if (user =='가위' and com =='보') or (user=='보' and com=='바위') or (user=='바위' and com =='가위'):
        
        print('컴퓨터는',com,'당신은',user,'당신이 이겼습니다')
        j+=1
        l+=1
        print('컴퓨터:', i,'승',l,'패', '당신:',j,'승',k,'패')
        continue
    


      
