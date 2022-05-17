def sum(arr):
    #Base Case
    if len(arr) == 1:
        return arr[0]

    # Subproblem
    return arr[0] + sum(arr[1:len(arr)])

print(sum([1,2,3,4,5]))