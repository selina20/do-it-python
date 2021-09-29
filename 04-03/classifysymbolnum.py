import re

#특수문자와 숫자가 섞인 원소 골라내기
#첫번째 방법
# i = ['123!!','151,767','11,093','27,394'] #'123!!'이란 원소 추가
# k =[]

# for j in i:
#     if re.search('[a-z가-힣!]',j):  #search()함수에 느낌표(!) 추가
#         k.append(j)
#     else:
#         k.append(float(re.sub(',','',j)))
# print(k)


#두번째 방법
#k리스트를 따로 만들지 않고, 기존의 i 리스트에서 원소를 바로 변경하는 방법
i = ['123!!','151,767','11,093','27,394'] #'123!!'이란 원소 추가

for j in i:
    if re.search('[a-z가-힣!]',j):  #search()함수에 느낌표(!) 추가
        i[i.index(j)]=j
    else:
         i[i.index(j)]=float(re.sub(',','',j))
print(i)