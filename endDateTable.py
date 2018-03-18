# importing libraries
import pandas as pd
import numpy as np
from datetime import date

# csv file name
filenameFrom = "CanadianDisasterDatabase.csv"
filenameTo = "endDateTable.csv"

df = pd.read_csv(filenameFrom)
df1 = pd.DataFrame()

df1['data_key'] = df['ID']
df1[['month','day','year']] = df['EVENT END DATE'].str.split('/',expand=True)
df1['year'] = df1['year'].map(lambda x: str(x)[:-5])  # remove time left corresponding to last 5 characters

weekend = []

for row in df['EVENT END DATE']:
        if (not row == '') & isinstance(row, basestring):
            month, day, year = row[:-5].split("/")
            if 59 <= year <= 99:
                newYear = '19' + year
            else:
                newYear = '20' + year

            mydate = date(int(newYear), int(month), int(day))

            if (mydate.weekday() == 5) | (mydate.weekday() == 6):
                weekend.append('yes')
            else:
                weekend.append('no')
        else:
            weekend.append('no')

df1.insert(loc=4, column='weekend', value=pd.Series(weekend))

conditions = [
    ((df1['month'] == '3') & (df1['day'] >= '20')) | (df1['month'] == '4') | (df1['month'] == '5') |
    ((df1['month'] == '6') & (df1['day'] < '21')),
    ((df1['month'] == '6') & (df1['day'] >= '21')) | (df1['month'] == '7') | (df1['month'] == '8') |
    ((df1['month'] == '9') & (df1['day'] < '22')),
    ((df1['month'] == '9') & (df1['day'] >= '22')) | (df1['month'] == '10') | (df1['month'] == '11') |
    ((df1['month'] == '12') & (df1['day'] < '21')),
    ((df1['month'] == '12') & (df1['day'] >= '21')) | (df1['month'] == '1') | (df1['month'] == '2') |
    ((df1['month'] == '3') & (df1['day'] < '20'))]

choices = ['spring', 'summer', 'fall', 'winter']

df1['season_canada'] = np.select(conditions, choices)

# df1['season_international'] = TODO

df1.to_csv(filenameTo, encoding='utf-8', index=False)
