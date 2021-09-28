import csv, os, re
#새롭게 시작할 때 csv모듈을 먼저 임포트 한다

def opencsv(filename):
    f = open(filename,'r')
    reader = csv.reader(f)
    output = []
    for i in reader:
        output.append(i)
    return output
    f.close()
#opencsv() 함수에서는 f를 파일 객체로 해 직접 open하는 방식을 사용했음

def writecsv(filename, the_list):
    with open(filename, 'w', newline = '') as f :
        a = csv.writer(f, delimiter = ',')
        a.writerows(the_list)
#writecsv() 함수에서는 with문을 사용해 코드 길이가 조금 더 짦음

#test.csv파일 만들어보기
import usecsv
os.chdir(r'D:\python_ws\do-it-python\04-02')
a = [['국어','영어','수학'],[99,88,77]]
usecsv.writecsv('test.csv',a)

