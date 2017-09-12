# Retrivies the organization from a collection
def get_organization( collection ):
    return collection['org']

# Retrieves the email from a collection
def get_email( collection ):
    return collection['email']

# Returns a set of the data
def get_unique( dataset ):
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