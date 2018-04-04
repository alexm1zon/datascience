from geopy.geocoders import Nominatim
from geopy.geocoders import GoogleV3
from timeit import default_timer
import time
import geocoder
import csv
filename = "csv/locationTable.csv"
unsuccessful_queries_csv = "csv/location_queries_none_return.csv"
previous_results = "csv/locationQueries.csv"
prairie_provinces  = ['Alberta', 'Saskatchewan', 'Manitoba']
PROVINCE_CODES = ['NL', 'PE', 'NS', 'NB', 'QC', 'ON', 'MB', 'SK', 'AB', 'BC', 'YT', 'NT', 'NU']


class Location:
    # variables
    PROVINCE_CODES = ['NL', 'PE', 'NS', 'NB', 'QC', 'ON', 'MB', 'SK', 'AB', 'BC', 'YT', 'NT', 'NU']
    problems_count = 0
    success_count = 0
    total_count = 0
    surrogateKeyID = sum(1 for line in open(filename))
    firstRun = False;
    start_time = time.time()

    @staticmethod
    def get_success_count():
        return Location.success_count;

    @staticmethod
    def get_problems_count():
        return Location.problems_count;

    @staticmethod
    def get_total_count():
        return Location.total_count;

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
            if (((row["city"] == city) or (row["city"]=="" and (city is None))) & \
                    ((row["province"] == province) or (row["province"]=="" and (province is None))) & \
                    (row["country"] == country) & \
                    (row["inCanada"] == inCanada)):
                return row["location_key"]
        f.close()

        with open(filename, 'ab') as ff:
            writer = csv.writer(ff)
            writer.writerow([Location.surrogateKeyID, city, province, country, inCanada, longitude, latitude])
        Location.surrogateKeyID = Location.surrogateKeyID + 1
        return (Location.surrogateKeyID-1)

    @staticmethod
    def getLocationKeys(location_string):
        if (location_string == 'Prairie Provinces'):
            keys = [None]*len(prairie_provinces)
            index=0
            while index<len(prairie_provinces):
                keys[index]=Location.getLocationKey(prairie_provinces[index])
                index+=1
        # locate the areas in the string that need to be split
        location_string = location_string.replace(", and ", "_ss_")
        location_string = location_string.replace(" and ", "_ss_")
        location_string = location_string.replace(",", "_ss_")

        # separate into different string
        areas = location_string.split("_ss_")
        words_in_last = areas[-1].split()
        last_word = words_in_last[-1]

        # check for provinces in common between areas
        if last_word in Location.PROVINCE_CODES:
            province_code = last_word;
            areas.reverse();
            index = 0
            while index < len(areas):
                areas[index] = areas[index].strip();
                if (index == 0):
                    index = index + 1;
                    continue;
                word = (areas[index].split())[-1];
                if word not in Location.PROVINCE_CODES:
                    areas[index] = areas[index] + ' ' + province_code;
                index = index + 1;
            areas.reverse()
        keys = [None] * len(areas)
        index = 0 ;
        while index < len(areas):
            keys[index] = Location.getLocationKey(areas[index])
            index = index + 1
        return keys

    @staticmethod
    def getLocationKey(location_string):

        if location_string == '':
            return -1

        #check if query has already been sent
        f = open(filename)
        reader = csv.DictReader(f)
        for row in reader:
            if (row["queryString"]==location_string):
                result_key = row["location_key"]
                f.close()
                return result_key;
        f.close()

        #check if this api call had been already made with an empty return
        if Location.check_if_unsuccessful_query(location_string):
            return -1

        #wait at least 1 second between consecutive api calls to Nominatim
        if(time.time() - Location.start_time) < 1:
            time.sleep(1.5 - (time.time() - Location.start_time))
            Location.start_time=time.time();

        #use geolocator to analyse the place string
        geolocator = Nominatim(country_bias='CA')
        location = geolocator.geocode(location_string, addressdetails=True, exactly_one=True, timeout=10)
        if not location is None:
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
            Location.add_unsuccessful_query(location_string)
            Location.problem()
            return -1;


    @staticmethod
    def check_if_unsuccessful_query(location_string):
        f = open(unsuccessful_queries_csv)
        reader = csv.DictReader(f)
        Location.surrogateKeyID
        for row in reader:
            if(row["queryString"]==location_string):
                f.close()
                return True
        f.close()
        return False

    @staticmethod
    def add_unsuccessful_query(location_string):
        with open(unsuccessful_queries_csv, 'ab') as ff:
            writer = csv.writer(ff)
            writer.writerow([location_string])


#def getLocationKey1(location):

# geolocator = Nominatim(country_bias='CA')
# #location = geolocator.geocode("Balmoral and Val d'Amour areas in Restigouche County NB", addressdetails=True)
# listLoc = geolocator.geocode("Ontario", addressdetails=True, exactly_one=False,timeout=100)
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
#             print(type(city))
#             print(city is None)
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

