# https://www.youtube.com/watch?v=dQWsEWgbgc8
# Give an array [3,1,2,1] find a subarray which has longest length and sum of them no more than a number k

array = [3,1,2,1]
array2 = [1,1,1,9,9,1,1,1,1]
k = 4
k2= 4

def find_min_path(array, k):
    sum = 0
    length = 0
    front = 0
    length_case = []
    sum_case = []
    for i in array:
       sum += i
       length += 1
       if sum > k:
           sum -= array[front]
           front += 1
           length -= 1
       else:
           length_case.append(length)
           sum_case.append(sum)
    # return sorted(length_case)[len(length_case)-1]
    return sorted(length_case),sorted(sum_case)
print(find_min_path(array,k))
print(find_min_path(array2,k2))