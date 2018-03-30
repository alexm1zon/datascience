# importing libraries
import csv

# csv file name
filename = "csv/costTable.csv"

surrogateKeyID = 1


def get_cost_key(estimated_total_cost, normalized_total_cost, federal_dfaa_payments,
                 provincial_dfaa_payments, provincial_payments, municipal_cost,  insurance_payments,
                 ogd_costs, ngo_payments):
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

            key = row["cost_key"]
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


