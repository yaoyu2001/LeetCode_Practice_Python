import collections
def ri(s):
    a, b = collections.defaultdict(int), collections.Counter(s)
    result = 0
    for char in s:
        a[char] += 1
        b[char] -= 1
        if b[char] == 0:
            del b[char]
        print(a,b)
        a_key, b_key = set(a.keys()), set(b.keys())
        count = 0
        for i in a_key:
            if i in b_key:
                count += min(a[i], b[i])
        if count > result:
            result = count
    return result

s = 'zzzxxxzzz'

print(ri(s))
