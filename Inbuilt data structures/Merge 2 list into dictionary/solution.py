def merge_lists_to_dictionary(keys, values):
    # Your code goes here
    dictionary = {}
    
    if len(keys) != len(values):
        return False
    
    for k in range(len(keys)):
        dictionary[keys[k]] = values[k]
        
    return dictionary
    pass
