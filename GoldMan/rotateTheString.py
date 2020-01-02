def rotateTheString(s, dir, amount):
    length = len(s)
    left = 0
    right = 0
    for i in range(len(dir)):
        if dir[i] == 0:
            left += amount[i] % length
            left %= length
        else:
            right += amount[i] % length
            right %= length

    if left == right:
        return s
    elif left > right:
        left -= right
        s += s[0:left]
        return s[left:]
    else:
        right -= left
        s = s[length-right:] + s
        return s[0:length]


s = "hurart"
dir = [1,0]
amount= [4,1]

print(rotateTheString(s,dir,amount))
