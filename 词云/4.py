import jieba
def getText(filePath):
    file = open(filePath,'r',encoding='utf-8')
    text = file.read()
    file.close()
    return text

def wordFreq(filePath,text,topn):
    words = jieba.lcut(text.strip())
    counts={}
    stopwords = stopwordslist('./stop_words.txt')
    for word in words:
        if len(word) == 1:
            continue
        elif word not in stopwords:
            if word == "凤儿姐":
                word="凤姐"
            elif word == "林黛玉" or word=="林妹妹" or word=="黛玉笑":
                word="黛玉"
            elif word=="宝二爷":
                word="宝玉"
            elif word=="裘人道":
                word="裘人"
            else:
                counts[word] = counts.get(word,0)+1
    items = list(counts.items())
    items.sort(key= lambda x:x[1], reverse=True)
    f = open(filePath[:-4]+'_词频.txt','w')
    for i in range(topn):
        word, count = items[i]
        f.writelines("{}\t{}\n".format(word,count))
    f.close()

def stopwordslist(filePath):
    stopwords = [line.strip() for line in open(filePath,'r',encoding='utf-8').readlines()]
    return stopwords

# filePath="./红楼梦.txt"
# text = getText(filePath)
# print(text)
# print(filePath)
# wordFreq(filePath,text,30)


import matplotlib.pyplot as plt
import wordcloud
# from scipy.misc import imread
from imageio import imread

bg_pic=imread('./star.jpg')
f = open("./红楼梦_词频.txt",'r')
text = f.read()
f.close()
dictText= []
temp=[]
count = 0
for i in range(len(text)):
    if text[i] == '\n':
        temp = text[:i].split()
        dictText.append((temp[count],float(temp[count+1])))
        count += 2

wcloud = wordcloud.WordCloud(
    background_color="white",
    width=1000,
    height=860,
    max_words=50,
    margin=1,
    font_path='C:\Windows\Fonts\STXINGKA.ttf',
    mask = bg_pic,

).fit_words(dict(dictText))
plt.imshow(wcloud)
plt.axis('off')
plt.show()

