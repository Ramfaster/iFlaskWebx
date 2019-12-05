import pandas as pd
import numpy as np
import os
import sys
import glob


def readDataSet():

    # csv 파일 위치
    read_path = r"d:/tmp/makedir/ncData"

    # 변수 선언
    wkTime, aufnr, eqmtCd, toolno = [], [], [], []
    globbed_files = glob.glob(read_path + "/*.txt.csv")  # creates a list of all csv files
    dfs = pd.DataFrame()
    li = []
    # 컬럼명 정의
    cols = ['Timestamp', 'ToolNumber', 'RPM', 'FeedSpeed', 'RPMOverride', 'FeedOverride', 'SpindleLoad', 'X-Load',
            'Y-Load', 'Z-Load', 'B-Load', 'A-Load']

    for file in globbed_files:
        #    print("test" , file)
        df = pd.read_csv(file, encoding='CP949', delimiter=';')
        li.append(df)

    dfs = pd.concat(li, axis=0, ignore_index=True)
    print(dfs[0].head())