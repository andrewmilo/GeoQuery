#!/usr/bin/python2.7

"""geoquery_requests.py: Source file for the GeoQuery Requests Web Application."""

import pymongo
import json

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

children = []

for d in data.find():
    name = d.get('name')
    if name:
        count = rq.get_request_count_for_dataset(name)
        child = {"name": name, "requests": count}
        children.append(child)

print children

# for r in requests.find():
#     ra = r['raster_data']
#     for d in ra:
#         for da in data.find({'name': d.get('name')}):
#             print d.get('name')
        
#         print 'Total: {0} VS {1}'.format(data.count(), data.find({'name': d.get('name')}).count())