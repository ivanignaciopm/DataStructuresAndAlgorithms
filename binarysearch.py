# It requires a sorted data set. O(log N)
# This is a recurisve approach 
def binary_search(sorted_list, left_pointer, right_pointer, target):
    
    # Base Case
    if left_pointer >= right_pointer:
        return "Value not found"
    
    # Mid value
    mid_idx = (left_pointer + right_pointer) // 2
    mid_val = sorted_list[mid_idx]
    
    if mid_val == target:
        return mid_idx
    
    if mid_val > target:
        return binary_search(sorted_list, left_pointer, mid_idx, target)
    
    if mid_val < target:
        return binary_search(sorted_list, mid_idx + 1, right_pointer, target)
        