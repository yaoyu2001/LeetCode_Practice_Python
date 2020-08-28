m = [2,1,5]
n = 5


def t1(m, n):
    set_ = set(m)
    count = 1
    while len(m) < n:
        if count not in set_:
            for i, num in enumerate(m):
                if num > count:
                    m.insert(i, count)
                    count += 1
                    if len(m) < n:
                        break
        else:
            count += 1

    return m

print(t1(m, 5))