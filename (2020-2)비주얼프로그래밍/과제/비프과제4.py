#1

while True:

    f = open("dict_test.txt", 'r')
    
    word = input('단어?')
    found = False

    try:
        while True:
            v=f.readline()

            if v == "" :
                break

            if word == v.split(':')[0][:-1]:         
                print(v[:-1])
                found = True

                break
                
        if found == False:
            print(word + ' Not Found')
            
    except TypeError:
        print('문제가 있어요')
        
f.close()

'''

#2

word = 'apple'

word_list = []

while True:
    found = False
    f = open("dict_test.txt", 'r')
    
    ques = input('%s 끝말잇기?' %word)

    #단어 짧은거
    if len(ques) < 5:
        print('단어가 짧아요(%s의 끝말을 이으세요).' %word)
        continue

    #단어가 긴거
    elif len(ques) > 5 :
        print('단어가 길어요(%s의 끝말을 이으세요).' %word)  
        continue

    while True:
        
        v = f.readline()
        v_split = v.split(":")[0][:-1]

        # 파일을 끝까지 읽은 경우 break
        if v =="":
            break
        
        if len(ques) ==5:
            #끝자와 첫글자가 맞는지 체크
            if ques[0] == word[4]:
                if ques == v_split:
                    #중복된 단어 비교하기
                    if ques in word_list:
                        print('중복된 단어입니다(%s의 끝말을 이으세요).' %word)
                        found = True
                        break
                    #중복되지 않은 단어일 경우 
                    else:
                        print("정답입니다(%s 의 끝말을 이으세요)." % ques)
                        word_list.append(ques)
                        word = ques
                        found = True          
                        break
            
            else:
                print('삑. 끝말잇기가 안되는 단어입니다.')
                found = True
                break
            
    #사전에 없는 단어
    if found == False:
        print("사전에 없는 단어입니다(%s 의 끝말을 이으세요)." % word)
        
f.close()


#3

# code와 province를 맵핑할 딕셔너리 자료형
code_dic = {}

# code를 담을 배열
code_arr = []

f = open('weather.csv', 'r')

v = f.readline().split(",") 

# 중복을 제거한 코드 리스트 받아온 후 코드 오름차순으로 정렬
while True:
    v = f.readline()

    if v == "":
        break

    v = v.split(",")
    code = int(v[0])
    province = v[1]
    if code not in code_arr:
        code_arr.append(code)               
        code_dic[code] = province        


code_arr.sort()

# 사용자 메뉴 만들기
menu_str = ""

for i in range(len(code_arr)):
    if i == 0:
        menu_str = str(i + 1) + ":" + code_dic[code_arr[i]]
    else:
        menu_str = menu_str + ", " + str(i + 1) + ":" + code_dic[code_arr[i]]



while True:  

    f.seek(0)
    f.readline()

    sel = input("도시를 선택하세요 (%s) " %menu_str)

    # 선택한 도시의 코드 얻어오기
    sel_code = code_arr[int(sel) - 1]

    # 이전년월과 현재읽은데이터년월
    last_ym = ""
    current_ym = ""
    
    cnt = 0

    sum_avg_temp = 0.0
    sum_prec = 0.0

    date_arr = []
    temp_arr = []
    prec_arr = []

    while True:
        v = f.readline()
        #파일을 끝까지 읽은 경우, 지금까지 누적된 변수 값을 마지막으로 배열에 넣고 break
        if v == "":
            date_arr.append(last_ym)
            temp_arr.append(sum_avg_temp/cnt)
            prec_arr.append(sum_prec)

            break

        v = v.split(",")

        code = int(v[0])
        date = v[2].split("-")
        
        # 선택한 도시코드와 동일한 데이터인가 체크
        if sel_code == code:
            current_ym = date[0] + "년 " + str(int(date[1])) + "월"


            if v[3] == "":
                continue

            avg_temp = float(v[3])
            prec = float(v[6])

            if last_ym == "":

                # 현재데이터년월을 이전년월에 갱신
                last_ym = current_ym

                sum_avg_temp = avg_temp
                sum_prec = prec
                cnt = 1
                
            # 이전년월과 현재데이터년월이 다른 경우에는 지금까지 저장한 값을 배열에 담고 변수 초기화.
            else:

                if last_ym != current_ym:
                    date_arr.append(last_ym)
                    temp_arr.append(sum_avg_temp / cnt)
                    prec_arr.append(sum_prec)

                    last_ym = current_ym
                    sum_avg_temp = 0.0
                    sum_prec = 0.0
                    cnt = 0

                sum_avg_temp += avg_temp
                sum_prec += prec
                cnt += 1


    # 저장한 값 출력
    print("\n%s 기후 분석\t\t평균 기온\t월별 강수량(mm)" % code_dic[sel_code])
    for i in range(len(date_arr)):
        print(date_arr[i] + '\t\t' + str(round(temp_arr[i], 1)) + '\t\t' + str(round(prec_arr[i], 1)))

    print('\n')
'''
