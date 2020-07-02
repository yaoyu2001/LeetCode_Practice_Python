class Solution:
    def isAlienSorted(self, words: [str], order: str) -> bool:
        m = {c:i for i,c in enumerate(order)}

        words = [[m[c] for c in w] for w in words]
        z = zip(words, words[1:])
        for item in z:
            print(item)
        for w1, w2 in zip(words, words[1:]):
             print(w1,w2)

        return all(w1<w2 for w1, w2 in (words, words[1:]))

words = ["hello","leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"

so = Solution()
# print(so.isAlienSorted(words,order))