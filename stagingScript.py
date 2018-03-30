# importing libraries
import pandas as pd
import csv
from dateTable import get_date_key
from disasterTable import get_disaster_key
from summaryTable import get_description_key
from costTable import get_cost_key

filenameSource = "csv/CanadianDisasterDatabase.csv"
filenameFACT = "csv/FACTtable.csv"

df = pd.DataFrame()

dateKey = []
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
        dateKey.append(get_date_key(row["EVENT START DATE"]))
        dateKey.append(get_date_key(row["EVENT END DATE"]))
        # locationKey.append(getlocationkey(row["PLACE"]))
        disasterKey.append(get_disaster_key(row["EVENT TYPE"], row["EVENT SUBGROUP"],
                                            row["EVENT GROUP"], row["EVENT CATEGORY"],
                                            row["MAGNITUDE"], row["UTILITY - PEOPLE AFFECTED"]))
        descriptionKey.append(get_description_key(row["COMMENTS"]))
        costKey.append(get_cost_key(row["ESTIMATED TOTAL COST"], row["NORMALIZED TOTAL COST"],
                                    row["FEDERAL DFAA PAYMENTS"], row["PROVINCIAL DFAA PAYMENTS"],
                                    row["PROVINCIAL DEPARTMENT PAYMENTS"],
                                    row["MUNICIPAL COSTS"], row["INSURANCE PAYMENTS"],
                                    row["OGD COSTS"], row["NGO PAYMENTS"]))
        fatalities.append(row["FATALITIES"])
        injured.append(row["INJURED / INFECTED"])
        evacuated.append(row["EVACUATED"])

df.insert(loc=0, column='dateKey', value=pd.Series(dateKey))
df.insert(loc=1, column='locationKey', value=pd.Series(locationKey))
df.insert(loc=2, column='disasterKey', value=pd.Series(disasterKey))
df.insert(loc=3, column='descriptionKey', value=pd.Series(descriptionKey))
df.insert(loc=4, column='costKey', value=pd.Series(costKey))
df.insert(loc=5, column='fatalities', value=pd.Series(fatalities))
df.insert(loc=6, column='injured', value=pd.Series(injured))
df.insert(loc=7, column='evacuated', value=pd.Series(evacuated))

df.to_csv(filenameFACT, encoding='utf-8', index=False)
