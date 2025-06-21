def merge_three_dictionaries(dict1, dict2, dict3):
    # Your code goes here
    merged = {}
    
    for d in (dict1, dict2, dict3):
        for k, v in d.items():
            merged[k] = v
            
    return merged
    pass
