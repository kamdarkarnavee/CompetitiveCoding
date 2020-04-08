
def group_anagrams(strs):
    dictionary = dict()
    for i in strs:
        dictionary.setdefault(tuple(sorted(i)), []).append(i)
    return list(dictionary.values())


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(strs))