import csv, os
os.chdir(r'D:\python_ws\do-it-python\04-02')

def opencsv(filename):
    f = open(filename,'r')
    reader = csv.reader(f)
    output = []
    for i in reader:
        output.append(i)
    return output
    f.close()


opencsv('example2.csv')
