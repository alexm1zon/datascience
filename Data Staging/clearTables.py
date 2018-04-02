import csv

filenameFACT = "/Users/alexmizon/PycharmProjects/datascience/Data Staging/csv/FACTtable.csv"
filenameDisaster = "/Users/alexmizon/PycharmProjects/datascience/Data Staging/csv/disasterTable.csv"
filenameDate = "/Users/alexmizon/PycharmProjects/datascience/Data Staging/csv/dateTable.csv"
filenameSummary = "/Users/alexmizon/PycharmProjects/datascience/Data Staging/csv/summaryTable.csv"
filenameCost = "/Users/alexmizon/PycharmProjects/datascience/Data Staging/csv/costTable.csv"
# filenameLocation = "Data Staging/csv/locationTable.csv"

file_names = [filenameFACT, filenameDisaster, filenameDate, filenameSummary, filenameCost]


def clear_tables():
    # clear existing CSV
    for the_files in file_names:
        f = open(the_files, "w+")
        f.close()

    # create fact header
    with open(filenameFACT, 'wb') as outcsv:
        writer = csv.writer(outcsv)
        writer.writerow(['date_key','location_key', 'disaster_key', 'description_key', 'costs_key', 'fatalities', 'injured',
                         'evacuated'])

    # create cost header
    with open(filenameCost, 'wb') as outcsv:
        writer = csv.writer(outcsv)
        writer.writerow(
            ['costs_key','estimated_total_cost', 'normalized_total_cost', 'federal_dfaa_payments',
             'provincial_dfaa_payments', 'provincial_payments', 'municipal_cost', 'insurance_payments',
             'ogd_costs', 'ngo_payments'])

    # create disaster header
    with open(filenameDisaster, 'wb') as outcsv:
        writer = csv.writer(outcsv)
        writer.writerow(['disaster_key', 'event_type', 'subgroup', 'group', 'category', 'magnitude', 'people_affected'])

    # create summary header
    with open(filenameSummary, 'wb') as outcsv:
        writer = csv.writer(outcsv)
        writer.writerow(['description_key', 'summary', 'keyword1', 'keyword2', 'keyword3'])

    # create date header
    with open(filenameDate, 'wb') as outcsv:
        writer = csv.writer(outcsv)
        writer.writerow(
            ['date_key','day', 'month', 'year', 'weekend', 'season_canada', 'season_international'])

    ## create location header
    # with open(filenameLocation, 'wb') as outcsv:
    #     writer = csv.writer(outcsv)
    #     writer.writerow(
    #         [])