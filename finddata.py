import json


database = "data.json"
data = json.loads(open(database).read())

find_major = input("전공 검색 : ")

print("검색 결과 :")
for i in range(len(data)):
    if data[str(i)]['major'] == find_major:
        print(str(i + 1) + ".", data[str(i)]['univ'], data[str(i)]['major'], data[str(i)]['type'], str(data[str(i)]['grade']))