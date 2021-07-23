#실습과제 6-1

import random
import math
import numpy as np

randnum = []
total_1 = 0
total_2 =0

for i in range(0,20):
    randnum.append(random.randint(0,10))

for i in range(len(randnum)):
    total_1 += randnum[i]

mean = total_1/len(randnum)

for i in range(len(randnum)):
    total_2 += (randnum[i] - mean)**2

std_c = math.sqrt(total_2/19)
std_m = np.std(randnum)

print('평균은 : %d' %mean)
print('표준편차는(계산) : %d' %std_c)
print('표준편차는(모듈) : %d' %std_m)

#실습과제 6-2

import matplotlib.pyplot as plt

import numpy as np

def f(x):
    return (x-2)*(x-1)*x*(x+1)

def g(x):
    return (x+2)*(x-1)*x*(x+1)

x=np.linspace(-3, 3, 100)
plt.plot(x, f(x), color='black', label='$f$')    #수식
plt.plot(x, g(x),color='cornflowerblue', label='$g$')

plt.legend(loc='upper left')
plt.ylim(-2, 15)
plt.title('$f(x) and g(x)$')
plt.xlabel('$x$')
plt.ylabel('$y$')

plt.grid(True)
plt.show()


#실습과제 6-3

import math
import matplotlib.pyplot as plt
import numpy as np

def f(x0,x1):
   r= 2*x0**2 + x1**2
   ans = r*np.sin(r)
   return ans
  

xn = 9
x0 = np.linspace(-2,2,xn) # -2 와 2 사이 9 개
x1 = np.linspace(-2,2,xn) # -2 와 2 사이 9 개
y = np.zeros((len(x0), len(x1))) #9행 9열 0행렬을 잡은 것

for i0 in range(xn):
  for i1 in range(xn):
    y[i1,i0] = f(x0[i0], x1[i1])

from mpl_toolkits.mplot3d import Axes3D #함수임포트

xx0, xx1 = np.meshgrid(x0, x1) #좌표점을 튜플형태로

plt.figure(figsize=(5, 3.5))
ax = plt.subplot(1, 1, 1, projection='3d') #3차원지정
ax.plot_surface(xx0, xx1, y, rstride=1, cstride=1, alpha=0.3, color='blue', edgecolor='black') #stride는 선 갯수조정, 알파는 면투명도
ax.set_zticks((0, 0.2))#z의 범위 제한
ax.view_init(75, -95)#3차원 그래프의 방향 조정 75는 상하 방향, -95는 반시계방향 95도 회전
plt.show()



#실습과제 6-4

import random

print('숫자는 무엇일까요?')


def numplay():
   cnt = 1
   com_num = random.randint(1,32)
   
   while True:
       
       my_num = int(input())

       if cnt >= 6 :
           ans = input('6번의 기회를 다 썼습니다 다시 시도하겠습니까?(y/n)')
           if ans == 'y':
               print('숫자는 무엇일까요?')
               cnt = 1
               continue
           else:
               break

       elif cnt < 6:

           if my_num > com_num :
               print('%d 보다 작습니다' %my_num)
               cnt +=1
               continue
               
           elif my_num < com_num:
               print('%d 보다 큽니다' %my_num)
               cnt +=1
               continue
           else:
               print('정답입니다')
               
               break

numplay()


#실습과제 6-5

num = int(input('원하는 평행 이동을 적으시오'))
string = input('보내고 싶은 메세지는?')

str_string = ""

for i in range(len(string)):
    cord = ord(string[i]) + num
    if cord > 90:
        cord = cord - 26
        str_string += (chr(cord))
    else:
        str_string += (chr(cord))

print('카이사르로 암호화된 메세지는 %s' %"".join(str_string))



#실습과제 6-6

num = int(input('자연수를 입력하세오'))

while True:
    
    if num%2 ==0:
        num = num / 2
        print(int(num))
        continue

    elif num%2 !=0 and num>1:
        num = num*3 +1
        print(int(num))
        continue

    elif num ==1:
        break

    elif num !=1:
        print(int(num))
        continue



#실습과제 6-7

import itertools as it
import math as m

def find_div(num):
   divisor_list = [1]
   for i in range(2, int(m.sqrt(num) +1)):
      if num%i == 0:
         divisor_list.append[i, int(num/i)]
   return divisor_list

def is_perfect_num(num, func = find_div):
   if num == sum(func(num)):
      return True
   else:
      return False

test_list = [4,6,28,496,8128,33550336, 8589869056, 137438691328, 2305843008139952128]

def prime_fac(num):
   prime_list = []
   while True:
      if num ==1:
         return prime_list
      for i in range(2, round(m.sqrt(num) +2)):
         if i == round(m.sqrt(num) +1):
            prime_list.append(num)
            num = 1
            break
         elif num % i == 0:
            num = int(num/i)
            prime_list.append(i)
            break

def make_div(num):
   prime_list = prime_fac(num)
   prime_set = list(set(prime_list))
   p_count_list = []
   for p in prime_set:
      p_count = prime_list.count(p)
      p_count_list.append(list(range(p_count+1)))

   divisor_list = []

   for p_count in list(it.product(*p_count_list)):
      divisor =1
      for i in range(len(prime_set)):
         divisor *= prime_set[i]**p_count[i]
      if divisor != num:
         divisor_list += [divisor]
   return divisor_list

for i in test_list :
   print(str(i) + ':' + str(is_perfect_num(i, make_div)))
         



#실습과제 6-8

#각자리수 더해주는 함수

def h(a) :
    s = 0
    while a//1 != 0 :
        s += (a%10)**2
        a = int(a/10)
    return (s)

#각 자릿수의 제곱합이 1혹은 4가 될때 까지 반복해서 구해주는 반복문
   
def findhappy(a):
   while 1 :
       a = h(a)
       if a == 4 :
           return 'UnHappy'
           break
       elif a == 1 :
           return 'Happy'
           break

happylist = []

for a in range(1,1001):

   if findhappy(a) == 'Happy':
      happylist.append(a)
   else:
      continue

print(happylist)
   
#실습과제 6-9


class Turtle:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.direction = 0
        self.speed = 1

    def acceleration(self):
        self.speed += 1

    def brake(self):
        self.speed -= 1

    def south(self):
        self.y -= self.speed

    def north(self):
        self.y += self.speed

    def west(self):
        self.x -= self.speed
        
    def east(self):
        self.x += self.speed



turtle = Turtle()

print('거북이 움직이기 게임 \n a : 속도 높이기, b : 속도 낮추기, w : 왼쪽이동, e : 오른쪽 이동, n : 위쪽 이동, s : 아래쪽 이동 \n f : 게임 끝내기')

while True:
    print('지금 위치는 (%d,%d) 입니다.' %(turtle.x, turtle.y))

    key = input()

    if key == 'a' :
        if turtle.speed == 3:
            print('더이상 속도를 높일 수 없습니다')
        else:
            turtle.acceleration()

    elif key == 'b':
        if turtle.speed == 0:
            print('더이상 속도를 늦출 수 없습니다')
        else:
            turtle.brake()
    
    elif key == 's':
        turtle.south()
        
    elif key == 'n':
        turtle.north()
        
    elif key == 'w':
        turtle.west()
        
    elif key == 'e':
        turtle.east()
    
    else:
        print('(%d,%d)에서 끝납니다.' %(turtle.x, turtle.y))
        break
    

