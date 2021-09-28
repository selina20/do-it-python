import csv, os
os.chdir(r'D:\python_ws\do-it-python\04-02')
f = open('a.csv','r')

new = csv.reader(f)
new

a_list = [] #csv형 리스트로 바꾸기 위해 임의이 객체 (a_list)를 하나 만듬

for i in new:
    print(i)
    a_list.append(i) #a_list에 i를 한 행씩 차례로 저장

#a_list #객체에 값이 텅 비었음. 왜? new객체에 저장하면서 커서가 맨 마지막으로 이동했기때문에
f.seek(0) # 다시 파일을 처음부터 일기 위해 seek()함수를 사용해 커서 이동해주기
a_list

