import googlemaps
from datetime import datetime
from pprint import pprint


def call_directions(api_key,location,end_location):

    gmaps = googlemaps.Client(key=api_key)

    now = datetime.now()
    directions_result = gmaps.directions(location,
                                     end_location,
                                        mode="driving",
                                     departure_time=now)
    pprint(directions_result)
    return directions_result