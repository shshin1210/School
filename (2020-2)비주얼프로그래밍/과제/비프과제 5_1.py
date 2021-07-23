import readmodule
import writemodule
import os

   
def makerank(strs):
    datas = strs.split("\n")
    new_data = []
    for i in range(len(datas)):
        data = datas[i].split(": ")
        if data[-1] == "오류":
            continue
        new_data.append([data[0], data[-1]])

    maxnum = 0
    maxindex = 0
    tempname = ""
    tempavg = ""

    for i in range(len(new_data) - 1):
        maxnum = 0
        for j in range(i, len(new_data) - 1):
            if maxnum < float(new_data[j][1]):
                maxnum = float(new_data[j][1])
                maxindex = j
        tempname = new_data[i][0]
        tempavg = new_data[i][1]
        new_data[i][0] = new_data[maxindex][0]
        new_data[i][1] = new_data[maxindex][1]
        new_data[maxindex][0] = tempname
        new_data[maxindex][1] = tempavg

    for i in range(len(new_data) - 1):
        print(str(i+1) + ". " + new_data[i][0] + " 평균: " + new_data[i][1])
            
while True:
    file_name, strs = readmodule.readdata()
    print("\n")
    writemodule.makereport(file_name, strs)
    makerank(strs)
