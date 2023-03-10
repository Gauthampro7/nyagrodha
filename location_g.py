def loco(place_name):
    from geopy.geocoders import Nominatim

    # create a Nominatim geolocator object
    geolocator = Nominatim(user_agent="my_app")

    
    

    # use the geolocator object to geocode the place name
    location = geolocator.geocode(place_name)

    # extract the latitude and longitude from the location object
    latitude = location.latitude
    longitude = location.longitude

    # convert the latitude and longitude to the desired format
    latitude_str = f"{abs(int(latitude))}n{int((latitude - abs(int(latitude))) * 60):02}"
    longitude_str = f"{abs(int(longitude))}e{int((longitude - abs(int(longitude))) * 60):02}"

    # combine the latitude and longitude strings to create the final coordinate string
    coordinate_str = f"{latitude_str} {longitude_str}"

    # print the final coordinate string
    return coordinate_str
