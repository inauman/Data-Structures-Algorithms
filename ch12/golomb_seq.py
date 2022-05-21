#Golomb sequence

def golomb(n, memo={}):
    # Base Case
    if n == 1:
        return 1

    # Sub problem
    # Fix: To fix the inefficiency in the algorith, use the Hashtable (memo) to store the computation results to be used by the parents.
        
    if not memo.get(n):
        memo[n] = 1 + golomb(n - golomb(golomb(n-1, memo), memo), memo)
    
    return memo[n]