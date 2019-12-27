def reorderLogFiles(logs):
    def f(log):
        id_, rest = log.split(" ", 1)
        return (1, rest, id_) if rest[0].isalpha() else (2,)

    return sorted(logs, key=f)

def f(log):
    id_, rest = log.split(" ", 1)
    print(type(id_))
    print(id_,rest)
    print(rest)
    return (3, rest, id_) if rest[0].isalpha() else (2,)

# print(f("dig1 8 1 5 1"))
# print(type(f("let1 art can")))
print(reorderLogFiles(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]))