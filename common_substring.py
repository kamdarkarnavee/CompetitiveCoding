def commonSubString(a, b):
    for i in range(len(a)):
        if set(a[i]).intersection(b[i]):
            print("YES")
        else:
            print("NO")


commonSubString(["ab", "bc"], ["af", "df"])