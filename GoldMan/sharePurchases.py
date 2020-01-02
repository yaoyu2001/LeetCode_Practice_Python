import collections

def sharePurchases(s,t):
    reslist = list()
    if len(s) < len(t) or s ==None or t == None or len(s) ==0 or len(t)==0:
        return reslist
    map = collections.defaultdict(int)

    for item in t:
        if not map.__contains__(item):
            map[item] = 1
        else:
            map[item] +=1

    counter = len(map)
    left = 0
    right = 0
    res =0

    while right<len(s):
        a = s[right]
        if map.__contains__(a):
            map[a] -=1
            if map[a] ==0:
                counter -=1
        right +=1

        while counter==0:
            temp = len(s)  -right +1
            for i in range(temp):
                reslist.append(s[left:right+i])
            b = s[left]
            if map.__contains__(b):
                map[b] +=1
                if map[b] >0:
                    counter +=1
            left +=1
    return reslist



inputs1 = "ABBCZBAC"
t ="ABC"

print(sharePurchases(inputs1,t))
print(len(sharePurchases(inputs1,t)))