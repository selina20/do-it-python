import os,re,usecsv

os.chdir(r'D:\python_ws\do-it-python\realestate-apt')
apt = usecsv.switch(usecsv.opencsv('apt_202109.csv'))

# print(apt[:3])
# print("2021년 9월 아파트 거래 수 :", len(apt),"건")

#'시군구'만 출력
# for i in apt:
#     print(i[0])

#처음 5개 데이터의 '시군구'만 출력
# for i in apt[:5]:
#     print(i[0])

#'시군구','아파트 단지명', '거래금액(만원)' 출력
# for i in apt[:5]:
#     print(i[0],i[4],i[-4]) #i[-4] 는 오른쪽에서 4번째 원소를 뜻함


# #1) 경기도 김포에 103제곱미터 이상, 7억 이하 아파트 검색하기
for i in apt:
    try:
        #오류가 날 경우를 대비해 예외처리사용
        if i[5] >= 103 and i[-5] <= 70000 and re.match('경기도 김포', i[0]):
            print(i[0],i[4],i[-5])
    except: 
        pass

# #2) 부산에 103제곱미터 이상, 10억원 이하 롯데캐슬 아파트 검색하기
# for i in apt:
#     try:
#         #오류가 날 경우를 대비해 예외처리사용
#         if i[5] >= 103 and i[-5] <= 100000 and re.match('롯데캐슬', i[4]) and re.match('부산', i[0]):
#             print(i[0],i[4],i[-5])
#     except: 
#         pass

#분석 결과를 CSV 파일로 저장하기
new_list = []
for i in apt:
    try:
        if i[5] >= 103 and i[-5] <= 70000 and re.match('경기도 김포', i[0]):
            #앞에서 만든 조건을 그대로 입력
            new_list.append([i[0], i[4], i[-5]])
    except:
        pass

new_list.insert(0,['시군구','단지명','거래금액']) 

usecsv.writecsv('Gyeonggi_aptPrice(202109).csv', new_list)