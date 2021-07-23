#1

import random
game = ('가위','바위','보')

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
    user = input('무엇을 내시겠습니까?' + str(game))

    if com == user:
        print('컴퓨터는 %s 당신은 %s 비겼습니다' %(com ,user))
        
    
    elif (com == game[0]  and user ==game[2]) or (com==game[2] and user==game[1]) or (com==game[1] and user ==game[0]):
        print('컴퓨터는 %s 당신은 %s 컴퓨터가 이겼습니다' %(com,user))
        i+=1
        k+=1
        print('컴퓨터: %d 승 %d 패 당신 %d 승 %d 패' %(i,l,j,k))
        
            
    else:
        print('컴퓨터는 %s 당신은 %s 당신이 이겼습니다' %(com,user))
        j+=1
        l+=1
        print('컴퓨터: %d 승 %d 패 당신 %d 승 %d 패' %(i,l,j,k))
        

#2


while True:
    
    sen = input('문장을 입력하세요.')
    
    if '저는' in sen[0:10]:
        
        print('이름: ', end='')
        
        for i in range(3,6):
            
            print(sen[i], end='')
            
        print()
        
        continue
        
    if '제 이름은' in sen[0:10]:
        
        print('이름: ', end='')
        
        for j in range(6,8):
            
            print(sen[j], end='')
            
        print()
        
        continue
    
#3

while True:

    sublist=[]
    strs_list=[]
    sumNum =0
    subNum=0
        

    strs = input('수식을 입력하시오')

    addlist=strs.split('+')

    for i in range(0, len(addlist)):

        if "-" in addlist[i]:
                                      
            strs_list = addlist[i].split('-')
                           
            addlist[i] = strs_list[0]    #addlist i 번째에 덮은 상태       
                                       
            for j in range(1,len(strs_list)):
                    
                sublist.append(strs_list[j])                            

            
    for i in addlist:
        sumNum += int(i)
               
                
    for i in sublist:
        subNum += int(i)
                    
        
    print(sumNum - subNum)



#4

teldic ={'홍길동':'010-4444-5555', '김중앙':'010-9191-8181','심청':'010-3232-5454'}


while True:

    list_keys = list(teldic.keys())
    find = False
    
    name = input('이름은?')

    if name == 'add':
        add_name = input('이름?')
        add_phone = input('번호?')

        teldic[add_name] = add_phone

        print('%s 전화번호가 추가되었습니다' %add_name)

    else:

        for i in range(len(list_keys)):

            if name in list_keys[i]:
                print(list_keys[i], ": ",teldic[list_keys[i]])
                
                find = True

               
        if find == False:
                print('찾을 수 없습니다')


#5

def insertComma(num):
   numString = str(num)
   ret = ""
   cnt = 0
   for number in reversed(numString):
      if cnt != 0 and cnt % 3 == 0:
         ret = number + ',' + ret
      else:
         ret = number + ret
      cnt = cnt + 1
   return ret

def numberToKorean(num):
   # 1 ~ 9의 숫자를 한글로 반환
   if num == 1:
      return '일'
   if num == 2:
      return '이'
   if num == 3:
      return '삼'
   if num == 4:
      return '사'
   if num == 5:
      return '오'
   if num == 6:
      return '육'
   if num == 7:
      return '칠'
   if num == 8:
      return '팔'
   if num == 9:
      return '구'
   return ''

def representSmallNumberByKorean(num):
   # '일', '십', '백', '천' 단위까지 한글로 반환

   numString = str(num)
   length = len(numString)
   temp = ""
   ret = ""
   cnt = 0
   if length == 4:
      temp = numberToKorean(int(numString[cnt]))
      if temp == '':
         pass
      elif temp == '일':
         ret = ret + '천'
      else:
         ret = ret + temp + '천'
      cnt = cnt + 1
   if length >= 3:
      temp = numberToKorean(int(numString[cnt]))
      if temp == '':
         pass      
      elif temp == '일':
         ret = ret + '백'
      else:
         ret = ret + temp + '백'
      cnt = cnt + 1      
   if length >= 2:
      temp = numberToKorean(int(numString[cnt]))
      if temp == '':
         pass      
      elif temp == '일':
         ret = ret + '십'
      else:
         ret = ret + temp + '십'
      cnt = cnt + 1         
   if length >= 1:
      ret = ret + numberToKorean(int(numString[cnt]))

   return ret


def representBigNumberByKorean(num):
   # '만', '억' 단위까지 한글로 변환
   # 1. '억' 1에 대해서 무조건 '일' 로 표기
   # 2. '만'은 1보다 더 큰 자리수가 존재하면 '일' 로 표기

   numString = str(num)
   length = len(numString)
   temp = ""
   ret = ""
   cnt = 0

   if length >= 9:
      temp = representSmallNumberByKorean(int(numString[cnt : length - 8]))
      if temp != "":
         ret = ret + temp + '억'
      cnt = length - 8
   if length >= 5:
      temp = representSmallNumberByKorean(int(numString[cnt : length - 4]))
      if temp != "":
         if temp == '일' and length == 5:
            ret = ret + '만'
         else:
            ret = ret + temp + '만'
      cnt = length - 4

   ret = ret + representSmallNumberByKorean(int(numString[cnt:]))

   return ret

while True:
   num = input('숫자는? ')

   print(insertComma(num))
   print(representBigNumberByKorean(num))
   print("")














