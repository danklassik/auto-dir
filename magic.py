import os
import pandas
path = os.getcwd()
Data = pandas.read_excel('./dirs.xls', sheet_name='Лист1')
class col:
    good = '\033[94m'
    bad = '\033[91m'
for row in Data.iterrows():
    newdir = (str(path)+"\\"+str(row[1][0])+"\\"+str(row[1][1]))
    try:
        os.makedirs(str(newdir))
        print(col.good + "Создал: "+str(path)+"\\"+str(row[1][0])+"\\"+str(row[1][1]))
    except:
        print(col.bad + "Проблема в: " + str(path) + "\\" + str(row[1][0]) + "\\" + str(row[1][1]))