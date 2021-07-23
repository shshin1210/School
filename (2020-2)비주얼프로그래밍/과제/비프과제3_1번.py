#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd

def df_maker(col_num, ind_num, fill):

    col = []
    ind = []
    con = []
    
    for i in range(0,col_num):
        col.append(fill)
    for i in range(0, ind_num):
        ind.append(fill)
    for i in range(0, ind_num):
        con.append(col)
    return pd.DataFrame(con, columns=col, index =ind)


df = df_maker(17,3,'0')

df.columns = ['서울', '부산', '대구', '인천', '광주', '대전', '울산', '세종', '경기', '강원',
         '충북', '충남', '전북', '전남', '경북', '경남', '제주']
df.index = ['오늘','변동','누계']

   
#오늘 행에 코로나 증가 수 적기
def set_corona_now(corona_today):
    
    corona_todaylst = corona_today.split(',')

    for i in range(0,len(df.loc['오늘'])):
        df.loc['오늘'][i] = corona_todaylst[i] #문자열로된리스트
    
    return corona_todaylst
    
#코로나 변화율
def set_corona_change(corona_today, corona_yes):
    
    corona_todaylst = corona_today.split(',')
        
    for i in range(0, len(df.loc['변동'])):
        if int(corona_todaylst[i]) > int(corona_yes[i]):
            df.loc['변동'][i] = '+'+ str(int(corona_todaylst[i])-int(corona_yes[i]))
        
        elif int(corona_todaylst[i]) < int(corona_yes[i]):
            df.loc['변동'][i] = '-'+ str(int(corona_yes[i]) - int(corona_todaylst[i]))
        
        else:
            df.loc['변동'][i] = '0'
            
#누계
def set_corona_sum(corona_today,corona_yes):

    corona_todaylst = corona_today.split(',')

    for i in range(0, len(df.loc['누계'])):
        df.loc['누계'][i] = str(int(df.loc['누계'][i]) + int(corona_todaylst[i]))

            
i=0
corona_yes = []
from IPython.display import display

while True:

    #현재 저장되어 있는 오늘 코로나 수를 배열에 저장
    corona_yes = list(df.loc['오늘'])
    
    #오늘 코로나 수를 새로 받기
    corona_today = input('%d일차' %(i+1))
    
    #오늘 코로나 증가수를 오늘에 입력
    set_corona_now(corona_today)
    
    #변동구하기
    set_corona_change(corona_today, corona_yes)
    
    #누계 저장
    set_corona_sum(corona_today,corona_yes)    
    display(df)
    i+=1


# In[ ]:




