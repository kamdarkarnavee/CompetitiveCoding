def reverse_words(words):
    ptr = 0
    print(words)
    l = len(words)
    for i in range(l):
        if words[i] == ' ':
            words.pop(i)
            words.insert(0, ' ')
            ptr = 0
        else:
            temp = words[i]
            words.pop(i)
            words.insert(ptr, temp)
            ptr += 1
    print(words)



s = list("can you read this")
reverse_words(s)
print(''.join(s))
# this read you can