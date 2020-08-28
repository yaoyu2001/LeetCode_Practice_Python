# Solution 1 backtrack

class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.combinations = []
        n, k = len(characters), combinationLength

        def backtrack(first = 0, cur = []):
            # if combinations is done
            if len(cur) == k:
                self.combinations.append(''.join(cur[:]))
                return
            for i in range(first, n):
                cur.append(characters[i])
                backtrack(first + 1, cur)
                cur.pop()

        backtrack()
        self.combinations.reverse()



    def next(self) -> str:
        return self.combinations.pop()

    def hasNext(self) -> bool:
        return self.combinations == []

# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()

# Solution2 bit
class CombinationIterator2:
    def __init__(self, characters: str, combinationLength: int):
        self.combinations = []
        n, k = len(characters), combinationLength

        # generate bitmasks from 0..00 to 1..11
        for bitmask in range(1 << n):
            # use bitmasks with k 1-bits
            if bin(bitmask).count('1') == k:
                # convert bitmask into combination
                # 111 --> "abc", 000 --> ""
                # 110 --> "ab", 101 --> "ac", 011 --> "bc"
                curr = [characters[j] for j in range(n) if bitmask & (1 << n - j - 1)]
                self.combinations.append(''.join(curr))

    def next(self) -> str:
        return self.combinations.pop()

    def hasNext(self) -> bool:
        return self.combinations

so = CombinationIterator2("abc", 2)
print(so.next())
print(so.next())
print(so.next())

print(bin(1<<3))
