# importing libraries
import pandas as pd
import numpy as np

# csv file name
filenameFrom = "CanadianDisasterDatabase.csv"
filenameTo = "costTable.csv"

df = pd.read_csv(filenameFrom)
df1 = pd.DataFrame()

df1['costs_key'] = df['ID']
df1['estimated_total_cost'] = np.where(df['ESTIMATED TOTAL COST'].isnull(), '0', df['ESTIMATED TOTAL COST'])
df1['normalized_total_cost'] = np.where(df['NORMALIZED TOTAL COST'].isnull(), '0', df['NORMALIZED TOTAL COST'])
df1['federal_payments'] = np.where(df['FEDERAL DFAA PAYMENTS'].isnull(), '0', df['FEDERAL DFAA PAYMENTS'])
df1['provincial_DFAA_payments'] = np.where(df['PROVINCIAL DFAA PAYMENTS'].isnull(), '0', df['PROVINCIAL DFAA PAYMENTS'])
df1['provincial_department_payments'] = np.where(df['PROVINCIAL DEPARTMENT PAYMENTS'].isnull(), '0', df['PROVINCIAL DEPARTMENT PAYMENTS'])
df1['insurance_payments'] = np.where(df['INSURANCE PAYMENTS'].isnull(), '0', df['INSURANCE PAYMENTS'])
df1['municipal_cost'] = np.where(df['MUNICIPAL COSTS'].isnull(), '0', df['MUNICIPAL COSTS'])
df1['insurance_payments'] = np.where(df['INSURANCE PAYMENTS'].isnull(), '0', df['INSURANCE PAYMENTS'])
df1['ogd_cost'] = np.where(df['OGD COSTS'].isnull(), '0', df['OGD COSTS'])
df1['ngo_payments'] = np.where(df['INSURANCE PAYMENTS'].isnull(), '0', df['INSURANCE PAYMENTS'])

df1.to_csv(filenameTo, encoding='utf-8', index=False)
