# https://www.youtube.com/watch?v=XFPHg5KjHoo
# To give a sorted array, find the longest subarray that the sum of it equal to target value.
# sliding window

array = [1,2,3,4,5,0,0,0,6,7,8,9,10]
s = 15
def findLongestSubarrayBySum(target, array):

    result = [-1]

    sumof,left,right = 0,0,0

    while right<len(array):
        sumof += array[right]
        while left<right and sumof > target:
            sumof -= array[left]
            left +=1
        if sumof == target and (len(result)==1 or result[1] - result[0] < right - left):
            result = [left+1,right+1]

        right +=1

    return result

print(findLongestSubarrayBySum(15,array))

all_set = 1<<3
print(all_set)


