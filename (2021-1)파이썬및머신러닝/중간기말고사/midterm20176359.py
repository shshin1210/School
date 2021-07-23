#신수현 20176359 1 8 9 12 17

#1 (a)

a= 'Life is too short. You need a python'
cnt = 0

for i in range(len(a)):
   if a[i] == 't' or a[i] == 'T':
      cnt +=1
   else:
      pass

print('t 개수는 %d개이다' %cnt)

#1 (b)
print()
num = input('두 숫자 사이의 쌍둥이 소수를 찾을 두 숫자를 입력하시오')

num_split = num.split(',')

first_num = int(num_split[0])
sec_num = int(num_split[1])

total =0

answer = set(range(first_num, sec_num+1))

for i in range(2,sec_num+1):
    if i in answer:
        answer -= set(range(i*2,sec_num+1,i))

set_lst = list(answer)

if 1 in set_lst:
   set_lst.remove(1)

for i in range(len(set_lst)):
   if set_lst[i] +2 in set_lst:
      print('( %d, %d )' %(set_lst[i], set_lst[i]+2), end = " ")
   else:
      continue
print()

#8 (a)
print()
a = [1, 4, 3, 2]

new_a = sorted(a)
new_a.append(5)

print(new_a)


#8 (b)
print()

# 진법 변환기

# 10진수 값 x를 y진수로 바꿔 반환하는 함수
def conv(x, y):
   s = ''
   t = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
   while x > 0:
      s += t[int(x % y)]
      x = int(x//y)
   s = s[::-1]
   return s

num = input("입력) 수 :")

fromBase = int(input("진법 :"))

# int(num, base)는 파이썬이 제공하는 기본 함수로,
# [base]진법으로 표현된 num문자열을 10진수 숫자로 바꿔줌
numByBase10 = int(num, fromBase)

toBase = int(input("표현할 진법 :"))

result = conv(numByBase10, toBase)

print(f"{fromBase}진법으로 {num}는 {toBase}진법으로 {result}입니다.")


#9 (a)
print()
leap = True

def is_leap_year(year):
    if year %4 ==0 and year%100 !=0 or year%400 ==0:
        leap =True
        return leap
        
    else:
        leap = False
        return leap
      
year = int(input('몇년도?'))

#윤년에는 2월이 29
#윤년이 아니면 2월은 28

day31 = [1,3,5,7,8,10,12]

def days_in_month(year, month):
    if month in day31:
        print('%d월은 31일까지이다' %month)

    elif month not in day31:
        if month != 2:
            print('%d월은 30일까지이다' %month)
        else:
            if is_leap_year(year) == True:
                print('%d월은 29일까지이다' %month)
            else:
                print('%d월은 28일까지이다' %month)

month =  int(input('몇월?'))
days_in_month(year, month)


#9 (b)
print()
leap = True

def is_leap_year(year):
    if year %4 ==0 and year%100 !=0 or year%400 ==0:
        leap =True
        return leap
        
    else:
        leap = False
        return leap
      
year = int(input('몇년도?'))

#윤년에는 2월이 29
#윤년이 아니면 2월은 28

day31 = [1,3,5,7,8,10,12]

month =  int(input('몇월?'))
day = int(input('몇일?'))


total = 0

#1918년도일때의  날수
if year == 1918:
   if month == 10:
      total += (day-11)
   elif month == 11:
      total += (20 + day)
   else:
      total += (50 +day)

#1919년도일 때의 날수
elif year == 1919:
   #마지막달 전까지의 날 수
   for i in range(1, month):
         if i in day31:
            total += 31
         elif i == 2:
            total += 28
         else:
            total += 30
            
   #마지막 달 날 수 계산  (1918년도 81일 더해주기)      
   total += (day+81)

   
#윤년인지에 따른 해에 따른 날 수 계산
elif year > 1919 :
   for i in range(1920, year):
      if is_leap_year(i) == True:
         total += 366
      else:
         total += 365

   #마지막 해 윤년인지 아닌지에 따른 달마다 날 수 계산
   if is_leap_year(year) == True:      
      for i in range(1, month):
         if i in day31:
            total += 31
         elif i == 2:
            total += 29
         else:
            total += 30

   if is_leap_year(year) == False:      
      for i in range(1, month):
         if i in day31:
            total += 31
         elif i == 2:
            total += 28
         else:
            total += 30
         
   #마지막 달 날 수 계산 (1918년도 81일 + 1919년도 365일 더해주기)      
   total += (day + 81 + 365)

print('개교일로부터 %d 일이 지났다' %total)


#12 (a)
print()
sentence = input('문장을 입력하시오')

replace = sentence.replace(" ",";")
print(replace)


#12 (b)
print()
N = int(input('N의 값은?'))
lst = []
total =0

for i in range(1,N+1):
   if i%3 == 0 or i%5==0 or i%7==0:
      lst.append(i)
   else:
      continue

set_lst = set(lst)
lst2 = list(set_lst)

for i in range(len(lst2)):
   total += lst2[i]

print('%d이하 3, 5, 7의 배수의 합은 %d 이다' %(N,total))


#17 (a)
print()
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
    print('수가 아닙니다. 수를 입력하시오.')


#17 (b)
print()

ugly= []
def is_ugly(num):
   if num <=0:
      return False
   while num%2 == 0:
      num /=2
   while num%3==0:
      num /= 3
   while num%5 ==0:
      num /= 5
      
   return num ==1

number = int(input('1부터 N까지 못난이 수'))

for i in range(number+1):
   if is_ugly(i) == 1:
      ugly.append(i)
   else:
      continue

print(ugly)
