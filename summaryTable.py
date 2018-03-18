# importing libraries
import pandas as pd
from collections import Counter

# csv file name
filenameFrom = "CanadianDisasterDatabase.csv"
filenameTo = "summaryTable.csv"

df = pd.read_csv(filenameFrom)
df1 = pd.DataFrame()

df1['summary_key'] = df['ID']
df1['summary'] = df['COMMENTS']

#array of words to omit
stopwords = ['and', 'in', 'than', 'by', 'at', 'is', 'the', 'of', 'a', 'as', 'were', 'with', 'or', 'to', 'was']
keyword1 = []
keyword2 = []
keyword3 = []

for row in df['COMMENTS']:
    if (not row == '') & isinstance(row, basestring):
        querywords = row.split()
        resultwords = [word for word in querywords if word.lower() not in stopwords]
        result = ' '.join(resultwords)
        print(Counter(result.split()).most_common(3))
        keyword1.append(Counter(result.split()).most_common(3)[0][0])
        keyword2.append(Counter(result.split()).most_common(3)[1][0])
        if len(Counter(result.split()).most_common(3)) < 3:
            keyword3.append('unknown')
        else :
            keyword3.append(Counter(result.split()).most_common(3)[2][0])

df1.insert(loc=2, column='keyword1', value=pd.Series(keyword1))
df1.insert(loc=3, column='keyword2', value=pd.Series(keyword2))
df1.insert(loc=4, column='keyword3', value=pd.Series(keyword3))

df1.to_csv(filenameTo, encoding='utf-8', index=False)
