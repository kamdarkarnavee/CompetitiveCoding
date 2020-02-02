def findCircleNum(M):
        ls = []
        N = len(M)
        for i in range(N):
            ls.append({i})

        for i in range(N):
            for j in range(i, N):
                if M[i][j] == 1:
                    if i == j:
                        continue
                    s1 = set()
                    s2 = set()
                    for s in ls:
                        if len({i}.intersection(s)) != 0 and len({j}.intersection(s)) != 0:
                            break
                        else:
                            if len({i}.intersection(s)) != 0:
                                s1 = s
                            if len({j}.intersection(s)) != 0:
                                s2 = s
                    if s1 != s2:
                        ls.append(s1.union(s2))
                        if len(s1) != 0:
                            ls.remove(s1)
                        if len(s2) != 0:
                            ls.remove(s2)
        print(ls)
        return len(ls)

print(findCircleNum([[1,1,0],[1,1,1],[0,1,1]]))