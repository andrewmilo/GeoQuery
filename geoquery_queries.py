#!/usr/bin/python2.7

"""geoquery_queries.py: Queries for the GeoQuery Requests Web Application."""

def get_field(field, document):
    """Get a field from a document.
    
    Args:
        field: the field.
        document: the document.
    Returns:
        value of the field in the document.
    """
    return document[field]

def compress(dataset):
    """Compress values to 1 of each.
    
    Args:
        dataset: set of data.
    Returns:
        set with 1 of each value.
    """
    return set(dataset)

def get_frequency(field, value, requests):
    """Get frequency of a field value from requests.
    
    Args:
        field: field to identify.
        value: sought after value of field.
        requests: list of requests.
    Returns:
        count of the occurence of the value.
    """
    count = 0
    for request in requests:
        if request[field] == value:
            count += 1
    
    return count

def get_emails(requests):
    """Get emails from requests. 
    
    Args:
        requests: all requests from database.
    Returns:
        list of emails - not guaranteed to be a unique list.
    """
    emails = []
    
    for request in requests.find():
        emails.append(request['email'])

    return emails

def unique_users(requests):
    """Get emails from requests. 
    
    Args:
        requests: all requests from database.
    Returns:
        list of unique users.
    """
    uniq = set()
    for request in requests.find():
        email = str(request['email']).lower()
        uniq.add(email)
    
    return uniq

def total_requests(requests):
    """Get total number of requests from the requests.
    
    Args:
        requests: all requests from database.
    Returns:
        number of requests
    """
    return requests.count()

def requests_per_user(requests):
    """Get amount of requests submitted per user. 
    
    Args:
        requests: all requests from database.
    Returns:
        count of requests per user
    """
    kv = {}

    for request in requests.find():
        email = str(request['email']).lower() # doesn't consider unicode comparison
        kv[email] = kv.get(email, 0) + 1
    
    return kv

def selections_per_user_request(requests):
    """Get amount of selected datasets per user. 
    
    Args:
        requests: all requests from database.
    Returns:
        total selection made by each user
    """
    sel = {}
    for request in requests.find():
        email = str(request['email']).lower()
        raster_data = request['raster_data']
        sel[email] = sel.get(email, 0) + len(raster_data)
    
    return sel

def get_organizations(requests):
    """Get organizations from the requests.
    
    Args:
        requests: all requests from database.
    Returns:
        list of organizations
    """
    orgs = set()
    blacklist = ['gmail.com', 'yahoo.com', 'hotmail.com']

    for request in requests.find():
        org = str(request['email']).split('@')[1]
        if org.lower() not in blacklist:
            orgs.add( org )
    
    return orgs

def get_requests(requests):
    """Get requests from database.
    
    Args:
        requests: all requests from database.
    Returns:
        list of requests
    """
    return requests.find()

def get_boundary_count(requests):
    """Get count of boundaries. 
    
    Args:
        requests: all requests from database.
    Returns:
        boundaries are their frequency
    """
    boundaries = {}
    for request in requests.find():
        boundary = request['boundary']['title']
        boundaries[boundary] = boundaries.get(boundary,0) + 1

    return boundaries

def get_boundaries(requests):
    """Get all boundaries from the requests.
    
    Args:
        requests: all requests from database.
    Returns:
        list of boundaries
    """
    ret = []
    for request in requests.find():
        ret.append(request['boundary']['title'])
    return ret

def get_boundary_request_info(requests, boundary):
    """Get request information for a boundary.
    
    Args:
        requests: all requests from database.
        boundary: country/region
    Returns:
        list containing (# of times the boundary has been requested, map of {info requested about boundary, # of times this info was requested}).
    """
    ret = []
    count = 0
    infokv = {}
    for request in requests.find():
        if request['boundary']['title'].split(' ')[0] == boundary:
            count += 1
            for field in request['raster_data']:
                info = field['title']
                infokv[ info ] = infokv.get( info, 0 ) + 1 # count number of times this info has been requested
                
                #return years with number of times requested in those years
    
    ret.append(count)
    ret.append(infokv)

    return ret