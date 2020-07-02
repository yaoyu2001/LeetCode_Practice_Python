class Solution(object):
    def anagramMappings(self, A, B):
        D = {x: i for i, x in enumerate(B)}
        return [D[x] for x in A]