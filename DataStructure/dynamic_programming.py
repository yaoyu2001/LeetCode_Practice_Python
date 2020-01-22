# https://www.youtube.com/watch?v=Jakbj4vaIbE&t=26s
# Dynamic programming Question 1
# Given an array, choose tow of them which have most sum value. These two numbers can't Adjacent
# OPT = optimazition has two situation. Choose or not choose. OPI(i) = max { choose opt(i-2) + arr[i], opt(i-1)}
# When i = 0, only has one choose that is arr[i]
import numpy as np

arr = [1,2,4,1,7,8,3]
# First, recursion method
def recursion_opt(arr,i):
    if i == 0:
        return arr[0]
    elif i == 1:
        return max(arr[0], arr[1])
    else:
        A = recursion_opt(arr, i - 2) + arr[i]
        B = recursion_opt(arr, i - 1)
        return max(A, B)

print(recursion_opt(arr, 5))
# DP method
def dp_opt(arr):
    opt = np.zeros(len(arr))
    opt[0] = arr[0]
    opt[1] = max(arr[0], arr[1])
    for i in range(2,len(arr)):
        A = opt[i-2] + arr[i]
        B = opt[i-1]
        opt[i] = max(A,B)
    return opt[len(arr) - 1]

print(dp_opt(arr))

# Question 2 15:35
# Given an array choose some of them to get an answer S
# Subset(arr[i], s) Exit 1: s = 0 return true Exit 2 : when i == 0, arr[0] = s Exit3: if arr[i] > s, return subset(arr, i-1,s)
arr3 = [3,34,4,12,5,2]

def rec_subset(arr, i, s):
    if s == 0 : return True
    elif i == 0 : return arr[0] == s
    elif arr[i] > s:return rec_subset(arr,i-1,s)
    else:
        A = rec_subset(arr, i-1, s-arr[i])# choose arr[i]
        B = rec_subset(arr, i-1,s)# not choose arr[i]
    return A or B

def dp_subset(arr,S):

    subset = np.zeros((len(arr), s+1), dtype=bool)
    subset[:,0] = True
    subset[0,:] = False
    subset[0,arr[0]] = True
    for i in range(1,len(arr)):
        for j in range(1,S+1):
            if arr[i] > j:
                subset[i,j] = subset[i-1,j]
            else:
                A = subset[i-1,j-arr[i]]
                B = subset[i-1, j]
                subset[i,j] = A or B
    r,c = subset.shape
    return subset[r-1,c-1]