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
collections = db.det

#print total_requests( collections )

#print get_organizations( collections )

#print get_emails( collections )

#print get_collections( collections )

#print get_boundaries( collections )

#print get_boundary_request_info( collections, 'Myanmar')

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