import time
import os
import pandas

while True:
    if os.path.exists('files/temps_today.csv'):
        data = pandas.read_csv('files/temps_today.csv')
        dataF = data.mean()
        print(dataF)
        print(dataF['st1'])
    else:
        print('File does not exist')
    time.sleep(10)

