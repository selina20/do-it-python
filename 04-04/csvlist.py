import os, re, usecsv

os.chdir(r'D:\python_ws\do-it-python\04-04')
total = usecsv.opencsv('popSeoul.csv')
newPop = usecsv.switch(total) #newPop라는 새 객체를 만들어 분석에 사용
print(newPop[:4]) #확인을 위해 앞 원소 4개만 출력해 봄

#코딩을 할 때는 '가장 기본적인 단위'에서부터 시작하고,
#그것이 확실해졌을 때 반복하는 것이 중요함


#1.등록외국인 비율 계산하기
i = newPop[1]
print(i)    #2017년 서울에는 내국인 약 974만명, 외국인 28만명 거주

i[2] / (i[1]+i[2])*100  #전체 인구 대비 외국인 비율 계산. i[2]=외국인 거주 수, i[1]=내국인 거주 수
foreign = round(i[2]/(i[1]+i[2])*100, 1) #약2.84% round()함수에서 '(,1)'은 소수점 첫째 자리까지만 foreign 객체에 저장하는 것을 의미
print(foreign)  #2.8


#2.각 구의 외국인 비율 출력하기
# for i in newPop:
#     foreign = 0
# #한 번 반복하고 나면 foreign을 다시 지정해야 하므로 foreign을 0으로 먼저 지정

#     try:
#         foreign = round(i[2]/(i[1]+i[2])*100, 1)
#         print(i[0], foreign)
#     #i[0]에는 구 이름이 저장되어 있고, foreign은 공식대로 계산한 외국인 비율
#     except:
#         pass

#     #혹시 오류가 생길 경우를 대비해
#     #오류가 생기면 그냥 지나가라는 예외 조항을 만들어둠

#3.첫 행 지정하기
new = [['구', '한국인', '외국인', '외국인 비율(%)']]
print(i)
new.append([i[0],i[1],i[2],foreign])
print(new)
