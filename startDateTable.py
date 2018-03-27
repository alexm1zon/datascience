# importing libraries
from datetime import date
import csv

# csv file name
filename = "startDateTable.csv"

surrogateKeyID = 1


def get_key_id(day, month, year, weekend, season_canada, season_international):
    f = open(filename)
    reader = csv.DictReader(f)
    global surrogateKeyID

    for row in reader:
        if (row["day"] == day) & (row["month"] == month) & (row["year"] == year) & \
                (row["weekend"] == weekend) & (row["season_canada"] == season_canada):
                # (row["season_international"] == season_international)
            return row["date_key"]

    f.close()

    with open(filename, 'ab') as ff:
        writer = csv.writer(ff)
        writer.writerow([])
        writer.writerow([surrogateKeyID, day, month, year, weekend, season_canada, season_international])
    key = surrogateKeyID
    surrogateKeyID = surrogateKeyID + 1

    return key


def get_start_date_key(start_date):
    if (not start_date == '') & isinstance(start_date, basestring) & (not start_date == '0'):
        month, day, year = start_date[:-5].split("/")

        if 59 <= int(year) <= 99:
            new_year = '19' + year
        else:
            new_year = '20' + year

        my_date = date(int(new_year), int(month), int(day))

        if (my_date.weekday() == 5) | (my_date.weekday() == 6):
            weekend = 'yes'
        else:
            weekend = 'no'

        if ((month == '3') & (day >= '20')) | (month == '4') |\
            (month == '5') | ((month == '6') & (day < '21')):
            season_canada = 'spring'
        elif ((month == '6') & (day >= '21')) | (month == '7') | (month == '8') | ((month == '9') & (day < '22')):
            season_canada = 'summer'
        elif ((month == '9') & (day >= '22')) | (month == '10') | (month == '11') | ((month == '12') & (day < '21')):
            season_canada = 'fall'
        else:
            season_canada = 'winter'

        season_international = season_canada
       
        return get_key_id(day, month, year, weekend, season_canada, season_international)

    else:
        print("problem! ")
        print(start_date)

    return -1


