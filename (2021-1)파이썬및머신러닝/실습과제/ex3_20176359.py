#3-1

def is_odd():
    exit = True

    while exit:

      try:
        
        num = float(input('자연수를 입력하시오'))
        
        if num <= 0 : 
          print('자연수가 아닙니다. 다시 입력해주세요.')

        elif num - int(num) != 0:
          print('자연수가 아닙니다. 다시 입력해주세요.')

        else:    
          if num % 2 == 0:
            print('짝수입니다.')
            exit = False

          else : 
            print('홀수입니다.')
            exit = False
            

      except:
        print('수를 입력하시오.')

is_odd()

#3-2

#첫번째 방법

def avg(*args):
    total =0
    avg =0
    for i in args:
        total +=i
    avg = total/ len(args)

    return avg

print(avg(1,2,3,5,4))

#두번째 방법

def avg():
    total =0
    avg =0
    args = input('숫자를 입력(평균값을 계산해줌)')
    
    args_split = args.split(',')
    
    for i in args_split:
        total += int(i)
    avg = total/ len(args_split)

    print(avg)

avg()



#3-3

def div(a,b):
    return a//b, a%b

print(div(10.2,3.2))
    

#3-4

#첫번째
def total():
    total =0
    args = input('합을 알고 싶은 숫자를 입력하세요 :')
    
    args_split = args.split(',')
    
    for i in args_split:
        total += int(i)

    print('합은 %d 입니다' %total)

total()

#3-5

def mul():
    num = int(input('구구단을 출력할 숫자를 입력하세요(2~9):'))
    for i in range(1,10):
        print(num*i, end=" ")

mul()


#3-6

#첫번째 방법
def fib(n):
    fib_list = []
    
    for i in range(n):
        if i < 2:
            fib_list.append(1)
        else:
            fib_list.append(fib_list[i-2] + fib_list[i-1])

    return fib_list[n-1]

print(fib(20))


#두번째 방법 (재귀함수)


def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1) + fib(n-2)

print(fib(20))



#3-7

def Grading(score):
    if score >=90:
        return 'A'
    elif score >=80 and score < 90:
        return 'B'
    elif score >=70 and score < 80:
        return 'C'
    elif score >=60 and score < 70:
        return 'D'
    else:
        return 'F'
    

score = int(input('당신의 점수는?'))
print('%s점은 %s입니다.' %(score, Grading(score)))


#3-8


def is_odd():
    exit = True

    while exit:

      try:
        
        num = float(input('자연수를 입력하시오'))
        
        if num <= 0 : 
          print('자연수가 아닙니다. 다시 입력해주세요.')

        elif num - int(num) != 0:
          print('자연수가 아닙니다. 다시 입력해주세요.')

        else:    
          if num % 2 == 0:
            print('짝수입니다.')
            exit = False

          else : 
            print('홀수입니다.')
            exit = False
            

      except ValueError:
        print('입력한 값은 수가 아닙니다.')

is_odd()




















    
