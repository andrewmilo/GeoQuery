#!/usr/bin/python2.7

"""geoquery_requests.py: Source file for the GeoQuery Requests Web Application."""

import pymongo
import json

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

for d in data.find():
    name = d.get('name')
    if name == "dist_to_groads":
        print d