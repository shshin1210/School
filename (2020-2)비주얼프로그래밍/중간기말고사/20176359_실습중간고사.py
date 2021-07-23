#1

sen = "Grief is the agony of an instant the indulgence of grief the blunder of a life"
sen2=""

while True:

    sen_list = sen.split(" ")
    
    word = input('검색할 단어 변경할 단어')

    if word == 'end':
        break

    else:

        list_word = word.split(" ")

        search_word = list_word[0]

        change_word = list_word[1]

        for i in range(len(sen_list)):
            
            if search_word == sen_list[i]:
                
                sen_list[i] = change_word
                break
            
     
        
        sen2 = " ".join(sen_list)
        print(sen2)


        
#2
        
import random
import time

num = [2,3,4,5,6,7,8,9]
math = ['+','*']

num1 = random.choice(num)
num2 = random.choice(num)

math_choice = random.choice(math)

cnt =0
total =0

while True:
   
    num1 = random.choice(num)
    num2 = random.choice(num)

    math_choice = random.choice(math)
    
    real_ans = 0
    
    if math_choice == "+":
        real_ans = num1 + num2
    else:
        real_ans = num1 * num2

    print('%d %s %d =' %(num1,math_choice,num2), end="")
    start= time.time()
    
    ans = int(input())
    end = time.time()
    
    res = end - start
    
    
    if 2- res > 0 :
        if ans == real_ans:
            score = res*100
            
            total += score
        
            print('%d점 획득 총점 %d점(기회%d번)' %(score, total, 3-cnt))
        else:
            cnt +=1
            print('틀렸습니다. 총점 %d점(기회%d번)' %(total, 3-cnt))
            
    else:
        if ans == real_ans:
            
            cnt+=1
            print('시간초과. 총점 %d점 (기회 %d번)' %(total, 3-cnt))
        else:
            cnt +=1
            print('시간초과&틀렸습니다. 총점 %d점(기회%d번)' %(total, 3-cnt))

    if cnt ==3:
        break

