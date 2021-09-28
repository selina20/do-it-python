#<<<숫자 원소만 골라서 쉼표(,) 제거하기>>>
import os, usecsv

os.chdir(r'D:\python_ws\do-it-python\04-03')
total = usecsv.opencsv('popSeoul.csv')

#1.먼저 정규식 불러오기
import re 

i = total[2]  #total[2]에 있는 자료 하나를 불러옴
print(i)

k = []
for j in i:
    if re.search('\d', j): #j에 숫자가 있다면
        k.append(float(re.sub(',','',j))) #쉼표(,)를 삭제하고 실수형으로 바꿔 k에 저장
    else: #j에 숫자가 들어있지 않다면
        k.append(j) #k에 그대로 저장
print(k)
