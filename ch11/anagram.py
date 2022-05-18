def anagrams(s):
    #Base Case
    if len(s) == 1:
        return [s[0]]

    anagram_words = anagrams(s[1:])

    #print(f'anagram_words ===> {anagram_words}')
    
    #Subprogram
    collection = []
    for w in anagram_words:
        for pos in range(len(w) + 1):
            #print(f'"{w}" ===> "{w[:pos]}" : "{s[0]}" : "{w[pos:]}"')
            collection.append(w[:pos] + s[0] + w[pos:])
    return collection

print(anagrams('abcd'))