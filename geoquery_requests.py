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

emails = []
for collection in collections.find():
    emails.append(collection['email'])

    #for entry in str(collection).split(','):
    #    print entry
    #print "ENDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDd\n"

for email in get_unique(emails):
    print get_frequency('email', email, collections.find())