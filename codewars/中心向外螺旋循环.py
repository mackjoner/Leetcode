def spiral(X, Y):
    x = y = 0
    dx = 0
    dy = -1
    res = []
    for i in range(max(X, Y) ** 2):
        if (-X / 2 < x <= X / 2) and (-Y / 2 < y <= Y / 2):
            # print(x, y)
            res.append(i)
        if x == y or (x < 0 and x == -y) or (x > 0 and x == 1 - y):
            dx, dy = -dy, dx
        x, y = x + dx, y + dy


spiral(3, 3)


def spiral(N, M):
    x, y = 0, 0
    dx, dy = 0, -1

    for dumb in xrange(N * M):
        if abs(x) == abs(y) and [dx, dy] != [1, 0] or x > 0 and y == 1 - x:
            dx, dy = -dy, dx            # corner, change direction

        if abs(x) > N / 2 or abs(y) > M / 2:    # non-square
            dx, dy = -dy, dx            # change direction
            x, y = -y + dx, x + dy          # jump

        yield x, y
        x, y = x + dx, y + dy
