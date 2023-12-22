from typing import List


class Solution:
    @staticmethod
    def twoSum(nums: List[int], target: int) -> List[int]:
        # This holds key:index
        maps = {}

        for index, num in enumerate(nums):
            y = target - num

            if maps.get(y) is None:
                maps[num] = index
            else:
                return [index, maps.get(y)]


if __name__ == '__main__':
    solution = Solution()
    print(solution.twoSum(nums=[3, 2, 4], target=6))
