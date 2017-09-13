import pymongo

import re
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

count = 0

users = get_emails( collections )    

s = set()
kv = {} # {user, # of times they asked for 'count'}
count = 0
for collection in collections.find():
    email = collection['email']
    raster = collection['raster_data']

    # print collection.keys()
    print collection['release_data']

    if len(raster) > 0:
        if 'count' in raster[0]['options']['extract_types']:
            country = collection['boundary']['title'].split(' ')[0]
            #title = raster[0]['title']
            title = collection['boundary']['title']
            kv[ title ] = kv.get( title, 0 ) + 1
            #count += 1
            #s.add( str(email).lower() )
       # if len(raster[0]['options']['extract_types']) == 1 and 'count' == raster[0]['options']['extract_types'][0]:
            #count +=1
            #s.add( str(email).lower() )
            #kv[ email ] = kv.get( email, 0 ) + 1
    # print collection['raster_data'][:]
    # print "\n\n\n"
    #if 'count' in collection['raster_data']['options']['extract_types']:
    #    count+=1
    #for info in collection['raster_data']:
        #for k,v in info.iteritems():
            #print k
        #if 'count' in info['options']['extract_types']:
        #    pass
            #s.add( str(email).lower() )
            #kv[ email.lower() ] = kv.get( email.lower(), 0 ) + 1
        # if len(info['options']['extract_types']) == 1 and 'count' == info['options']['extract_types'][0]:
        #     s.add( str(email).lower() )
        #     count += 1
    

# for key in sorted(kv.iterkeys()):
#     print "%s: %s requests." % (key, kv[key])

# for k,v in sorted(kv.items(), key=lambda x:x[1], reverse=True):
#     print k + ': ' + str(v) + ' results.'
# for k,v in kv.iteritems():
#     print k + ': ' + str(v) + ' requests.'
#print len(kv)
# print sum(kv.values())
print len(s)
print count

#print collections.find().count() #1970
