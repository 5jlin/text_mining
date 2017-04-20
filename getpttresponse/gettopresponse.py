import json
import jieba
from operator import itemgetter
import readfile

with open('Boy-Girl-3356-3358.json', encoding = 'utf-8-sig') as data_file:    
    data = json.load(data_file, encoding = 'utf-8-sig')

def list2freqdict(mylist):
    mydict=dict()
    for ch in mylist:
        mydict[ch]=mydict.get(ch,0)+1
    return mydict

stopword = []

pttstop = readfile.read('ptt_words.txt')
speaial = readfile.read('specialMarks.txt')
chinesestop = readfile.read('chinese_sw.txt')

stopword = pttstop + speaial + chinesestop


#pprint(data)
num = len(data["articles"])
response = []
#for i in range(num):
for i in range(6,7):
    datatmp = data["articles"][i]
    print(i)
    print(data["articles"][i]["article_title"])
    print(data["articles"][i]["content"])
    tmp = []
    s = ""
    if "messages" in datatmp:
        messages = data["articles"][i]["messages"]
        j = 0
        while j < len(messages):
            s = ""
            
            #print(messages[j]["push_userid"])
            s = messages[j]["push_content"]
            for z in range(20):
                if j + z + 1 >= len(messages):
                    j = j + 1
                    break
                elif messages[j]["push_userid"] == messages[j+z+1]["push_userid"]:
                    s = s + messages[j+z+1]["push_content"]
                else:
                    #print(s)
                    response.append(s)
                    j = j+z+1
                    break
     
    
    else:continue

allword = []
for i in response :
    words = jieba.cut(i, cut_all=False)
    for word in words:
        allword.append(word)
        
d = {}
for i in allword :
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

    


for i in response :
    score = 0
    tmp = []
    words = jieba.cut(i, cut_all=False)
    for word in words:
        #tmp.append(word)
        if word not in stopword:
            score += d[word]
    print(i,score)

    
