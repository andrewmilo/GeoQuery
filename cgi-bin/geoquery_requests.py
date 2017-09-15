#!/usr/bin/python2.7
import pymongo

import re

from pymongo import MongoClient
from geoquery_queries import *  

try:
    client = MongoClient('localhost', 27017)
    print "\n**Connected successfully.**\n"
except pymongo.errors.ConnectionFailure, e:
    print "Could not connect: %s" % e

db = client.asdf
requests = db.det
data = db.data

#print total_requests( requests )

#print get_organizations( requests )

#print get_emails( requests )

#print get_requests( requests )

#print get_boundaries( requests )

#print get_boundary_request_info( requests, 'Myanmar')

# for k, v in selections_per_user_request( requests ).iteritems():
#     print "{0} : {1}".format(k, v) 

for request in requests.find():
    print request
    print "\n\n\n"
    raw_input()

# for dataset in data.find():
#     print dataset
#     print "\n\n"

def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    return str(raster_options())

# are they asking for ONLY count? what options are involved with count? is count also always with sum?
def raster_options():

    count=0
    only_count=0
    count_with_sum=0
    count_with_others=0
    count_with_others_no_sum=0

    for request in requests.find():
        raster_data = request['raster_data']

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

    return (count,only_count,count_with_sum, count_with_others, count_with_others_no_sum)
    print count
    print "Requests"
    print "Only Count: %s" % only_count
    print "Count with Sum: %s" % count_with_sum
    print "Count with others (sum included): %s" % count_with_others
    print "count with others (no sum) %s" % count_with_others_no_sum

#print raster_options()

def get_count_requests():
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
