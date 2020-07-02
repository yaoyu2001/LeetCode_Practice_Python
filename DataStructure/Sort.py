 #1.Bubble sort


def bubble(arr):

    for i in range(len(arr)):
        for j in range(0, len(arr) - i -1):
            if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

arr = [64, 34, 25, 12, 22, 11, 90]
# print(arr)
# print(bubble(arr))

# 2 Quick sort
def quickSort(arr, startIndex, endIndex):
    if startIndex >= endIndex:
        return

    pivotIndex = partition(arr, startIndex, endIndex)
    # print(pivotIndex)

    quickSort(arr, startIndex, pivotIndex - 1)
    quickSort(arr, pivotIndex + 1, endIndex)
    return arr

def partition(arr, startIndex, endIndex):
        """Pick the first element as pivot"""
        pivot = arr[startIndex]
        left = startIndex
        right = endIndex
        """The position of hole, the same with pivot at beginning"""
        index = startIndex

        """Out loop, end when left pointer and right pointer intersect"""
        while right >= left:

            while right >= left:
                """Inner loop, from right to left, when fill a hole, break"""
                if arr[right] < pivot:
                    arr[left] = arr[right]
                    index = right
                    left += 1
                    break
                else:
                    right -= 1

            while right >= left:
                """Inner loop, from left to right, when fill a hole, break"""
                if arr[left] > pivot:
                    arr[right] = arr[left]
                    index = left
                    right -= 1
                    break
                else:
                    left += 1

        arr[index] = pivot

        return index



# print(quickSort(arr,0,len(arr) -1))

# print(partition(arr, 0 ,len(arr) -1))

#3. Merge sort
# https://www.youtube.com/watch?v=cyGTFYJZY_E&list=PLJCHnHCd1EzRBdOdjbPxxQK75OJswMXjY&index=5&t=4049s
def mergeTwoArr(arr1,arr2,result):

    i, j = 0,0
    while i < len(arr1) and j < len(arr2):

        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1

    for item1 in range(i, len(arr1)):
        result.append(arr1[item1])
    for item2 in range(j, len(arr2)):
        result.append(arr2[item2])

    return result


def mergeSort(arr):

    if len(arr) < 2:
        return

    mid = len(arr)//2

    sub_arr1,sub_arr2 = [],[]

    for i in range(mid):
        sub_arr1.append(arr[i])
    for j in range(mid, len(arr)):
        sub_arr2.append(arr[j])

    mergeSort(sub_arr1)
    mergeSort(sub_arr2)

    arr.clear()
    # mergeTwoArr(sub_arr1, sub_arr2, arr)

    return mergeTwoArr(sub_arr1, sub_arr2, arr)







# print(mergeTwoArr([2,5,8,20], [1,3,5,7,30,50]))
print(mergeSort([5,-7,9,8,1]))