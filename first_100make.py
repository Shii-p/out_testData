from csv import list_dialects
import numpy as np
import numpy.random as rd
import glob
import os.path
import re
import shutil
from os import listdir
from shutil import move

#班に割り振るファイルを書き換える
han_name=input()

#出力するカード番号
card_list=[]
kigo_name=["h","s","d","c"]


def card_pattern(n):
    N=n
    for i in range(N):
        kigo = kigo_name[rd.randint(0,3)]
        num = rd.poisson(4,1)[0] #ポアソン分布に従う
        if int(num)>12:
            N+=1
        else:
            card_list.append((kigo,int(num)+1))
    return(card_list) #[("h",3)("s",5),...]



card_list = card_pattern(100)

f = open("/Users/fujiokashino/Desktop/AI班6月コンペ/" + han_name +"/label.txt")  
c = f.readlines()
c = list(set(c))  
f.close()

list_ =  []

for i in range(100):
    #ファイル内の枚数Kとする
    dir="/Users/fujiokashino/Desktop/データ/"+str(card_list[i][0])+"/"+str(card_list[i][0])+str(card_list[i][1]+1)
    K=sum(os.path.isfile(os.path.join(dir, name)) for name in os.listdir(dir))
    num = str(rd.randint(0,K-1))
    copy_PATH = dir + "/" + num +".jpg"
    card_=i +1
    shutil.copyfile(copy_PATH,"/Users/fujiokashino/Desktop/AI班6月コンペ/" + han_name +"/"+str(card_).zfill(3) + ".jpg")
    list_.append(str(card_).zfill(3)+" "+str(card_list[i][0])+str(card_list[i][1]+1)+"\n")



        #出力ファイル名：（AI班6月コンペ>OO班）
        #ファイルを生成
        #ファイル内に画像をコピペ

with open("/Users/fujiokashino/Desktop/AI班6月コンペ/" + han_name +"/label.txt", 'w') as f:
    for i in range(100):
        f.write(list_[i])