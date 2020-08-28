class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> [int]:
        res = [0] * num_people
        n = 1
        index = 0

        while candies > 0:
            if candies - n >= 0:
                res[index % num_people] += n
                candies -= n
            else:
                res[index % num_people] += candies
                candies = 0

            n += 1
            index += 1

        return res
# print(so.distributeCandies(7, 4))