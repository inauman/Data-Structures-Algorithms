def anagram(s):
    
    # Base Case
    if len(s) == 1:
        return [s]
    # Subproblem

    words = anagram(s[1:])
    collection = []
    
    for word in words:
        for i in range(len(word)+1):
            collection.append(word[:i] + s[0] + word[i:])

    return collection

print(anagram('abcd'))