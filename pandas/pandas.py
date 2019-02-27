#import pandas as pd

#読み込みたいファイルを指定する
path = 'ユースケース.md'
#ファイルを開いて、行ごとに読み込む
with open(path, "r", encoding="utf-8") as f:
  s_lines = f.readlines()
f.close()

for s_line in s_lines:
    if s_line.find("#") >= 0:
        print (s_line[:-1])
    elif s_line.find("##") >= 0:
        print(s_line[:-1])
    elif s_line.find("###") >= 0:
        print (s_line[:-1])


