from typing import List


class Solution:
    @staticmethod
    def findMaxConsecutiveOnes(nums: List[int]) -> int:
        curr_max = counter = i = 0

        while i < len(nums):
            if nums[i] == 1:
                counter += 1
            else:
                counter = 0
            curr_max = max(curr_max, counter)
            i += 1

        return curr_max


if __name__ == '__main__':
    solution = Solution()
    print(solution.findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1]))
