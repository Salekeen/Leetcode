from typing import List


class Solution:
    @staticmethod
    def longestOnes(nums: List[int], k: int) -> int:
        curr_max = i = j = 0

        while i < len(nums):
            if nums[i] == 0:
                k -= 1

            if k < 0:
                while nums[j] != 0:
                    j += 1
                j += 1
                k += 1
            curr_max = max(curr_max, i - j + 1)
            i += 1

        return curr_max


if __name__ == '__main__':
    solution = Solution()
    print(solution.longestOnes(nums=[0, 0], k=2))
