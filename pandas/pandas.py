#import pandas as pd

#読み込みたいファイルを指定する
path = 'C:/Users/mnara/Downloads/ユースケース.md'
#ファイルを開いて、行ごとに読み込む
with open(path, "r", encoding="utf-8") as f:
  s_lines = f.readlines()
f.close()

for s_line in s_lines:
  
  print (s_line)


