arr = [1, 2, None, 3, 1, None,2]
b = set()
for i in arr:
    if i not in b:
        b.update(i)
        print("added")
    else:
        print(i)
