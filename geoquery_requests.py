#!/usr/bin/python2.7

"""geoquery_requests.py: Source file for the GeoQuery Requests Web Application."""

import pymongo
import json
import re
from geotext import GeoText
import geograpy
import unicodedata

from pymongo import MongoClient
from geoquery_queries import GeoQueryRequests

try:
    client = MongoClient('localhost', 27017)
    print "\n**Connected successfully.**\n"
except pymongo.errors.ConnectionFailure, e:
    print "Could not connect: %s" % e

db = client.asdf
requests = db.det
data = db.data

rq = GeoQueryRequests(requests)

json_file = {'name': 'flare', 'children': []}
name = "flare"

with open('countries.json') as data_file:    
    country_list = json.load(data_file)

countries_with_datasets = {}

for request in requests.find():
    countries = set()
    for v in country_list.values():
        for boundary in request['boundary'].values():
            if v in boundary:
                countries_with_datasets[v] = {}
                countries.add(v)

    raster_data = request['raster_data']
    if raster_data:
        for r in raster_data:
            name = r['name'] # name of dataset
            for country in countries:
                countries_with_datasets[country][name] = countries_with_datasets[country].get(name, 0) + 1
                child = {"name": name, "size": 1}
                combo = {'name': country, 'children': [{'name': name}]}
                json_file['children'].append(combo)
                #json_file['children'].append(child)

    countries_with_datasets[country][name] = countries_with_datasets[country].get(name, 0) + 1
    child = {"name": name, "size": 1}
    combo = {'name': country, 'children': [{'name': name}]}
    json_file['children'].append(combo)

with open('data.txt', 'w') as outfile:
    json.dump(countries_with_datasets, outfile)

    #print countries

# for r in requests.find():
#     # t = GeoText(str(r['boundary']))
#     t = geograpy.get_place_context(text=str(r['boundary']))
#     countries = t.countries
#     if countries:
#         pass#print countries
#     else:
#         if len(t.other) == 0 and len(t.regions) == 0:
#             print r['boundary']
        #print t.other
    # if not countries:
    #     print r['boundary']
    #     print countries
    # print countries
    # if len(countries) > 1:
    #     print r
#     t = GeoText(str(r))
#     countries = t.country_mentions
#     if len(countries) > 1:
#         print countries
#         print r
#     raw_input()

# for d in data.find():
#     t = GeoText(str(d))
#     countries = t.country_mentions
#     if len(countries) > 1:
#         print countries
#         print d
#     # for x in t.country_mentions:
#     #     print x
#     # print '\n\n'
#     raw_input()
    # if t:
    #     if not('ADM1' in t or 'ADM2' in t or 'ADM3' in t or 'ADM4' in t or 'ADM5' in t):
    #         #print t[0:t.index('ADM1')]
    #         print t
    #     country = d.get('country')
    #n = d.get('name')
    # children = []
    # if n:
    #     count = rq.get_request_count_for_dataset(n)
    #     if count != 0:
            # child = {"name": n, "size": count}
            # json_file['children'].append(child)

# print json_file

with open('flare.json', 'w') as outfile:
    json.dump(json_file, outfile)