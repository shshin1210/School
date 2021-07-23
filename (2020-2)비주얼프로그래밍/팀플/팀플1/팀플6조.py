#1
import time

def floor(now, n):
    
    for i in range(now,n+1):
        print("현재 %d층입니다."%i)
        time.sleep(1)
        if n==i:
            print("%d층 도착했습니다."%n)
    return n

def f_down(now, n):

    for i in range(now,n-1,-1):
        print("현재 %d층입니다."%i)
        time.sleep(1)
        if n==i:
            print("%d층 도착했습니다."%n)
    return n

now = 1

while True:
    num = int(input("가고 싶은 층을 입력하세요."))
    if num>now:
        
        now = floor(now, num)
    elif num<now:
        
        now = f_down(now, num)
    else:
        print("현재 층입니다.")
        
#2
collec = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
a = input('문장을 입력하시오. ')
words = a.split(' ')
count = 0
countList= []

for i in range(0, len(words)):
    for j in range(0, len(collec)): 
        if collec[j] in words[i]:
            if words[i] not in countList:
                countList.append(words[i])
                
for i in range(0, len(a)):
    if a[i] in collec:
        count +=1


print('모음 글자 개수 : %d ' %count)
print('모음이 들어간 단어: %s'  %' '.join(countList))

#2 .upper()함수 이용

collec = ['a', 'e', 'i', 'o', 'u']
a = input('문장을 입력하시오. ')
words = a.split(' ')
count = 0
countList= []

for i in range(0, len(words)):
    for j in range(0, len(collec)): 
        if collec[j] in words[i]:
            if words[i] not in countList:
                countList.append(words[i])
                
        if collec[j].upper() in words[i]:
            if words[i] not in countList:
                countList.append(words[i])
        
        
                
for i in range(0, len(a)):
    if a[i] in collec:
        count +=1
    for j in range(0,len(collec)):
        if a[i] in collec[j].upper():
            count +=1
        

print('모음 글자 개수 : %d ' %count)
print('모음이 들어간 단어: %s'  %' '.join(countList))
