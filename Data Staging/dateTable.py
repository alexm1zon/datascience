# importing libraries
from datetime import date
import csv

# csv file name
filename = "csv/dateTable.csv"

surrogateKeyID = 1


def get_key_id(day, month, year, weekend, season_canada):
    f = open(filename)
    reader = csv.DictReader(f)
    global surrogateKeyID

    for row in reader:
        if (row["day"] == day) & (row["month"] == month) & (row["year"] == year) & \
                (row["weekend"] == weekend) & (row["season_canada"] == season_canada):
            return row["date_key"]

    f.close()

    with open(filename, 'ab') as ff:
        writer = csv.writer(ff)
        writer.writerow([surrogateKeyID, day, month, year, weekend, season_canada])
    key = surrogateKeyID
    surrogateKeyID = surrogateKeyID + 1

    return key


def get_date_key(start_date):
    if (start_date == '') | (not isinstance(start_date, basestring)) | (start_date == '0'):
        day = None
        month = None
        year = None
        weekend = None
        season_canada = None

    else:
        year, new_month, new_day = start_date.split("-")
        month = int(new_month)
        day = int(new_day)

        my_date = date(int(year), int(month), int(day))

        if (my_date.weekday() == 5) | (my_date.weekday() == 6):
            weekend = 'yes'
        else:
            weekend = 'no'

        if ((month == 3) & (day >= 20)) | (month == 4) |\
            (month == 5) | ((month == 6) & (day < 21)):
            season_canada = 'spring'
        elif ((month == 6) & (day >= 21)) | (month == 7) | (month == 8) | ((month == 9) & (day < 22)):
            season_canada = 'summer'
        elif ((month == 9) & (day >= 22)) | (month == 10) | (month == 11) | ((month == 12) & (day < 21)):
            season_canada = 'fall'
        else:
            season_canada = 'winter'


    return get_key_id(day, month, year, weekend, season_canada)




