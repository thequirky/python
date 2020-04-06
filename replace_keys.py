def replace_keys(dct, old, new):
    """Replace the keys of a nested dictionary matching a value with a new value 
    recursively"""

    output_dict = {}
    for k, v in dct.items():
        k = new if k == old else k
        output_dict[k] = replace_keys(v, old, new) if isinstance(v, dict) else v
    return output_dict
