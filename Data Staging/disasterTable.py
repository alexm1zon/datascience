# importing libraries
import csv

# csv file name
filename = "csv/disasterTable.csv"

surrogateKeyID = 1


def get_disaster_key(event_type, subgroup, group, category, magnitude, people_affected):
    if not event_type:
        event_type = None
    if not subgroup:
        subgroup = None
    if not group:
        group = None
    if not category:
        category = None
    if not magnitude:
        magnitude = None
    if not people_affected:
        people_affected = None

    f = open(filename)
    reader = csv.DictReader(f)
    key = -1
    found = False
    global surrogateKeyID

    for row in reader:
        if (row["event_type"] == event_type) & (row["subgroup"] == subgroup) & (row["group"] == group) & \
                (row["category"] == category) & (row["magnitude"] == magnitude) & \
                (row["people_affected"] == people_affected):

            key = row["disaster_key"]
            found = True
    f.close()

    if not found:
        with open(filename, 'ab') as ff:
            writer = csv.writer(ff)
            writer.writerow([surrogateKeyID, event_type, subgroup, group, category, magnitude, people_affected])
        key = surrogateKeyID
        surrogateKeyID = surrogateKeyID + 1

    return key


