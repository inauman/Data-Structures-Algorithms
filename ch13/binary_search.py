'''
Time Complexity: O(log(n))
'''

import math
def binary_search(arr, search_value):
    lower_bound = 0
    upper_bound = len(arr) - 1

    while lower_bound <= upper_bound:
        mid_point_index = math.floor((lower_bound + upper_bound)/2)
        
        value_at_mid_point = arr[mid_point_index]
    
        if value_at_mid_point == search_value:
            return search_value
        elif search_value < value_at_mid_point:
            upper_bound = mid_point_index - 1
        elif search_value > value_at_mid_point:
            lower_bound = mid_point_index + 1

    return "No match found"

print(binary_search([1,2,3,4,5,6,7,8], 50))
            
            
    
    