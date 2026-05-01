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


# optimal one- 2 pointer approach
def merge_sort(lst1,lst2):
    i, j = 0, 0
    merged = []
    
    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            merged.append(lst1[i])
            i += 1
        else:
            merged.append(lst2[j])
            j += 1
    
    # Append remaining elements
    merged.extend(lst1[i:])
    merged.extend(lst2[j:])
    
    return merged
lst1=list(map(int,input("Enter lst1 values seperated by comma:").split(',')))
lst2=list(map(int,input("Enter lst2 values seperated by comma:").split(',')))
print(merge_sort(lst1,lst2))