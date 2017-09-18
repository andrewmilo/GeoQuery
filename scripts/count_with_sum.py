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
count_with_all_options = {}
count_with_other_options = {}
count_1 = {} # only count selected with some other options available
#count_2 = {} # only count selected with ALL other options available


TOTAL_OPTIONS = 5

for request in requests.find():
    raster_data = request['raster_data']
    
    for r in raster_data:
        extract_types = r['options']['extract_types'] # the selection
        if 'count' in extract_types:
            # get dataset name/id to compare it to core_metadata
            name = r['name']

            options = data.find_one({'name': name}) # find unique dataset name
            if options:
                #options = options['options']['extract_types_info'].keys()
                options = options['options']['extract_types']
                
                if len(extract_types) == 1: # only 'count' selected
                    if len(options) > 1:
                        count_1[name] = count_1.get(name, 0) + 1
                elif len(extract_types) > 1: # if more than just 'count' selected
                    if len(extract_types) == len(options): # all options selected
                        count_with_all_options[name] = count_with_all_options.get(name, 0) + 1
                        
                    count_with_other_options[name] = count_with_other_options.get(name, 0) + 1 # 'count' with other options selected

                if 'sum' in options:
                    if 'sum' in extract_types: # part of selection
                        count_with_sum[name] = count_with_sum.get(name, 0) + 1
                    else: # not selected
                        only_count_with_sum_available[name] = only_count_with_sum_available.get(name, 0) + 1
                else: # not in options
                    only_count[name] = only_count.get(name, 0) + 1 # sum not included, however others may be included
            else:
                print "Could not find: {0}".format(name)

total_count_1 = sum(count_1.values())
#total_count_2 = sum(count_2.values())
total_count_with_sum = sum(count_with_sum.values())
total_only_count_with_sum_available = sum(only_count_with_sum_available.values())
total_count_with_all_options = sum(count_with_all_options.values())
total_count_with_other_options = sum(count_with_other_options.values())

total = total_count_with_sum + total_only_count_with_sum_available
total2 = total_count_with_all_options + total_only_count_with_sum_available
total3 = total_count_1 + total_count_with_other_options
total4 = total_count_1 + total_count_with_all_options

#print "Total of count selected alone: {0}".format(total_count)
print "Total of count with sum included: {0}".format(total_count_with_sum)
print "Total of only count with sum available in options: {0}".format(total_only_count_with_sum_available)
print "Total of count with other options: {0}".format(total_count_with_other_options)
print "Total of count with all other options: {0}".format(total_count_with_all_options)
print "Percentage of count with sum: {0}% ".format(float(total_count_with_sum)/float(total)*100)
print "Percentage of other options being included when count is selected: {0}%".format(float(total_count_with_other_options)/float(total3)*100)
print "Percentage of ALL options being included when count is selected: {0}%".format(float(total_count_with_all_options)/float(total4)*100)