#ポワソン分布をまいかい使って、指定された枚数分のカード模様・数字を出力
#カードの模様：0ハート、1スペード、2ダイヤ、3クローバー

import numpy as np
import numpy.random as rd
import glob
import os.path
import re
import shutil
from os import listdir
from shutil import move
import random

#指定枚数　交換するカードを選べないようにする方式
n=int(input())
#班に割り振るファイルを書き換える
han_name=input()

#出力するカード番号
card_list=[]
kigo_name=["h","s","d","c"]

del_list = []

#今回使うファイルパス(状況に応じて書き換え)
file_path = "*/AI班6月コンペ/"


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



card_list = card_pattern(n)

#1~100からn枚選択
NUM = []
for i in range(100):
    NUM.append(str(i+1).zfill(3))
del_list = sorted(random.sample(NUM,k=n))

#フォルダ検索　フォルダ内：AI班6月コンペ>h>h13


print(card_list)
print(del_list)


f = open(file_path + han_name +"/label.txt")  
c = f.readlines()
c = list(set(c))
f.close()

print(c)
for i in range(n):

    #ファイル内の枚数Kとする
    dir = file_path + "/データ/" + str(card_list[i][0])+"/"+str(card_list[i][0])+str(card_list[i][1])
    K = sum(os.path.isfile(os.path.join(dir, name)) for name in os.listdir(dir))
    num = str(rd.randint(0,K-1))
    copy_PATH = dir + "/" + num +".jpg"
    rename_PATH = file_path + han_name +"/" +del_list[i] + ".jpg"
    #print(rename_PATH)
    shutil.copy(copy_PATH, rename_PATH)
    #c[i].replace(c[i],del_list[i] + " " +card_list[i][0]+str(card_list[i][1]))
    c[int(del_list[i])-1] = del_list[i] + " "+card_list[i][0]+str(card_list[i][1])+"\n"
        #出力ファイル名（AI班6月コンペ>OO班）
        #ゴミ箱（AI班6月コンペ>del）
        #ファイルを生成
        #ファイル内に画像をコピペ
print(c)
os.remove(file_path + han_name +"/label.txt")
k=0
for k in range(len(c)):
    with open(file_path + han_name +"/label.txt","a") as f:
        f.write(c[k])
    k +=1
