#4.외국인 비율이 3% 초과할 때만 출력해보기
import re, os, usecsv

os.chdir(r'D:\python_ws\do-it-python\04-04')
total = usecsv.opencsv('popSeoul.csv')
newPop = usecsv.switch(total)
i = newPop[1]

# for i in newPop:
#     foreign =0
#     try:
#         foreign = round(i[2]/(i[1]+i[2])*100, 1)
#         if foreign > 3:
#             print([i[0],i[1],i[2],foreign])
#     except:
#         pass
# #각 리스트의 네 번째 값인 외국인 비율이 전부 3보다 큼

new = [['구', '한국인', '외국인', '외국인 비율(%)']]    #new초기화
for i in newPop:
    foreign = 0
    try:
        foreign = round(i[2]/(i[1]+i[2])*100, 1)
        if foreign > 3:
            new.append([i[0],i[1],i[2],foreign])
    except:
        pass
#print(new)

#5.newPop.csv 파일로 저장하기
usecsv.writecsv('newPop.csv', new) 

#new객체가 제대로 생성되었다면 코드 한 줄로 csv 파일로 저장할 수 있음 :)