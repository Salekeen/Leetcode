from typing import List


class Solution:
    @staticmethod
    def findMaxAverage(nums: List[int], k: int) -> float:
        curr_sum = sum(nums[:k])
        max_sum = curr_sum

        i = 0
        j = i + k
        while j < len(nums):
            curr_sum = curr_sum - nums[i] + nums[j]
            max_sum = max(max_sum, curr_sum)
            j += 1
            i += 1

        return max_sum / k


if __name__ == '__main__':
    solution = Solution()
    print(solution.findMaxAverage([4], k=1))
