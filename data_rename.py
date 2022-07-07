#今回使うファイルパス(状況に応じて書き換え)
file_path = "*/AI班6月コンペ/"

card = ["h","s","d","c"]

import os
for n in range(len(card)):
    for j in range(13):
        dir_path = file_path + "/データ/" +card[n]+"/"+card[n]+str(j+1)
        dir_list = os.listdir(dir_path)

        for i in range(len(dir_list)):
            new_file_name = "{}.jpg".format(i) #ファイル名 "new_name_"+ 連番 + ".txt"
            os.rename(os.path.join(dir_path,dir_list[i]),os.path.join(dir_path,new_file_name))

