# 5-1

print('1번문제')

class Coordinate():
    x=0
    y=0
    
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

    def describe(self):
        print('x좌표: %s, y좌표: %s' %(self.x,self.y))

print()

#5-2

print('2번문제')

point_1 = Coordinate(-1,2)
point_2 = Coordinate(2,3)

point_1.describe()
point_2.describe()

print()

#5-3

print('3번문제')

import math

def square(x):
    """전달받은 수의 제곱을 반환한다."""
    return x * x

def distance(point_1, point_2):
    """두 점 사이의 거리를 계산해 반환한다. (피타고라스의 정리)"""
    return math.sqrt(square(point_1.x - point_2.x) + square(point_1.y - point_2.y))

point_1 = Coordinate(-1,2)
point_2 = Coordinate(2,3)

print(distance(point_1, point_2))

print()

#5-4

print('4번문제')

class Coordinate():
    x=0
    y=0

    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

    def describe(self):
        print('x좌표: %s, y좌표: %s' %(self.x,self.y))

    def distance(self, point_1,point_2):
        """두점 사이 거리 계산"""
        print(math.sqrt(square(point_1.x - point_2.x) + square(point_1.y - point_2.y)))

point_1 = Coordinate(-1,2)
point_2 = Coordinate(2,3)

point_1.distance(point_1,point_2)
print()

#5-5

print('5번문제')


class Coordinate():

    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

    def describe(self):
        print('x좌표: %s, y좌표: %s' %(self.x,self.y))

    def distance(self, point_1,point_2):
        """두점 사이 거리 계산"""
        print(math.sqrt(square(point_1.x - point_2.x) + square(point_1.y - point_2.y)))

point_1 = Coordinate()
point_2 = Coordinate()

point_1.x = 3

point_1.describe()

print()

#5-6

print('6번문제')

class FourCal():
    def __init__(self):
        pass

    def setdata(self,a,b):
        self.a =a
        self.b = b
        
    def add(self):
        print(self.a+self.b)

a = FourCal()
a.setdata(4,2)
a.add()

print()

#5-7

print('7번문제')


class SquarePillar():
    def __init__(self, width,depth ,height):
        self.height= height
        self.width = width
        self.depth = depth

    def volume(self):
        volume = self.height* self.width *self.depth
        print('부피는 :', volume)

    def surface(self):
        surface = 2*(self.height* self.width+self.width *self.depth+self.height *self.depth)
        print('겉넓이는:',surface)

square_1 = SquarePillar(3,2,5)
square_1.volume()
square_1.surface()

print()

#5-8

print('8번문제')

class Shape():
    def __init__(self, sides):
        self.sides = sides
    
    def describe(self):
        print('이 도형은 %d개의 변을 갖고 있습니다' %self.sides)

class Triangle(Shape):
    def __init__(self):
        self.sides = 3


class Rectangle(Shape):
    def __init__(self):
        self.sides = 4

shapes = [Triangle(), Rectangle()]

for shape in shapes:
    shape.describe()

print()


#5-9

print('9번문제')    


class Coordinate():

    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

    def distance(self,other):
        """두점 사이 거리 계산"""
        return ((self.x - other.x)**2 +(self.y - other.y)**2)**(1/2)



class Shape():
    def __init__(self, *points):
        self.sides = len(points)
        self.vertax = []

        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        for i in range(len(points)):
            setattr(self,f"point_{alphabet[i]}", points[i])
            self.vertax.append(points[i])

    def describe(self):
        print('이 도형은 %d개의 변을 갖고 있습니다' %self.sides)

    def circumference(self):
        result = 0
        for i in range(-1, self.sides-1):
            result += int(self.vertax[i].distance(self.vertax[i+1]))
        return result

class Triangle(Shape):
    def __init__(self, p1,p2,p3):
        super().__init__(p1,p2,p3)


class Rectangle(Shape):
    def __init__(self, p1,p2,p3,p4):
        super().__init__(p1,p2,p3, p4)


shapes = [
    Triangle(Coordinate(0,0),Coordinate(3,0),Coordinate(3,4)),
             Rectangle(Coordinate(2,2),Coordinate(6,2),Coordinate(6,6),Coordinate(2,6)),
]


