import usecsv,re,os

os.chdir(r'D:\python_ws\do-it-python\04-03')
total = usecsv.opencsv('popSeoul.csv')
#print(total)

#i = total[1]
#print(i)

for i in total:
    for j in i:
        try:
            i[i.index(j)] = float(re.sub(',','',j))

        except:
            pass

print(total)