# -*- coding: utf-8 -*-

# 파일명 양식 : 학교명-전형명-학과명-평균내신등급.txt
# 자기소개서의 각 문항은 "\n"으로 구분되어있음 -> readlines 이용


from collections import OrderedDict
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')


# 자기소개서 text file -> dictionary -> DB


def introductions_to_dict():

    jagi_data = OrderedDict()
    index = 0

    for root, subdirs, files in os.walk('database/txtfile'):
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

    return jagi_data


if __name__=='__main__':
    django.setup()
    from app_jagi.models import CoverLetter  # 빨간줄 무시하셈

    j = introductions_to_dict()
    for i in range(len(j)):
        CoverLetter(school_name=j[i]['univ'],
                    major=j[i]['major'],
                    type=j[i]['type'],
                    grade=j[i]['grade'],
                    question1=j[i]['self-intro'][1],
                    question2=j[i]['self-intro'][2],
                    question3=j[i]['self-intro'][3],
                    question4=j[i]['self-intro'][4],
                    ).save()
