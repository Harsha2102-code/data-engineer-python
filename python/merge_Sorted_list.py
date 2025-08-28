# Write a Python program to merge two sorted lists into one sorted list
def merge_sort(lst1,lst2):
    lst1.sort()
    lst2.sort()
    lst1.extend(lst2)
    lst1.sort()
    return lst1
lst1=list(map(int,input("Enter lst1 values seperated by comma:").split(',')))
lst2=list(map(int,input("Enter lst2 values seperated by comma:").split(',')))
print(merge_sort(lst1,lst2))

