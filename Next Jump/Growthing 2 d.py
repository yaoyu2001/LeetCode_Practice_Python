def countMax(upRight):
    # Write your code here
    if upRight == None or len(upRight) == 0:
        return 0
    def get_d1_d2(item):
        up0 = item[0].split(" ")
        return int(up0[0]), int(up0[1])

    d1, d2 = get_d1_d2(upRight[0])

    for string in upRight[1:]:
        temp1, temp2 = get_d1_d2(string)
        if d1 > temp1: d1 = temp1
        if d2 > temp2: d2 = temp2
        print(d1,d2)
    return d1 * d2

if __name__ == '__main__':
    countMax(str)