# importing libraries
import pandas as pd
import csv
from startDateTable import get_start_date_key

filenameSource = "CanadianDisasterDatabase.csv"
filenameFACT = "FACTtable.csv"

df = pd.DataFrame()

startDateKey = []
endDateKey = []
locationKey = []
disasterKey = []
descriptionKey = []
costKey = []
fatalities = []
injured = []
evacuated = []

f = open(filenameSource)
reader = csv.DictReader(f)

for row in reader:
        startDateKey.append(get_start_date_key(row["EVENT START DATE"]))
        # endDateKey.append(getenddatekey(row["EVENT END DATE"]))
        # locationKey.append(getlocationkey(row["PLACE"]))
        # disasterKey.append(getdisasterKey(row["EVENT TYPE"], row["EVENT SUBGROUP"],
        #                                   row["EVENT GROUP"], row["EVENT CATEGORY"],
        #                                   row["MAGNITUDE"], row["UTILITY - PEOPLE AFFECTED"]))
        # descriptionKey.append(getdescriptionkey(row["COMMENTS"]))
        # costKey.append(getstartdatekey(row["ESTIMATED TOTAL COST"], row["NORMALIZED TOTAL COST"],
        #                                row["FEDERAL DFAA PAYMENTS"], row["PROVINCIAL DFAA PAYMENTS"],
        #                                row["PROVINCIAL DEPARTMENT PAYMENTS"], row["INSURANCE PAYMENTS"],
        #                                row["MUNICIPAL COSTS"], row["INSURANCE PAYMENTS"],
        #                                row["OGC COSTS"], row["INSURANCE PAYMENTS"]))
        fatalities.append(row["FATALITIES"])
        injured.append(row["INJURED / INFECTED"])
        evacuated.append(row["EVACUATED"])

df.insert(loc=0, column='startDateKey', value=pd.Series(startDateKey))
df.insert(loc=1, column='endDateKey', value=pd.Series(endDateKey))
df.insert(loc=2, column='locationKey', value=pd.Series(locationKey))
df.insert(loc=3, column='disasterKey', value=pd.Series(disasterKey))
df.insert(loc=4, column='descriptionKey', value=pd.Series(descriptionKey))
df.insert(loc=5, column='costKey', value=pd.Series(costKey))
df.insert(loc=6, column='fatalities', value=pd.Series(fatalities))
df.insert(loc=7, column='injured', value=pd.Series(injured))
df.insert(loc=8, column='evacuated', value=pd.Series(evacuated))

df.to_csv(filenameFACT, encoding='utf-8', index=False)
