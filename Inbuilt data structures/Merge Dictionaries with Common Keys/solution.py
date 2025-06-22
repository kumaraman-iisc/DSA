def merge_dicts_with_overlapping_keys(dicts):
    # Your code goes here
    merge = {}
    
    for d in dicts:
        for k, v in d.items():
            if k in merge:
                merge[k] += v
                
            else:
                merge[k] = v

    return merge
    pass
