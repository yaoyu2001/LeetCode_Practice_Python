class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        # When number of nodes = 0 and 1, only have 1 situation
        dp[0], dp[1] = 1, 1

        # Let G(n) be the number of unique BST for a sequence of length n dp[n] = G[n]
        # F(i,n) as the number of unique BST, where the number i is served as the root of BST (1 \leq i \leq n1≤i≤n).
        # Recursively got each case by G(n)=∑(n,i=1) F(i,n) and F(i,n) = G(i-1)*G(n-i)

        # From 2 because we have got the result of 0, and 1 nodes
        for i in range(2, n+1):
            # From node 1 to node n
            for j in range(1, i+1):
                dp[i] += dp[j-1]*dp[i-j]


        return dp[n]

