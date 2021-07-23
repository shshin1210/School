
#2 로또문제

import random


def lotto_generator(replay):
    i=0
    
    #replay번만큼 로또 번호 생성
    while i < replay:               
        lotto_list =[]

        j=0
        
        #로또 번호 6개 랜덤으로 생성하기
        while j < 6:                    
            lotto_num = random.randint(1,45)
            
            if lotto_num not in lotto_list:
                lotto_list.append(lotto_num)
                j +=1
                
        i+=1

        #로또 list안 int들을 str로 바꿔주기(나중에 .join을 쓰기 위해)
        for i in range(len(lotto_list)):
            lotto_list[i] = str(lotto_list[i])

    return lotto_list

lotto_list2 = []

while True:
    replay = int(input('원하는 숫자를 선택하세요.(1~100)'))

            
    for i in range(replay):
        lotto_list2.append(lotto_generator(replay))

        print('%d회: %s' %(i+1, " ".join(lotto_list2[i])))

    print()
    print('이 주의 로또 번호 : %s' %" ".join(lotto_list2[replay-1]))
        

 
    

