#!/usr/bin/python2.7

"""get_raster_data_options.py: Gets the frequency of the 'count' selection in raster_data."""

import pymongo

from pymongo import MongoClient

try:
    client = MongoClient('localhost', 27017)
    print "\n**Connected successfully.**\n"
except pymongo.errors.ConnectionFailure, e:
    print "Could not connect: %s" % e

requests = client.asdf.det

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

print "{0} total requests".format(count)
print "Only Count: %s" % only_count
print "Count with Sum: %s" % count_with_sum
print "Count with others (sum included): %s" % count_with_others
print "count with others (no sum) %s" % count_with_others_no_sum