#-*- coding: utf-8 -*-

# 파일명 양식 : 학교명-전형명-학과명-평균내신등급.txt
# 자기소개서의 각 문항은 "\n"으로 구분되어있음 -> readlines 이용

import json
from collections import OrderedDict
import os

jagi_data = OrderedDict()

index = 0

# 자기소개서 text file -> json
for root, subdirs, files in os.walk('/Users/soo/PycharmProjects/jagi/database/txtfile'):
    for file in files:
        full_fname = os.path.join(root, file)
        s = os.path.splitext(full_fname)  # 확장자명 제거
        s = os.path.split(s[0])           # 파일명에서 정보 추출
        elements = s[1].split('-')

        info = {'univ': elements[0], 'type': elements[1], 'major': elements[2], 'grade': float(elements[3])}

        with open(full_fname, 'r', encoding='euc-kr') as f:
            innerIndex = 1
            lines = f.readlines()

            selfIntro = {}

            for line in lines:
                if line is "\n" or None or "":
                    continue
                line = line.strip()
                selfIntro[innerIndex] = line
                innerIndex += 1

            info['self-intro'] = selfIntro
        jagi_data[index] = info
        index += 1

print(json.dumps(jagi_data, ensure_ascii=False, indent="\t"))
