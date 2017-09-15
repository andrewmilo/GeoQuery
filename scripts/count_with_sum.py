#!/usr/bin/python2.7

"""count_with_sum.py: Gets the sum and percentages of the usage of 'count' with and without 'sum'."""

import pymongo

from pymongo import MongoClient

try:
    client = MongoClient('localhost', 27017)
    print "\n**Connected successfully.**\n"
except pymongo.errors.ConnectionFailure, e:
    print "Could not connect: %s" % e

requests = client.asdf.det
data = client.asdf.data

only_count = {}
only_count_with_sum_available = {}
count_with_sum = {}

#for x in requests.find({'raster_data.options.extract_types': 'count'}):
for request in requests.find():
    raster_data = request['raster_data']
    
    for r in raster_data:
        extract_types = r['options']['extract_types'] # the selection
        if 'count' in extract_types:
            #get dataset name/id to compare it to core_metadata
            name = r['name']
            #print name

            options = data.find_one({'name': name})
            if options:
                options = options['options']['extract_types_info'].keys()

                if 'sum' in options:
                    if 'sum' in extract_types: # part of selection
                        count_with_sum[name] = count_with_sum.get(name, 0) + 1
                    else: # not selected
                        only_count_with_sum_available[name] = only_count_with_sum_available.get(name, 0) + 1
                else: # not in options
                    only_count[name] = only_count.get(name, 0) + 1

total = sum(only_count_with_sum_available.values()) + sum(count_with_sum.values())

print float(sum(count_with_sum.values()))/float(total)
