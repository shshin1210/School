import matplotlib.pyplot as plt
import numpy as np

import xlrd


isFirst = True
# make a square figure and axes
# pie chart looks best in square figures
# otherwise it looks like ellipses
while True:
    f = xlrd.open_workbook(filename = 'elec.xlsx')

    colors = ['lightblue','pink','purple','burlywood','lightcoral']
    ws = f.sheet_by_index(0)

    labels = []

    for i in range(5):
        labels.append(ws.row_values(0)[i])

    frequency = []

    for i in range(5):
        frequency.append(int(ws.row_values(1)[i]))


    #숫자가 겹치지 않게 sort
    frequency.sort()
    tempsmall = frequency[0] 
    tempbig = frequency[-1]
    frequency[0] = tempbig
    frequency[-1] = tempsmall


    if isFirst:
        isFirst = False
        fig = plt.figure(figsize=(8,8)) ## 캔버스 생성
        
    fig.set_facecolor('white') ## 캔버스 배경색을 하얀색으로 설정
    ax = fig.add_subplot() ## 프레임 생성

     
    pie = ax.pie(frequency, ## 파이차트 출력
           startangle=90, ## 시작점을 90도(degree)로 지정
           counterclock=False, ## 시계방향으로 그려짐
           colors = colors, ## 색상 지정
           )

    total =0

    for i in range(len(frequency)):
        total += frequency[i]


    threshold = 5 ## 상한선 비율
    sum_pct = 0 ## 퍼센티지
     
    bbox_props = dict(boxstyle='square',fc='w',ec='w',alpha=0) ## annotation 박스 스타일
     
    ## annotation 설정
    config = dict(arrowprops=dict(arrowstyle='-'),bbox=bbox_props,va='center')
     
    for i,l in enumerate(labels):
        ang1, ang2 = ax.patches[i].theta1, ax.patches[i].theta2 ## 파이의 시작 각도와 끝 각도
        center, r = ax.patches[i].center, ax.patches[i].r ## 원의 중심 좌표와 반지름길이
        
        if i < len(labels) - 1:
            sum_pct += float(f'{frequency[i]/total*100:.2f}')
            text = f'{frequency[i]/total*100:.2f}%'
        else: ## 마지막 파이 조각은 퍼센티지의 합이 100이 되도록 비율을 조절
            text = f'{100-sum_pct:.2f}%'
        
        ## 비율 상한선보다 작은 것들은 Annotation으로 만든다.
        if frequency[i]/total*100 < threshold:
            ang = (ang1+ang2)/2 ## 중심각
            x = np.cos(np.deg2rad(ang)) ## Annotation의 끝점에 해당하는 x좌표
            y = np.sin(np.deg2rad(ang)) ## Annotation의 끝점에 해당하는 y좌표
            
            ## x좌표가 양수이면 즉 y축을 중심으로 오른쪽에 있으면 왼쪽 정렬
            ## x좌표가 음수이면 즉 y축을 중심으로 왼쪽에 있으면 오른쪽 정렬
            horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
            connectionstyle = "angle,angleA=0,angleB={}".format(ang) ## 시작점과 끝점 연결 스타일
            config["arrowprops"].update({"connectionstyle": connectionstyle}) 
            ax.annotate(text, xy=(x, y), xytext=(1.6*x, 1.5*y),
                        horizontalalignment=horizontalalignment, **config)
        else:
            x = (r/2)*np.cos(np.pi/180*((ang1+ang2)/2)) + center[0] ## 텍스트 x좌표
            y = (r/2)*np.sin(np.pi/180*((ang1+ang2)/2)) + center[1] ## 텍스트 y좌표
            ax.text(x,y,text,ha='center',va='center',fontsize=12)
        
    plt.legend(pie[0],labels,loc='upper right') ## 범례
    plt.draw()
    plt.pause(10)
    plt.clf()
