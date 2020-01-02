def findRank(performance, rank):
    n = len(performance)
    k = len(performance[0])

    grade = [[None for i in range(2)] for j in range(n)]

    for i in range(0,n):
        g = 0
        for j in range(0,k):
            g += performance[i][j]
        grade[i][0] = g
        grade[i][1] = i
    print(grade)
    grade.sort(key=lambda a:a[0], reverse=True)
    for i in range(n):
        print(f"Grade is {grade[i][0]} ID is {grade[i][1]}")
    return grade[rank - 1][1]

def findRank_c(performance, rank):
    grade_a = sorted([(sum(list_), i) for i, list_ in enumerate(performance)])[::-1]
    grade = [(sum(list_), i) for i, list_ in enumerate(performance)]
    print(grade)
    grade.sort(key=lambda a:a[0],reverse=True)
    print(grade)
    print(grade_a)


performance = [[79,89,15],[85,89,92],[71,96,88],[70,97,88]]
rank = 2
print(findRank(performance,rank))
findRank_c(performance,rank)