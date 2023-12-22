from typing import List


class Solution:
    @staticmethod
    def twoSum(numbers: List[int], target: int) -> List[int]:
        # Intuition
        # Notice, as the array will be in sorted ascending order
        # the smaller values will be lesser indexed and so on..
        # NOW!
        # WHEN THE x+y for any (x,y) will become less than the target sum
        # then that means we need to increase our current sum and vice versa

        l, r = 0, len(numbers) - 1
        while l <= r:
            s = numbers[l] + numbers[r]

            if s == target:
                return [l + 1, r + 1]

            if s < target:
                l += 1
            else:
                r -= 1


if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([-1, 0], target=-1))
