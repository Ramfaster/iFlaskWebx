# since 2019-09-04
# author : Ramfaster
# Description
# 필요 Util
import re
import sys
import io

class MakeUtils:

    def cleanText(readData):
        #스팸 메세지에 포함되어 있는 특수 문자 제거
        text = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]', '', readData)
        #양쪽(위,아래)줄바꿈 제거
        text = text.strip('\n')
        return text
