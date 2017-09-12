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
    """Get frequency of a field value from a list of collections.
    
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
    emails = []
    
    for collection in dbcollections.find():
        emails.append( collection['email'])

    return emails

def total_requests( dbcollections ):
    return dbcollections.count()

def get_organizations( dbcollections ):

    orgs = set()
    blacklist = ['gmail.com', 'yahoo.com', 'hotmail.com']

    for collection in dbcollections.find():
        org = str(collection['email']).split('@')[1]
        if org.lower() not in blacklist:
            orgs.add( org )
    
    return orgs

def get_collections( dbcollections ):
    return dbcollections.find()