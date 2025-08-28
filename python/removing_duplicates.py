# Given a list of numbers, remove all duplicates without using set().
def remove_duplicates(lst1):
    lst2=[]
    [lst2.append(i) for i in lst1 if i not in lst2]
    return lst2
# str.strip() is a string method that removes any leading and trailing whitespace from a string.
lst1 = list(map(str.strip, input("Enter values separated by commas: ").split(',')))
print(remove_duplicates(lst1))


# optimal one
# def remove_duplicates(lst1):
#     seen = {}
#     result = []
#     for i in lst1:                     # loop → runs n times
#         if i not in seen:              # dictionary lookup
#             seen[i] = True             # dictionary insert
#             result.append(i)           # list append
#     return result
