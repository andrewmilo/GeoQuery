#!/usr/bin/python2.7

"""get_count_requests.py: Gets the frequency of the 'count' selection in raster_data, and the related release datasets."""

import pymongo

from pymongo import MongoClient

try:
    client = MongoClient('localhost', 27017)
    print "\n**Connected successfully.**\n"
except pymongo.errors.ConnectionFailure, e:
    print "Could not connect: %s" % e

requests = client.asdf.det

count = 0  

s = set()
kv = {} # {user, # of times they asked for 'count'}
count = 0
for request in requests.find():

    email = request['email']
    raster_data = request['raster_data']

    for data in raster_data:
        if 'count' in data['options']['extract_types']:
        #if len( data['options']['extract_types'] ) == 1 and data['options']['extract_types'][0] == 'count': #sole extract type
            release_data = request['release_data']
            s.add( email.lower() ) # count unique users
            count += 1 # count number of 'count' requests

            for entry in release_data:
                kv[ entry['dataset'] ] = kv.get( entry['dataset'], 0 ) + 1

for k,v in sorted(kv.items(), key=lambda x:x[1], reverse=True):
    print k + ': ' + str(v) + ' requests.'

print str(len(s)) + " unique users."
print str(count) + " total requests."