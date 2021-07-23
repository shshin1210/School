
#1번
    
f = open('littleprince.txt', 'r')

#단어 개수를 찾는 Counter 쓰기 위해 import
from collections import Counter

wordDict = Counter()

sentences = f.readlines()

#나중에 단어와 단어 쓰인 횟수 담을 리스트
word_list =[]

for sentence in sentences:
    for word in sentence.split():
        wordDict[word] +=1

for word, freq in wordDict.most_common(10):
    word_list.append([word,freq])

f.close()


f = open("dict_test.txt", 'r')


while True:
    #단어장에 없는 단어를 대비
    found = False
    v=f.readline()

    #단어장 끝에 도달하면 break
    if v == "" :
        break
            
    for i in range(len(word_list)):
        #단어 리스트에 담긴 단어와 단어장에 있는 단어 비교
        if word_list[i][0] == v.split(':')[0][:-1]:           
            print(v.split(':')[0][:-1],'(',word_list[i][1],')',":", v.split(':')[1])
            found = True
            break
                                      
if found == False:
    print(word_list[i][0], ' Not Found')

        
f.close()


