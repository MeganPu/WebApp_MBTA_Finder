import urllib.request
import json
from pprint import pprint

MAPQUEST_BASE_URL = "http://www.mapquestapi.com/geocoding/v1/address"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"

MAPQUEST_API_KEY = 'FjopzYjCGZVg2Z7qAWrFgkPGnMjw5Lgp'
MBTA_KEY='07c74aa5c40746f08920ea14b006a76f'

def get_json(url):
 
    f = urllib.request.urlopen(url)
    response_data = json.loads(f.read().decode('utf-8'))
    return response_data


def get_lat_long(place_name):
   
    place = place_name.replace(' ', '%20')
    url = f'{MAPQUEST_BASE_URL}?key={MAPQUEST_API_KEY}&location={place}'
    # print(url) # uncomment to test the url in browser
    place_json = get_json(url)
    # pprint(place_json)
    lat = place_json["results"][0]["locations"][0]['displayLatLng']['lat'] # modify this so you get the correct latitude
    lon = place_json["results"][0]["locations"][0]['displayLatLng']['lng'] # modify this so you get the correct longitude

    return lat,lon


def get_nearest_station(latitude, longitude,route_type):
    
#	Choose the type of transportation used on a route. Valid options are:
# 0 - Tram, Streetcar, Light rail. 
# 1 - Subway, Metro. 
# 2 - Rail. 
# 3 - Bus. 
# 4 - Ferry. 
# 5 - Cable tram. 
# 6 - Aerial lift, suspended cable car (e.g., gondola lift, aerial tramway). 
# 7 - Funicular. 
# 11 - Trolleybus. 
# 12 - Monorail. 
    url = f'{MBTA_BASE_URL}?api_key={MBTA_KEY}&filter[latitude]={latitude}&filter[longitude]={longitude}&sort=distance&route_type={route_type}&radius=0.08'
    # print(url) # uncomment to test the url in browser
    station_json = get_json(url)
    # pprint(station_json) # uncomment to see the json data
    station_name = station_json["data"][0]['attributes']['name'] 
    # print(station_name) # uncomment to check it0

    # try to find out where the wheelchair_boarding information is
    wheelchair_boarding = station_json["data"][0]['attributes']['wheelchair_boarding']

    return station_name, wheelchair_boarding

def find_stop_near(place_name,route_type):
    return get_nearest_station(*get_lat_long(place_name),route_type)

def main():
    # final test here
    place = input('Enter a place name in Boston such as "Fenway Park": ')
    route_type=input('RouteType:')
    lat,lon = get_lat_long(place)
    print(lat,lon)
    print(get_nearest_station(lat,lon,route_type))

    # final wrap-up
    print(find_stop_near(place,route_type))


if __name__ == '__main__':
    main()
    