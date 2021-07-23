#실습과제 1-2

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

#실습과제 1-3

hong = '881120-1068234'

split = hong.split('-')

hong_birth = split[0]
hong_num = split[1]

print('생년월일 : %s' %hong_birth)
print('주민번호뒷자리 : %s' %hong_num)


#실습과제 1-4

pin = "881120-1068234"

pinsplit = pin.split('-')

end_num = pinsplit[1]

print('성별 : %s' %end_num[0])


#실습과제 1-5

#1
str = 'a:b:c:d'
str_replace = str.replace(':','#')

print(str_replace)

#2
str_split = str.split(':')

print('#'.join(str_split))
