from typing import List


class Solution:
    @staticmethod
    def maxOperations(nums: List[int], k: int) -> int:
        op_count = 0
        mappings = {}

        for i in range(len(nums)):
            y = k - nums[i]
            if mappings.get(y) is None:
                mappings[nums[i]] = i
            else:
                op_count += 1
                del mappings[y]

        return op_count


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxOperations([2, 5, 4, 4, 1, 3, 4, 4, 1, 4, 4, 1, 2, 1, 2, 2, 3, 2, 4, 2], 3))
