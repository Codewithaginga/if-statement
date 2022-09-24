def location(m,n):

    for i in range(len(m)):

        if m[i] == n:

            return i
    return [-1]


ls = [1, 2, 3, 4, 5]

loc = location(ls, 4)

print(loc)
