import csv

a = [['구','전체','내국인','외국인'],
['관악구','519864','502089','17775'],
['강남구','547602','542498','5104'],
['송파구','686181','679247','56934'],
['강동구','428547','424235','4312']]

f = open('abc.csv','w',newline='') #새 csv파일을 쓰기모드(w)로 열기

csvobject = csv.writer(f, delimiter=',')
csvobject.writerows(a) #csv형 리스트가 저장된 객체를 --> 파일에 쓸 때는 writerows() 사용함
f.close()
