# importing libraries
import pandas as pd
import csv
from dateTable import get_date_key
from disasterTable import get_disaster_key
from summaryTable import get_description_key
from costTable import get_cost_key
from clearTables import clear_tables
from locationMethod import Location

# clear data
clear_tables()

testMode = False; #will limit read to 50 rows

filenameSource = "csv/CanadianDisasterDatabase.csv"
filenameFACT = "csv/FACTtable.csv"

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
testModeCount = 0 ;
row_count=1;
for row in reader:
        print('On row#:'+ str(row_count))
        startDateKey_value = get_date_key(row["EVENT START DATE"])
        endDateKey_value = get_date_key(row["EVENT END DATE"])
        disasterKey_value = get_disaster_key(row["EVENT TYPE"], row["EVENT SUBGROUP"],
                                            row["EVENT GROUP"], row["EVENT CATEGORY"],
                                            row["MAGNITUDE"], row["UTILITY - PEOPLE AFFECTED"])
        descriptionKey_value = get_description_key(row["COMMENTS"])
        costKey_value = get_cost_key(row["ESTIMATED TOTAL COST"], row["NORMALIZED TOTAL COST"],
                                    row["FEDERAL DFAA PAYMENTS"], row["PROVINCIAL DFAA PAYMENTS"],
                                    row["PROVINCIAL DEPARTMENT PAYMENTS"],
                                    row["MUNICIPAL COSTS"], row["INSURANCE PAYMENTS"],
                                    row["OGD COSTS"], row["NGO PAYMENTS"])
        fatalities_value = row["FATALITIES"]
        injured_value = row["INJURED / INFECTED"]
        evacuated_value = row["EVACUATED"]
        locationKeys = Location.getLocationKeys(row["PLACE"])
        index = 0
        while index < len(locationKeys):
            startDateKey = startDateKey_value
            endDateKey = endDateKey_value
            locationKey = locationKeys[index]
            disasterKey= disasterKey_value
            descriptionKey = descriptionKey_value
            costKey = costKey_value
            fatalities = fatalities_value
            injured = injured_value
            evacuated = evacuated_value
            index = index + 1

        # testModeCount = testModeCount+1
        # if (testMode==True and testModeCount==50):
        #     break;
            
            with open(filenameFACT, 'ab') as ff:
                writer = csv.writer(ff)
                writer.writerow([startDateKey,endDateKey,locationKey,disasterKey,descriptionKey,
                                 costKey,fatalities,injured,evacuated])
        row_count+=1
# df.insert(loc=0, column='startDateKey', value=pd.Series(startDateKey))
# df.insert(loc=1, column='endDateKey', value=pd.Series(startDateKey))
# df.insert(loc=2, column='locationKey', value=pd.Series(locationKey))
# df.insert(loc=3, column='disasterKey', value=pd.Series(disasterKey))
# df.insert(loc=4, column='descriptionKey', value=pd.Series(descriptionKey))
# df.insert(loc=5, column='costKey', value=pd.Series(costKey))
# df.insert(loc=6, column='fatalities', value=pd.Series(fatalities))
# df.insert(loc=7, column='injured', value=pd.Series(injured))
# df.insert(loc=8, column='evacuated', value=pd.Series(evacuated))
# 
# df.to_csv(filenameFACT, encoding='utf-8', index=False)
# print(Location.get_success_count() + '=success')
# print(Location.get_problems_count() + '=problems')
# print(Location.get_total_count() + '=total')

