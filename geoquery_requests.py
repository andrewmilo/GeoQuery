#!/usr/bin/python2.7

"""geoquery_requests.py: Source file for the GeoQuery Requests Web Application."""

import pymongo
import json
import re

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

for d in data.find():
    t = d.get('title')
    print d
    print '\n\n'
    # if t:
    #     if not('ADM1' in t or 'ADM2' in t or 'ADM3' in t or 'ADM4' in t or 'ADM5' in t):
    #         #print t[0:t.index('ADM1')]
    #         print t
    #     country = d.get('country')
#     n = d.get('name')
#     children = []
#     if n:
#         count = rq.get_request_count_for_dataset(n)
#         if count != 0:
#             child = {"name": n, "size": count}
#             json_file['children'].append(child)

# print json_file

# with open('flare.json', 'w') as outfile:
#     json.dump(json_file, outfile)

# for k in children:
#     print k['name']

# for r in requests.find():
#     ra = r['raster_data']
#     for d in ra:
#         for da in data.find({'name': d.get('name')}):
#             print d.get('name')
        
#         print 'Total: {0} VS {1}'.format(data.count(), data.find({'name': d.get('name')}).count())