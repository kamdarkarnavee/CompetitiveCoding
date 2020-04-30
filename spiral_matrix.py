def spiralOrder(n):
    row_begin = 0
    row_end = n-1
    col_begin = 0
    col_end = n-1
    ans = [[i for i in range(n)] for j in range(n)]
    count = 1
    while row_begin <= row_end and col_begin <= col_end:
        for i in range(col_begin, col_end+1):
            ans[row_begin][i] = count
            count += 1
        row_begin += 1

        for i in range(row_begin, row_end+1):
            ans[i][col_end] = count
            count += 1
        col_end -= 1

        if col_begin <= col_end:
            for i in range(col_end, col_begin-1, -1):
                ans[row_end][i] = count
                count += 1
        row_end -= 1

        if row_begin <= row_end:
            for i in range(row_end, row_begin-1, -1):
                ans[i][col_begin] = count
                count += 1
        col_begin += 1

    print(ans)


# create an n x n spiral matrix
n = 3
spiralOrder(n)
