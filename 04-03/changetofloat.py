import os,re
import usecsv

os.chdir(r'D:\python_ws\do-it-python\04-03')
total = usecsv.opencsv('popSeoul.csv')

for i in total[:5]:
    print(i)

#문자형 자료를 숫자로형으로 바꾸기
i = '123'
float(i)
int(i)

#'1,468,146'은 숫자형으로 직접 바꿀 수 없음. 세 자릿수마다 있는 쉼표(,)때문에
float('1,468,146')

#먼저 re.sub()함수를 사용해 쉼표(,) 제거
j  = '1,468,146'
float(re.sub(',','',j)) #쉼표를 빈 문자열로 대체

type(float(re.sub(',','',j))) #실수형인지 다시 확인