for shape in shapes:
    shape.describe()
    print('둘레:', shape.circumference())

print()


#5-10

print('10번 문제')

class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

class UpgradeCalculator(Calculator):
    def __init__(self):
        self.value = 0

    def minus(self,val):
        self.value -= val


cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)

print(cal.value)

print()

#5-11

print('11번 문제')

class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

        
class MaxLimitCalculator(Calculator):
    def __init__(self):
        self.value =0
        
    def add(self, val):
            self.value += val

            if self.value >100:
                self.value = 100


    
cal = MaxLimitCalculator()
cal.add(50)
cal.add(60)

print(cal.value)

print()



#5-12

print('12번 문제')

class Car():
    def __init__(self, max_speed=160, speed=0, gap =20):
        self.max_speed = max_speed
        self.speed = speed
        self.gap = gap
        
    def speed_up(self):
        self.speed += self.gap
        if self.speed <= self.max_speed :
            print('speed :', self.speed)
        else:
            print('speed는', self.max_speed,' 이상 올라갈수 없습니다')

            
    def speed_down(self):
        self.speed -= self.gap
        
        if self.speed >= 0:
            print('speed :', self.speed)
        else:
            print('speed는 0밑이 될 수 없음')
        

car_1 = Car()

car_1.speed_up()
car_1.speed_down()
car_1.speed_down()


print()


#5-13

print('13번 문제')

class SportCar(Car):
    pass

class Truck(Car):
    pass

car_2 = SportCar(200,45)
car_3 = Truck(100,15)

car_3.speed_up()
car_3.speed_up()
car_3.speed_up()
car_3.speed_up()
car_3.speed_down()
car_3.speed_down()
car_3.speed_down()
car_3.speed_down()
car_3.speed_down()

print()


#5-14
print('14번 문제')

import random 

class Dice:
    def __init__(self, sides):
        self.seed = random.seed(5)
        self.sides = sides
        self.plane = random.randint(1,sides)

    def top(self):
        return self.plane

    def roll(self):
        random.seed(self.seed)
        self.plane = random.randint(1,self.sides)
        return self.plane


dice_4 = Dice(4)      # 사면체 주사위 생성
print('사면체 주사위 테스트 ----')
print('처음 나온 면:', dice_4.top())
print('다시 굴리기:', dice_4.roll())
print('다시 굴리기:', dice_4.roll())

dice_100 = Dice(100)  # 백면체 주사위 생성
print('백면체 주사위 테스트 ----')
print('처음 나온 면:', dice_100.top())
print('다시 굴리기:', dice_100.roll())
print('다시 굴리기:', dice_100.roll())

       
print()

#5-15

print('15번 문제')

class Food:
    """음식을 나타내는 클래스"""
    def __init__(self, taste, calorie):
        """인스턴스를 초기화한다."""
        self.taste = taste      
        self.calorie = calorie  
    
    def __str__(self):          
        """이 음식을 표현하는 문자열을 반환한다."""
        return str(self._taste) + '만큼 맛있고, ' + str(self._calorie) + '만큼 든든한 음식'
    
    def __add__(self, other):    
        """이 음식(self)과 다른 음식(other)을 더한
        새 음식을 반환한다."""
        taste = self.taste + other.taste
        calorie = self.calorie + other.calorie
        return Food(taste, calorie)

    def __gt__(self, other):
        if self.taste > other.taste:
            return True
        else:
            return False

    def __it__(self, other):
        if self.taste < other.taste:
            return true
        else:
            return False

    def __le__(self, other):
        if self.taste < other.taste:
            return True
        else:
            return False

    def __ge__(self, other):
        if self.taste >= other.taste:
            return True
        else:
            return False


strawberry = Food(9, 32)
potato = Food(6, 66)
sweet_potato = Food(12, 131)
pizza = Food(13, 266)
print('딸기 < 감자: ', strawberry < potato)
print('감자 + 감자 < 고구마: ', potato + potato < sweet_potato)
print('피자 >= 딸기: ', pizza >= strawberry)
print('피자 >= 피자: ', pizza >= strawberry)
print('감자 + 딸기 < 피자: ', potato + strawberry < pizza)
print('딸기 == 딸기: ', potato == potato)

















        



