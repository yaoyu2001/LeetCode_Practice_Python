class Solution:
    def findMaximumXOR(self, nums: [int]) -> int:
        # length of max number in a binary representation
        L = len(bin(max(nums))) - 2
        max_xor = 0
        for i in range(L)[::-1]:
            # go to the next bit by the left shift
            max_xor <<= 1
            # set 1 in the smallest bit
            curr_xor = max_xor | 1
            # compute all existing prefixes
            # of length (L - i) in binary representation
            prefixes = {num >> i for num in nums}
            # Update max_xor, if two of these prefixes could result in curr_xor.
            # Check if p1^p2 == curr_xor, i.e. p1 == curr_xor^p2
            for p in prefixes:
                if curr_xor ^ p in prefixes:
                    max_xor = curr_xor
                    break
            # max_xor |= any(curr_xor ^ p in prefixes for p in prefixes)

        return max_xor

input = [3, 10, 5, 25, 2, 8]
so = Solution()
print(so.findMaximumXOR(input))