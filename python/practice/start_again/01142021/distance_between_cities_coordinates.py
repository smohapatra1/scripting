#Distance Between Two Cities - [ Only Km and Miles ]
#Calculates the distance between two cities and allows the user to specify a unit of distance. 
#This program may require finding coordinates for the cities like latitude and longitude.

from pygeocoder import Geocoder
import numpy as np
import sys

def distance ( c1, c2):
    earth_rad = 6371.0
    dlat = np.deg2rad(c2[0] - c1[0])
    dlon = np.deg2rad(c2[1] - c1[1])
    a = np.sin(dlat/2) * np.sin(dlat/2) + np.cos(np.deg2rad(c1[0])) * np.cos(np.deg2rad(c2[0])) * np.sin(dlon/2) * np.sin(dlon/2)
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1-a))
    print (earth_rad * c)

def get_latlong (location):
    return Geocoder.geocode (location)[0].coordinates

def convert_km_to_miles(km):
    miles_per_km = 0.621
    return km * miles_per_km

def main():
    c1 = input("Enter City Name -  city1: ")
    c2 = input("Enter City Name -  city2: ")
    unit= str(input("Enter the conversion in km or miles: "))
    if unit in ['clicks', 'km', 'kilometers', 'kilometer']:
        unit = 'km'
    elif unit in ['m', 'mile','miles']:
        unit = 'm'
    else:
        print ("units is not recogniged, please try again")
    try:
        distance(get_latlong(c1),get_latlong(c2))
        if unit == 'km':
            print (str(distance), ' km')
        else:
            distance = convert_km_to_miles(km)
            print (str(distance), ' miles')
    except:
        print ("Error occored, Are the input cities correct ?")

if __name__ == "__main__":
    main()