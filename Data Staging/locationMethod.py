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
    def get_key_id(city, province, country, inCanada, longitude, latitude,location_description, queryString, city_pop):
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
            writer.writerow([Location.surrogateKeyID, city, province, country, inCanada, longitude, latitude, location_description, queryString, city_pop])
        Location.surrogateKeyID = Location.surrogateKeyID + 1
        return (Location.surrogateKeyID-1)

    @staticmethod
    def getLocationKeys(location_string):
        population = 0
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
        keys = [None] #* len(areas)
        index = 0 ;
        while index < len(areas):
            pop_loc = Location.getLocationKey(areas[index])
            if(not (pop_loc == -1)):
                population = population + int(pop_loc[0])
                for location_key in pop_loc[1]:
                    keys.append(location_key)
            index = index + 1
        return [population,keys]

    @staticmethod
    def getLocationKey(location_string):
        location_keys = [None]
        population = 0 ;
        if location_string == '':
            return -1

        #check if query has already been sent
        f = open(filename)
        reader = csv.DictReader(f)
        for row in reader:
            if (row["queryString"]==location_string):
                result_key = row["location_key"]
                pop = int(row["city_pop"])
                f.close()
                location_keys.append(result_key)
                return [pop, location_keys];
        f.close()

        #check if this api call had been already made with an empty return
        if Location.check_if_unsuccessful_query(location_string):
            return -1

        #wait at least 1 second between consecutive api calls to Nominatim
        # if(time.time() - Location.start_time) < 1:
        #     time.sleep(1.5 - (time.time() - Location.start_time))
        #     Location.start_time=time.time();

        #use geolocator to analyse the place string
        #start
        g = geocoder.geonames(location=location_string, username='danoaudi', key='danoaudi', maxRows=4, timeout=10,
                              countryBias='CA')
        if(len(g)==0):
            Location.add_unsuccessful_query(location_string)
            return -1

        g = sorted(g, key=lambda object1: object1.population, reverse=True)
        higherlevel =False;
        code = g[0].code
        if(code=='PCLI' or code=='ADM1'):
            population =int(g[0].population)
            higherlevel=True;


        if(higherlevel):
            for result in g:
                if (result.code == 'PCLI' or result.code == 'ADM1'):
                    continue
                city = result.address.encode('utf-8').strip();
                province = result.province.encode('utf-8').strip();
                country = result.country.encode('utf-8').strip();
                latitude = result.latlng[0]
                longitude = result.latlng[1]
                inCanada= 'Yes'
                if(not result.country=='Canada'):
                    inCanada = 'No'
                location_description = result.description.encode('utf-8').strip();
                city_pop=result.population
                location_keys.append(Location.get_key_id(city, province, country, inCanada, longitude, latitude, location_description,location_string, city_pop))
        else:
            result=g[0]
            city = result.address
            if(city is not None):
                city = result.address.encode('utf-8').strip();
            province = result.province
            if(province is not None):
                province = result.province.encode('utf-8').strip();
            country = result.country
            if(country is not None):
                country = result.country.encode('utf-8').strip();
            latitude = result.latlng[0]
            longitude = result.latlng[1]
            inCanada= 'Yes'
            if(not result.country=='Canada'):
                inCanada = 'No'
            location_description = result.description
            if(location_description is not None):
                location_description = result.description.encode('utf-8').strip();
            population = int(result.population)
            city_pop = int(result.population)
            location_keys.append(Location.get_key_id(city, province, country, inCanada, longitude, latitude, location_description,location_string,city_pop))

        return [int(population), location_keys]

        #
        #
        #
        # #end
        # geolocator = Nominatim(country_bias='CA')
        # location = geolocator.geocode(location_string, addressdetails=True, exactly_one=True, timeout=10)
        # if not location is None:
        #     city = location.raw.get('address').get('city');
        #     if (city is not None):
        #         city= city.encode('utf-8').strip();
        #     province = location.raw.get('address').get('state');
        #     if (province is not None):
        #         province = province.encode('utf-8').strip();
        #     country = location.raw.get('address').get('country');
        #     if(country is not None):
        #         country = country.encode('utf-8').strip();
        #     if country=='Canada':
        #         inCanada='Yes'
        #     elif country is not None:
        #         inCanada='No'
        #     else:
        #         inCanada='Unknown'
        #     longitude = location.raw.get('lon')
        #     latitude = location.raw.get('lat')
        #     Location.success()
        #     return Location.get_key_id(city, province, country, inCanada, longitude, latitude, location_string)
        # else:
        #     Location.add_unsuccessful_query(location_string)
        #     Location.problem()
        #     return -1;


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



#pop = geocoder.geonames().population('Springfield, Virginia')

#def getLocationKey1(location):

# geolocator = Nominatim(country_bias='CA')
# location = geolocator.geocode("Balmoral and Val d'Amour areas in Restigouche County NB", addressdetails=True)
# listLoc = geolocator.geocode("Northern Ontario", addressdetails=True, exactly_one=True,timeout=100)
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
#
#
# g= geocoder.geonames(location='Yukon', username='danoaudi', key='danoaudi', maxRows=10, timeout=100, countryBias='CA')
#
# print(len(g))
# 5
# g=sorted(g, key=lambda object1: object1.population, reverse=True)
# for result in g:
#     if(not result.code=='ADM154'):
#         print(result.address, result.latlng, result.population, result.country, result.province, result.class_description, result.code, result.description)

