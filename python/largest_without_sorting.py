# Given a list of integers, find the second largest element without sorting
# def find_second_largest(lst):
#     lst.remove(max(lst))
#     print(max(lst))
    
# lst=[1,2,10,6,4,9,7]
# find_second_largest(lst)

# without modyfying list

def second_largest(lst):
    max_val = max(lst)
    lst_copy = [x for x in lst if x != max_val]  # avoid mutating original
    return max(lst_copy)

  
lst=[1,2,3,6,4,10,9]
print(second_largest(lst))
