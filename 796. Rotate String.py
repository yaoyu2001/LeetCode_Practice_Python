# 1 Brute Force
class Solution(object):
    def rotateString(self, A, B):
        if len(A) != len(B):
            return False
        if len(A) == 0:
            return True

        for s in range(len(A)):
            if all(A[(s+i) % len(A)] == B[i] for i in range(len(A))):
                return True
        return False


# 2 Simple Check
class Solution2:
    def rotateString(self, A: str, B: str) -> bool:
          return len(A) == len(B) and B in A+A


# 3 Roll Hash
class Solution3(object):
    def rotateString(self, A, B):
        MOD = 10**9 + 7
        P = 113
        Pinv = pow(P, MOD-2, MOD)

        hb = 0
        power = 1
        for x in B:
            code = ord(x) - 96
            hb = (hb + power * code) % MOD
            power = power * P % MOD

        ha = 0
        power = 1
        for x in A:
            code = ord(x) - 96
            ha = (ha + power * code) % MOD
            power = power * P % MOD

        if ha == hb and A == B: return True
        for i, x in enumerate(A):
            code = ord(x) - 96
            ha += power * code
            ha -= code
            ha *= Pinv
            ha %= MOD
            if ha == hb and A[i+1:] + A[:i+1] == B:
                return True
        return False


# 4 KMP
class Solution4:
    def rotateString(self, A, B):
        N = len(A)
        if N != len(B): return False
        if N == 0: return True

        #Compute shift table
        shifts = [1] * (N+1)
        left = -1
        for right in range(N):
            while left >= 0 and B[left] != B[right]:
                left -= shifts[left]
            shifts[right + 1] = right - left
            left += 1

        #Find match of B in A+A
        match_len = 0
        for char in A+A:
            while match_len >= 0 and B[match_len] != char:
                match_len -= shifts[match_len]

            match_len += 1
            if match_len == N:
                return True

        return False