def remove_duplicates(lst):
    # Your code goes here
    unique = []
    
    for i in range(len(lst)):
        found = False
        for j in range(i):
            if lst[i] == lst[j]:
                found = True
                break
            
        if not found:
            unique.append(lst[i])
                
    return unique
    pass
