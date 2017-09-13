import pymongo

from pymongo import MongoClient
from geoquery_queries import *  

try:
    client = MongoClient('localhost', 27017)
    print "Connected successfully."
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

for collection in collections.find():
    print collection['custom_name']