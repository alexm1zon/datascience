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
        pop_loc = Location.getLocationKeys(row["PLACE"])

        if(pop_loc is None):
            locationKeys = [-1]
            population = None
        else:
            population = pop_loc[0]
            locationKeys = pop_loc[1]
            hasPop = True ;

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
            population = population

            with open(filenameFACT, 'ab') as ff:
                writer = csv.writer(ff)
                writer.writerow([startDateKey,endDateKey,locationKey,disasterKey,descriptionKey,
                                 costKey,fatalities,injured,evacuated,population])
        row_count+=1

