'''def unique_paths(rows, columns):
    # Base Case
    if rows == 1 or columns == 1:
        return 1

    # Sub problem
    return unique_paths(rows - 1, columns) + unique_paths(rows, columns -1)'''

def unique_paths(rows, columns, memo = {}):
    # Base Case
    if rows == 1 or columns == 1:
        return 1

    # Sub problem
    if not memo.get((rows, columns)):
        memo[(rows, columns)] = unique_paths(rows - 1, columns, memo) + unique_paths(rows, columns -1, memo)
        
    return memo[(rows, columns)]

print(unique_paths(3, 7))