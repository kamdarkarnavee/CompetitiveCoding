"""Insert only the first occurrence of anagram strings"""


def anagrams_array(ls):
    dictionary = dict()

    for i in ls:
        temp = ''.join(sorted(i))
        if temp not in dictionary:
            dictionary[temp] = i

    print(dictionary.values())


anagrams_array(['poke', 'opke', 'gramana', 'anagram', 'coke'])