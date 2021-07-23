'''#4-1
fruit = ['사과','포도','홍시']

in_fruit = input('좋아하는 과일은?')

if in_fruit in fruit:
    print('정답입니다')

else:
    print('오답입니다')

#4-2
def hakjum():
    num = int(input('Score?'))

    if num > 80:
        print('grade is A')

    elif num > 60 and num <=80:
        print('grade is B')

    elif num>40 and num <= 60:
        print('grade is C')

    elif num>20 and num<= 40:
        print('grade is D')

    else:
        print('grade is E')

hakjum()


#4-3
n = 2
total1 = 0
total2 =0
num_list = [8,9,2,3,4,5]

idnum = input('주민등록번호:')

idnum_split = idnum.split('-')

idnum_front = idnum_split[0]
idnum_back = idnum_split[1]

for i in range(len(idnum_front)):
    i = int(idnum_front[i])*n
    total1 += i
    n+=1

for i in range(len(idnum_back)-1):
    i = int(idnum_back[i]) * num_list[i]
    total2 += i

total = total1+total2

left = total%11

last_num = (11-left)%10

if last_num != int(idnum_back[-1]):
    print('유효하지 않은 주민등록번호입니다')
else:
    print('유효한 주민등록번호입니다')


#4-4
def sale(num):
    if num < 10:
        price = num*100
    elif num >=10 and num<30:
        price = num*95
    elif num >=30 and num<100:
        price = num*90
    else:
        price = num*85
    print('%d원' %price)

num = int(input('구매할 상품 개수'))
sale(num)



#4-5
leap = True

def is_leap_year(year):
    if year %4 ==0 and year%100 !=0 or year%400 ==0:
        print('%d년은 윤년이다' %year)
        leap =True
        
    else:
        print('%d년은 윤년이아니다' %year)
        leap = False

year = int(input('몇년도?'))
is_leap_year(year)



#4-6
#윤년에는 2월이 29
#윤년이 아니면 2월은 28

day31 = [1,3,5,7,8,10,12]

def days_in_month(year, month):
    if month in day31:
        print('%d월은 31일이다' %month)

    elif month not in day31:
        if month != 2:
            print('%d월은 30일이다' %month)
        else:
            if is_leap_year(year):
                print('%d월은 29일이다' %month)
            else:
                print('%d월은 28일이다' %month)


year = int(input('몇년도?'))
month =  int(input('몇월?'))
days_in_month(year, month)


#4-7
total =0
i =1

for i in range(1001):
    if i% 3 ==0:
        total += i

print(total)
    


#4-8
A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
total =0

for a in A:
    if a>50:
        total +=a
print(total)
        

#4-9
n =1

while n<5:
    print('*' *n)
    n+=1
    

#4-10
num = 100
total = 0

while num < 10000:
    total += num
    num +=5

print(total)


#4-11
for i in range(1,101):
    print(i, end= " ")


#4-12
print()
A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total =0

for i in range(len(A)):
    total += A[i]

avg = total / len(A)

print('평균은 %d' %avg)


#4-13
numbers = []

for i in range(1,101,1):
    if '3' in str(i) or '6' in str(i) or '9' in str(i):
        print("*", end=" ")

    else:
        print(i, end= " ")


#4-14
print()
for i in range(1,101):
    if i%3 ==0 or i%4 ==0:
        print(i, end =" ")

#4-15
print()
lst = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
maxnum = 0

for i in range(len(lst)):
    if maxnum < lst[i]:
        maxnum = lst[i]

print(maxnum)

#4-16
n=100
total =0

answer = set(range(2,n+1))

for i in range(2,n+1):
    if i in answer:
        answer -= set(range(i*2,n+1,i))

set_lst = list(answer)

for i in range(len(set_lst)):
    total += set_lst[i]

print(total)


'''

num=input('주민등록번호(-제외):')
wei=[2,3,4,5,6,7,8,9,2,3,4,5]
total=0

for i in range(12):
    sum=int(num[i])*int(wei[i])
    total += sum

last=total%11

if (11-last)%10==int(num[-1]):
    print('유효한 주민등록번호입니다.')
else:
    print('유효하지 않은 주민등록번호입니다.')


















