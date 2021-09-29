import re

#문자와 숫자가 섞인 원소 골라내기

p = ['123강남', '151,767','11,093','27,394'] #'123강남'이라는 원소 추가
k = []

# for j in p:
#     if re.search('\d', j):
#         k.append(float(re.sub(',','',j)))
#     else:
#         k.append(j)
#
#이렇게 할 경우, 오류남
#'123강남'은 숫자가 포함되어 있지만 float()함수로 바꿀수 없기때문에

for j in p:
    if re.search('[a-z가-힣]',j): #알파벳 또는 한글이 있다면 그대로 k에 저장
        k.append(j)
    else:
        k.append(float(re.sub(',','',j)))

print(k)