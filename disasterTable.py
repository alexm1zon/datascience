# importing libraries
import pandas as pd
import numpy as np

# csv file name
filenameFrom = "CanadianDisasterDatabase.csv"
filenameTo = "disasterTable.csv"

df = pd.read_csv(filenameFrom)
df1 = pd.DataFrame()

df1['disaster_key'] = df['ID']
df1['disaster_type'] = df['EVENT TYPE']
df1['disaster_subgroup'] = df['EVENT SUBGROUP']
df1['disaster_group'] = df['EVENT GROUP']
df1['disaster_category'] = df['EVENT CATEGORY']
df1['magnitude'] = np.where(df['MAGNITUDE'].isnull(), '0.0', df['MAGNITUDE'])
df1['utility_people_affected'] = np.where(df['UTILITY - PEOPLE AFFECTED'].isnull(), '0', df['UTILITY - PEOPLE AFFECTED'])

df1.to_csv(filenameTo, encoding='utf-8', index=False)
