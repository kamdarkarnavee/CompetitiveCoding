ans = []
dictionary = dict()
capacity = 2


def get(key):
    if key in dictionary:
        ans.remove(key)
        ans.append(key)
        print(dictionary[key])
    else:
        print(-1)


def put(key, value):
    if len(dictionary) < capacity:
        if key in ans:
            ans.remove(key)
        ans.append(key)
        dictionary[key] = value
    else:
        if key in ans:
            ans.remove(key)
            dictionary.pop(key)
        else:
            dictionary.pop(ans[0])
            ans.remove(ans[0])
        ans.append(key)
        dictionary[key] = value


put(1,1)
put(2,2)
get(1)
put(3,3)
get(2)
put(4,4)
get(1)
get(3)
get(4)

