from geopy.geocoders import Nominatim
from geopy.geocoders import GoogleV3
import geocoder
import time
import csv
filename = "/Users/alexmizon/PycharmProjects/datascience/Data Staging/csv/locationTable.csv"

problems_count = 0
success_count = 0
total_count = 0
surrogateKeyID = 1


class Location:
    # variables
    problems_count = 0
    success_count = 0
    total_count = 0
    surrogateKeyID = 1

    @staticmethod
    def get_success_count():
        return success_count;

    @staticmethod
    def get_problems_count():
        return problems_count;

    @staticmethod
    def get_total_count():
        return total_count;

    @staticmethod
    def success():
        Location.success_count= Location.success_count + 1
        Location.total_count = Location.total_count + 1

    @staticmethod
    def problem():
        Location.problems_count=Location.problems_count + 1
        Location.total_count = Location.total_count + 1

    @staticmethod
    def get_key_id(city, province, country, inCanada, longitude, latitude):
        f = open(filename)
        reader = csv.DictReader(f)
        Location.surrogateKeyID
        for row in reader:
            if (row["city"] == city) & (row["province"] == province) & (row["country"] == country) & \
                    (row["inCanada"] == inCanada):
                return row["location_key"]
        f.close()

        with open(filename, 'ab') as ff:
            writer = csv.writer(ff)
            # writer.writerow([])
            writer.writerow([Location.surrogateKeyID, city, province, country, inCanada, longitude, latitude])
        Location.surrogateKeyID = Location.surrogateKeyID + 1
        return (Location.surrogateKeyID-1)

    @staticmethod
    def getLocationKey(location):

        if not location == '':
            time.sleep(0.9)
            geolocator = Nominatim(country_bias='CA')
            location = geolocator.geocode(location, addressdetails=True, exactly_one=True, timeout=10)
            if (not location is None):
                city = location.raw.get('address').get('city');
                if (city is not None):
                    city= city.encode('utf-8').strip();
                province = location.raw.get('address').get('state');
                if (province is not None):
                    province = province.encode('utf-8').strip();
                country = location.raw.get('address').get('country');
                if(country is not None):
                    country = country.encode('utf-8').strip();
                if country=='Canada':
                    inCanada='Yes'
                elif country is not None:
                    inCanada='No'
                else:
                    inCanada='Unknown'
                longitude = location.raw.get('lon')
                latitude = location.raw.get('lat')
                Location.success()
                return Location.get_key_id(city, province, country, inCanada, longitude, latitude)
            else:
                Location.problem()
                return -1
        else:
            Location.problem()
            return -1

            for x in range(len(places.cities)):
                print[places.cities[x]]
                print(places.cities.getitem(0))
        print('Hello World!');
        return 1;

#def getLocationKey1(location):

# geolocator = Nominatim(country_bias='CA')
# #location = geolocator.geocode("Balmoral and Val d'Amour areas in Restigouche County NB", addressdetails=True)
# listLoc = geolocator.geocode("", addressdetails=True, exactly_one=False,timeout=100)
# if not(listLoc is None):
#     print(type(listLoc))
#     print(len(listLoc))
#     for location in listLoc:
#         if (not (location is None)):
#             print(location._raw)
#             print(location.raw.get('display_name'))
#             longitude=location.raw.get('lon')
#             print(location.raw.get('lon'))
#             latitude=location.raw.get('lat')
#             print(location.raw.get('lat'))
#             city=location.raw.get('address').get('city');
#             print(city)
#             country=location.raw.get('address').get('country');
#             print(country)
#             state = location.raw.get('address').get('state');
#             print(state)

# g = GoogleV3(timeout=10, api_key='AIzaSyALLBrCS3OQtEBwM7XBaccpfCNco92nY4Q')
# listGoogleLoc = g.geocode(query="balmoral", exactly_one=False)


# g= geocoder.geonames(location='135 kenilworth', username='danoaudi', key='danoaudi', maxRows=1, timeout=100, countryBias='CA')

# print(len(g))
# 5
# for result in g:
#     print(result.address, result.latlng, result.population, result.country, result.province)

