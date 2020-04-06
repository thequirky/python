def flatten(lst):
    """flatten a list of lists"""
    
    return [item for sublist in lst for item in sublist]
