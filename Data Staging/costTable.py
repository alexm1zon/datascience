# importing libraries
import csv

# csv file name
filename = "csv/costTable.csv"

surrogateKeyID = 1


def get_cost_key(estimated_total_cost, normalized_total_cost, federal_dfaa_payments,
                 provincial_dfaa_payments, provincial_payments, municipal_cost,  insurance_payments,
                 ogd_costs, ngo_payments):

    if estimated_total_cost == '0' and normalized_total_cost == '0':
        federal_dfaa_payments = '0'
        provincial_dfaa_payments = '0'
        provincial_payments = '0'
        municipal_cost = '0'
        insurance_payments = '0'
        ogd_costs = '0'
        ngo_payments = '0'

    else:
        if not estimated_total_cost:
            estimated_total_cost = 'unknown'
        if not normalized_total_cost:
            normalized_total_cost = 'unknown'
        if not federal_dfaa_payments:
            federal_dfaa_payments = 'unknown'
        if not provincial_dfaa_payments:
            provincial_dfaa_payments = 'unknown'
        if not provincial_payments:
            provincial_payments = 'unknown'
        if not municipal_cost:
            municipal_cost = 'unknown'
        if not insurance_payments:
            insurance_payments = 'unknown'
        if not ogd_costs:
            ogd_costs = 'unknown'
        if not ngo_payments:
            ngo_payments = 'unknown'

    f = open(filename)
    reader = csv.DictReader(f)
    key = -1
    found = False
    global surrogateKeyID

    for row in reader:
        if (row["estimated_total_cost"] == estimated_total_cost) & \
                (row["normalized_total_cost"] == normalized_total_cost) & \
                (row["federal_dfaa_payments"] == federal_dfaa_payments) & \
                (row["provincial_dfaa_payments"] == provincial_dfaa_payments) & \
                (row["provincial_payments"] == provincial_payments) & \
                (row["municipal_cost"] == municipal_cost) & \
                (row["insurance_payments"] == insurance_payments) & \
                (row["ogd_costs"] == ogd_costs) &\
                (row["ngo_payments"] == ngo_payments):

            key = row["costs_key"]
            found = True
    f.close()

    if not found:
        with open(filename, 'ab') as ff:
            writer = csv.writer(ff)
            writer.writerow([surrogateKeyID, estimated_total_cost, normalized_total_cost, federal_dfaa_payments,
                             provincial_dfaa_payments, provincial_payments, municipal_cost,  insurance_payments,
                             ogd_costs, ngo_payments])
        key = surrogateKeyID
        surrogateKeyID = surrogateKeyID + 1

    return key


