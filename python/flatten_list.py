# Implement a function to flatten a nested list (e.g., [1, [2, [3, 4]], 5] → [1, 2, 3, 4, 5]).
def flatten(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list): #check if item is list
            flat_list.extend(flatten(item))  # Recursively flatten the sublist
        else:
            flat_list.append(item)
    return flat_list
nested_list = [1, [2, [3, 4]], 5]
print(flatten(nested_list))