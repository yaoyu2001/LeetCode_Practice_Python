import collections
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        # Use a hashmap to store number of numbers in "secret"
        h_secret = collections.Counter(secret)

        bulls, cows = 0, 0

        # One pass guess
        for idx, c in enumerate(guess):
            if c in h_secret:
                # corresponding characters match
                if c == secret[idx]:
                    # Update bulls when find match
                    bulls += 1
                    # If all cows in "secret" were used up, update numbers of cow
                    cows -= int(h_secret[c] <= 0)
                else:
                    # If still have unused "current number" in "secret", add a cow
                    cows += int(h_secret[c] > 0)

            h_secret[c] -= 1

        return f"{bulls}A{cows}B"

so = Solution()
print(so.getHint("1123", "0111"))