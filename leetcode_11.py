from typing import List


class Solution:
    @staticmethod
    def maxArea(height: List[int]) -> int:
        res = 0
        i, j = 0, len(height) - 1
        while i <= j:
            area = min(height[i], height[j]) * (j - i)
            res = max(res, area)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
