def remove_duplicates(lst):
    unique_list = []
    for item in lst:
        # Check if the item is already in the unique_list
        if item not in unique_list:
            unique_list.append(item)
    return unique_list
