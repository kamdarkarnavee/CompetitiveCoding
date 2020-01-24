
def has_character_map(str1, str2):
    d = dict()

    if (len(set(str1)) != len(set(str2))) or (len(str1) != len(str2)):
        return False

    for i, j in zip(str1, str2):
        if i in d:
            d[i] = d[i].union(j)
            if len(d[i]) >= 2:
                return False
        else:
            d[i] = set(j)
    return True


print(has_character_map('abc', 'ebec'))
print(has_character_map('aabc', 'ddef'))
