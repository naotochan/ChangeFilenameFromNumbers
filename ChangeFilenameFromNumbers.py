# for python3
# coding: utf-8

import os
import sys

#引数の取得
argvs = sys.argv
#引数の数の取得
argc = len(argvs)

#引数が足りない場合はその旨を出力
if (argc != 2):
    print ("引数が合致しません：ChangeNumberFrom123.py 変えたいフォルダのパス")
    quit()

#変更したいフォルダのパスを引数として取得
path = argvs[1]
#そのディレクトリ内のファイルを取得
files = os.listdir(path)

num = 0

s = "1"
for file in files:
    #このファイルじゃないなら
    if (file != "ChangeFilenameFromNumbers.py"):
        #ファイル名と拡張子に分ける
        paths, ext = os.path.splitext(file)

        #windowsだと\が2つになってパスが正しくなくなるのでreplace
        argvs[1] = argvs[1].replace("\\", "/")

        #ファイルをリネーム
        os.rename(argvs[1]+"/"+file, argvs[1]+"/"+str(num)+ext)
        num += 1
