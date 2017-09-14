#!/usr/bin/python2.7

print "Content-type: text/html\n\n"
print "sdsf"

import pymongo
import cgitb
import re

from pymongo import MongoClient
from geoquery_queries import *  

try:
    client = MongoClient('localhost', 27017)
    print "\n**Connected successfully.**\n"
except pymongo.errors.ConnectionFailure, e:
    print "Could not connect: %s" % e

cgitb.enable()

db = client.asdf
collections = db.det

#print total_requests( collections )

#print get_organizations( collections )

#print get_emails( collections )

#print get_collections( collections )

#print get_boundaries( collections )

#print get_boundary_request_info( collections, 'Myanmar')

# for collection in collections.find():
#     print collection
#     raw_input()

# are they asking for ONLY count? what options are involved with count? is count also always with sum?
def raster_options():

    count=0
    only_count=0
    count_with_sum=0
    count_with_others=0
    count_with_others_no_sum=0

    for collection in collections.find():
        raster_data = collection['raster_data']

        for data in raster_data:
            options = data['options']['extract_types']
            if 'count' in options:
                count += 1
                if len(options) > 0:
                    if len(options) == 1:
                        only_count += 1
                    elif len(options) == 2:
                        if 'sum' in options:
                            count_with_sum += 1
                        else:
                            count_with_others_no_sum += 1
                    else:
                        if 'sum' in options:
                            count_with_others += 1
                        else:
                            count_with_others_no_sum += 1

    print count
    print "Requests"
    print "Only Count: %s" % only_count
    print "Count with Sum: %s" % count_with_sum
    print "Count with others (sum included): %s" % count_with_others
    print "count with others (no sum) %s" % count_with_others_no_sum

print raster_options()

def get_count_requests():
    count = 0  

    s = set()
    kv = {} # {user, # of times they asked for 'count'}
    count = 0
    for collection in collections.find():

        email = collection['email']
        raster_data = collection['raster_data']

        for data in raster_data:
            if 'count' in data['options']['extract_types']:
            #if len( data['options']['extract_types'] ) == 1 and data['options']['extract_types'][0] == 'count': #sole extract type
                release_data = collection['release_data']
                s.add( email.lower() ) # count unique users
                count += 1 # count number of 'count' requests

                for entry in release_data:
                    kv[ entry['dataset'] ] = kv.get( entry['dataset'], 0 ) + 1

    for k,v in sorted(kv.items(), key=lambda x:x[1], reverse=True):
        print k + ': ' + str(v) + ' requests.'

    print str(len(s)) + " unique users."
    print str(count) + " total requests."
