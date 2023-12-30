from typing import List
from collections import Counter


class Solution:
    @staticmethod
    def maxOperations(nums: List[int], k: int) -> int:
        op_count = 0
        counter = Counter(nums)
        for i in range(len(nums)):
            y = k - nums[i]
            if counter.get(y) is not None:
                if not nums[i] == (k / 2):
                    op_count += min(counter.get(y), counter.get(nums[i]))
                else:
                    op_count += (counter[nums[i]] // 2)

                del counter[nums[i]]
                del counter[y]

        return op_count


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxOperations([3, 1, 3, 4, 3], 6))
