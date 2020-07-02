import bisect
import copy

class Solution:
    def countSmaller(self, nums: [int]) -> [int]:
        sortedL, res = [], []
        for n in nums[:: -1]:
            idx = bisect.bisect_left(sortedL, n)
            print(f"inx = {idx}")
            sortedL.insert(idx, n)
            res.append(idx)

        return res[::-1]

so=Solution()
# print(so.countSmaller([5,2,6,1]))


# Method 2 Merge sort
# https://leetcode.com/problems/count-of-smaller-numbers-after-self/discuss/76584/Mergesort-solution
#
class Solution2:
    def countSmaller(self, nums):
        def sort(enum):
            half = len(enum) / 2
            if half:
                left, right = sort(enum[:half]), sort(enum[half:])
                for i in range(len(enum))[::-1]:
                    if not right or left and left[-1][1] > right[-1][1]:
                        smaller[left[-1][0]] += len(right)
                        enum[i] = left.pop()
                    else:
                        enum[i] = right.pop()
            return enum
        smaller = [0] * len(nums)
        sort(list(enumerate(nums)))
        return smaller

#  Method 3 Binary Search Tree




class BSTNode:
    def __init__(self,val):
        self.val = val
        self.count = 0
        self.left = None
        self.right = None


class BSTree:

    def BST_insert(self, node: BSTNode, insert_node: BSTNode, counter_small):

        if insert_node.val <= node.val:
            node.count += 1
            if node.left:
                self.BST_insert(node.left, insert_node, counter_small)
            else:
                node.left = insert_node
        else:
            counter_small += node.count + 1
            if node.right:
                self.BST_insert(node.right, insert_node, counter_small)
            else:
                node.right = insert_node

class Solution3:

    def BST_insert(self, node: BSTNode, insert_node: BSTNode, counter_small):

        if insert_node.val <= node.val:
            node.count += 1
            if node.left:
                self.BST_insert(node.left, insert_node, self.count_small)
            else:
                node.left = insert_node
        else:
            self.count_small += node.count + 1 if node.count else 1
            if node.right:
                self.BST_insert(node.right, insert_node, self.count_small)
            else:
                node.right = insert_node

    def countSmaller(self, nums):


        node_vec = []
        count = []

        for item in nums[::-1]:
            node_vec.append(BSTNode(item))

        count.append(0)

        for i in range(1, len(node_vec)):
            self.count_small = 0
            self.BST_insert(node_vec[0], node_vec[i], self.count_small)
            count.append(copy.deepcopy(self.count_small))

        return count[::-1]

so3 = Solution3()
print(so3.countSmaller([5,2,6,1]))