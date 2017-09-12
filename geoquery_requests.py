import pymongo
import sys

from pymongo import MongoClient
from geoquery_queries import *  

try:
    client = MongoClient('localhost', 27017)
    print "Connected successfully."
except pymongo.errors.ConnectionFailure, e:
    print "Could not connect: %s" % e
    sys.exit()

db = client.asdf
collections = db.det

print total_requests( collections )

print get_organizations( collections )

print get_emails( collections )

print get_collections( collections )