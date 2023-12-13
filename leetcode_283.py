from typing import List


class Solution:
    @staticmethod
    def moveZeroes(nums: List[int]) -> None:
        l, r = 0, 0
        while r < len(nums):
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r += 1
            else:
                r += 1
        return None


if __name__ == "__main__":
    solution = Solution()
    solution.moveZeroes(nums=[0])
