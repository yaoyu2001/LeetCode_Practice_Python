
#https://www.youtube.com/watch?v=4O2x7g_vRFs&list=PLJCHnHCd1EzRBdOdjbPxxQK75OJswMXjY&index=7

def binary_search(sort_array, begin, end, target):

    if begin > end:
        return False
    mid = (begin + end)//2

    if target == sort_array[mid]:
        return True

    elif target<sort_array[mid]:
        return binary_search(sort_array,begin,mid-1,target)
    elif target>sort_array[mid]:
        return binary_search(sort_array,mid+1,end,target)


def binary_search_iterate(sort_array, target):

    begin =0
    end = len(sort_array) - 1
    while begin<=end:
        mid = (begin + end) //2


        if target == sort_array[mid]:
            return True

        elif target<sort_array[mid]:
            end = mid - 1
        elif target>sort_array[mid]:
            begin = mid + 1
    return False
arr= [1,2,3,4,5,6,7,8,9,10]
t = 1
print(binary_search(arr,0,9,1))
print(binary_search_iterate(arr,1))
