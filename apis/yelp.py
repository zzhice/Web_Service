from apis.yelpapi import YelpAPI
from pprint import pprint
import collections


def call_yelp(api_key, term="Chinese", location="umdearborn"):
    yelp_container = {'businesses':[]}

    yelp_api = YelpAPI(api_key)

    response = yelp_api.search_query(term=term, location=location, radius=40000,sort_by='rating', limit=10)

    yelp = response
    pprint(response)
    # print(yelp['businesses'][0]['id'])
    for i in range(len(yelp['businesses'])):
        new_dict = {}
        new_dict['name']=yelp['businesses'][i]['name']
        new_dict['id'] = yelp['businesses'][i]['id']
        if not yelp['businesses'][i]['location']['address1']:
            new_dict['location'] = 'NA'
        else:
            new_dict['location'] = yelp['businesses'][i]['location']['address1']
        if not yelp['businesses'][i]['rating']:
            new_dict['rating'] = 'NA'
        else:
            new_dict['rating'] = yelp['businesses'][i]['rating']
        if not yelp['businesses'][i]['distance']:
            new_dict['distance'] = 'NA'
        else:
            new_dict['distance'] = yelp['businesses'][i]['distance']
        yelp_container['businesses'].append(new_dict)

    # pprint(yelp_container)
    return yelp_container
    # print("id:{}".format(response['id']))


def call_review(api_key, location, record):
    yelp=record
    yelp_api = YelpAPI(api_key)

    new_response = ""
    response = yelp_api.search_query(location=location, radius=40000, sort_by='rating', limit=5)
    print("response:{}".format(response))
    for i in range(len(response['businesses'])):
        if str(response['businesses'][i]['name']) == str(location) or str(response['businesses'][i]['location']['address1']) == str(location):
            new_response = yelp_api.reviews_query(id=response['businesses'][i]['id'])

    # print(yelp['businesses'][0]['id'])
    for i in range(len(yelp['businesses'])):
        if(str(yelp['businesses'][i]['name']) == str(location)) or (str(yelp['businesses'][i]['location']) == str(location)):
            new_response = yelp_api.reviews_query(id=yelp['businesses'][i]['id'])

    pprint(new_response)
    return new_response


def call_autocomplete(api_key, text=""):
    # set default location to Dearborn area

    yelp_api = YelpAPI(api_key)

    response = yelp_api.autocomplete_query(text=text, longitude=42.3223, latitude=-83.1763)
    # pprint(response)
    return response

