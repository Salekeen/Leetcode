from typing import List


class Solution:
    @staticmethod
    def kidsWithCandies(candies: List[int], extraCandies: int) -> List[bool]:
        max_candy = max(candies)
        output = [False] * len(candies)
        for i, candy in enumerate(candies):
            if candy + extraCandies >= max_candy:
                output[i] = True
        return output


if __name__ == '__main__':
    solution = Solution()
    print(solution.kidsWithCandies([2, 3, 5, 1, 3], 3))
