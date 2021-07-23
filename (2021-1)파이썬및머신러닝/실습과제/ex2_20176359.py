
#2-1

a = ['Life','is','too','short']
str =  " ".join(a)
print(str)

#2-2

a = [1,3,5,4,2]
a.sort()
a.reverse()
print(a)

#2-3

b= (1,2,3)
c = (4,)
a=b+c

print(a)


#2-4

dic = {'name':'홍길동', 'birth':1128,'age':30}
print(dic)

#2-5

a = {'A':90, 'B':80}
print(a.get('C',70))

#2-6

a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
print(set(a))

#2-7

inventory = {'메로나': [300,20] , '비비빅' : [400,3],'죠스바': [250,100]}

#2-8

print('%d원' %inventory['메로나'][0])
print('%d개' %inventory['메로나'][1])

inventory['월드콘'] = [500,7]

print(inventory)

#2-9

my_list = ["A", "b", "c", "D"]

for i in range(len(my_list)):
    
    if my_list[i].isupper() == True:
        print(my_list[i])


#2-9 두번째 방법

for alphabet in my_list:
    if alphabet.isupper():
        print(alphabet)
        
#2-10

my_list = ["A", "b", "c", "D"]

for i in range(len(my_list)):
    if my_list[i].isupper() == True:
        my_list[i] = my_list[i].lower()
        
    else:
        my_list[i] = my_list[i].upper()


print(my_list)



















