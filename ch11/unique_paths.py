def find_unique_paths(rows, cols):

    # Base Case
    if rows == 1 or cols == 1:
        return 1
    
    return find_unique_paths(rows -1, cols) + find_unique_paths(rows, cols-1)

print(find_unique_paths(3, 7))