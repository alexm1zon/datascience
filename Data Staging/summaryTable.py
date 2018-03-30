# importing libraries
from collections import Counter
import csv

# csv file name
filename = "Data Staging/csv/summaryTable.csv"

surrogateKeyID = 1

# array of words to omit
stopwords = ['and', 'in', 'than', 'by', 'at', 'is', 'the', 'of', 'a', 'as', 'were', 'with', 'or', 'to', 'was', 'into',
             'for', 'from', 'an', 'due']


def get_description_key(summary):
    key = -1
    global surrogateKeyID

    if (not summary == '') & isinstance(summary, basestring):
        querywords = summary.split()
        resultwords = [word for word in querywords if word.lower() not in stopwords]
        result = ' '.join(resultwords)
        keyword1 = Counter(result.split()).most_common(3)[0][0]
        keyword2 = Counter(result.split()).most_common(3)[1][0]

        if len(Counter(result.split()).most_common(3)) < 3:
            keyword3 = 'unknown'
        else:
            keyword3 = Counter(result.split()).most_common(3)[2][0]

        f = open(filename)
        reader = csv.DictReader(f)
        found = False

        for row in reader:
            if (row["summary"] == summary) & (row["keyword1"] == keyword1) & (row["keyword2"] == keyword2) & \
                    (row["keyword3"] == keyword3):

                key = row["description_key"]
                found = True
        f.close()

        if not found:
            with open(filename, 'ab') as ff:
                writer = csv.writer(ff)
                writer.writerow([surrogateKeyID, summary, keyword1, keyword2, keyword3])
            key = surrogateKeyID
            surrogateKeyID = surrogateKeyID + 1

    return key


