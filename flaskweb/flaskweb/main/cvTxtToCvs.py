# since 2019-08-22
# author : Ramfaster
# Description
# text 파일을 csv 로 파일로 변환 후 저장
# 변환된 파일은 기존 폴더에서 신규폴더로 이동
# 원본 text 파일은 이동폴더로 이동


import pandas as pd
import os
import sys
import glob
import shutil

def maketxttocsv (dirname):
    #path_dir = 'd:/Docs/05. 회사관련/05. 자료조사/14.데이터분석/한화HAS/NC설비(mt02)데이터_20190724/bak'
    # file_list = os.listdir(dirname)
    # for filename in file_list if filename:
    #     full_filename = os.path.join(filename)
    #     print (full_filename)

    #print(dirname)
    os.chdir(dirname) #디렉토리를 바꿔야 할 경우에만 쓰세요
    read_dir =  dirname + "ncData/"
    mv_dir = dirname + "mvData/"
    files = os.listdir(read_dir)

    #for file in glob.glob("*.txt"): #'*'은 모든 값을 의미
    for file in files:
        #print("#1 : ", file)
        #file = file.replace(" ", "_")
        #print("#2 : ", file)
        df = pd.read_csv(read_dir+file, encoding='CP949',delimiter=';')
        print("#3 : ", read_dir+file.replace(".txt","") + '.csv')
        df.to_csv(read_dir+file.replace("*.txt","") + '.csv')
        shutil.move(read_dir+file, mv_dir+file)

maketxttocsv("d:/tmp/makedir/")
#maketxttocsv("d:/Docs/05. 회사관련/05. 자료조사/14.데이터분석/한화HAS/수집자료/MT설비데이터/MT01/")
