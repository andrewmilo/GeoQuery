#!/usr/bin/python2.7

"""geoquery_requests.py: Source file for the GeoQuery Requests Web Application."""

import pymongo
import json
import re
from geotext import GeoText
import geograpy
import unicodedata

from collections import defaultdict
from collections import Counter
from pymongo import MongoClient
from geoquery_queries import GeoQueryRequests
from copy import deepcopy

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
    raster_data = request['raster_data']
    if raster_data:
        for r in raster_data:
            name = r['name'] # name of dataset

            for v in country_list.values():
                for boundary in request['boundary'].values(): # search for matching country names
                    if v in boundary:
                        if not v in countries_with_datasets:
                            countries_with_datasets[v] = {}
                        countries_with_datasets[v][name] = countries_with_datasets[v].get(name, 0) + 1

for c, d in countries_with_datasets.items():
    print countries_with_datasets[c]
    countries_with_datasets[c] = [{'name': k, 'size': v} for k, v in d.iteritems()]
    print countries_with_datasets[c]
    raw_input()

for c, d in countries_with_datasets.iteritems():
    json_file['children'].append({'name': c, 'children': d})

with open('flare.json', 'w') as outfile:
    json.dump(json_file, outfile)