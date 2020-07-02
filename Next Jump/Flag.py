# Given an array list that every element is also a list, for each sub list,
# the first element is id and second is flag. Find all element that flag equal to one

def findflag(arr):
    counter = 0
    res =set()

    for item in arr:
        if item[1] == -1:
            res.add(item[0])
            counter +=1