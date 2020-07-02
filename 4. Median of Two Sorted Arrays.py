
def findMedianSortedArrays(nums1, nums2):
        """If input length is greater than switch them so that input1 is smaller than input2"""
        if len(nums1) > len(nums2):
            return findMedianSortedArrays(nums2,nums1)

        x = len(nums1)
        y = len(nums2)

        low = 0
        high = x

        while low <= high:
            partitionX = int((low + high)/2)
            partitionY = int((x + y + 1)/2 - partitionX)

            maxLeftx = float("-inf") if partitionX == 0 else nums1[partitionX -1]
            minrightx = float("inf") if partitionX == x else nums1[partitionX]

            maxLefty = float("-inf") if partitionY == 0 else nums2[partitionY - 1]
            minrighty = float("inf") if partitionY == y else nums2[partitionY]

            if maxLeftx <= minrighty and maxLefty <= minrightx:
                if (x+y)%2 == 0:
                    return (max(maxLeftx,maxLefty) + min(minrightx,minrighty))/2
                else:
                    return max(maxLeftx,maxLefty)
            elif maxLeftx > minrighty:
                high = partitionX - 1
            else:
                low = partitionX + 1
        return None

num1 = [1,3]
num2 = [2]
print(findMedianSortedArrays(num1,num2))