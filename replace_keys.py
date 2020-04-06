def replace_keys(dct, old, new):
    """replace the keys of a nested dictionary matching a value with a new value 
    recursively"""

    output_dict = {}
    for k, v in dct.items():
        if k == old:
            k = new
        output_dict[k] = replace_keys(v, old, new) if isinstance(v, dict) else v
    return output_dict
