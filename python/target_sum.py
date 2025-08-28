# Given a list of integers, find the pair whose sum is closest to a given target.
def find_pair_closest_to_target(lst, target):
    lst.sort()  # Sort the list first

    left, right = 0, len(lst) - 1
    closest_pair = (None, None)
    closest_diff = float('inf')

    while left < right:
        current_sum = lst[left] + lst[right]
        current_diff = abs(current_sum - target)

        if current_diff < closest_diff:
            closest_diff = current_diff
            closest_pair = (lst[left], lst[right])

        if current_sum < target:
            left += 1
        else:
            right -= 1

    return closest_pair
lst = [10, 22, 28, 29, 30, 40]

target = 54
print(find_pair_closest_to_target(lst, target))
# Output: (22, 30)