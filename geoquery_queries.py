def get_field( field, document ):
    """Get a field from a document.
    
    Args:
        field: the field.
        document: the document.
    Returns:
        value of the field in the document.
    """
    return document[field]

def compress( dataset ):
    """Compress values to 1 of each.
    
    Args:
        dataset: set of data.
    Returns:
        set with 1 of each value.
    """
    return set( dataset )

def get_frequency( field, value, collections ):
    """Get frequency of a field value from requests.
    
    Args:
        field: field to identify.
        value: sought after value of field.
        collections: list of collections.
    Returns:
        count of the occurence of the value.
    """
    count = 0
    for collection in collections:
        if collection[field] == value:
            count += 1
    
    return count

def get_emails( dbcollections ):
    """Get emails from requests.
    
    Args:
        dbcollections: all collections from database.
    Returns:
        list of emails
    """
    emails = []
    
    for collection in dbcollections.find():
        emails.append( collection['email'])

    return emails

def total_requests( dbcollections ):
    """Get total number of requests from the requests.
    
    Args:
        dbcollections: all collections from database.
    Returns:
        number of requests
    """
    return dbcollections.count()

def get_organizations( dbcollections ):
    """Get organizations from the requests.
    
    Args:
        dbcollections: all collections from database.
    Returns:
        list of organizations
    """
    orgs = set()
    blacklist = ['gmail.com', 'yahoo.com', 'hotmail.com']

    for collection in dbcollections.find():
        org = str(collection['email']).split('@')[1]
        if org.lower() not in blacklist:
            orgs.add( org )
    
    return orgs

def get_collections( dbcollections ):
    """Get collections from database.
    
    Args:
        dbcollections: all collections from database.
    Returns:
        list of collections
    """
    return dbcollections.find()
def get_boundaries( dbcollections ):
    """Get all boundaries from the requests.
    
    Args:
        dbcollections: all collections from database.
    Returns:
        list of boundaries
    """
    ret = []
    for collection in dbcollections.find():
        ret.append(collection['boundary']['title'])
    return ret

def get_boundary_request_info( dbcollections, boundary ):
    """Get request information for a boundary.
    
    Args:
        dbcollections: all collections from database.
        boundary: country/region
    Returns:
        list containing (# of times the boundary has been requested, map of {info requested about boundary, # of times this info was requested}).
    """
    ret = []
    count = 0
    infokv = {}
    for collection in dbcollections.find():
        if collection['boundary']['title'].split(' ')[0] == boundary:
            count += 1
            for field in collection['raster_data']:
                info = field['title']
                infokv[ info ] = infokv.get( info, 0 ) + 1 # count number of times this info has been requested
                
                #return years with number of times requested in those years
    
    ret.append( count )
    ret.append( infokv )

    return ret
    