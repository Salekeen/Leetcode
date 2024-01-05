from typing import List


class Solution:
    @staticmethod
    def pivotIndex(nums: List[int]) -> int:
        left_array = []
        right_array = []

        for i in range(len(nums)):
            if left_array:
                left_array.append(nums[i] + left_array[-1])
            else:
                left_array.append(nums[i])

        for i in range(len(nums) - 1, -1, -1):
            if right_array:
                right_array.insert(0, right_array[0] + nums[i])
            else:
                right_array.append(nums[i])

        for i in range(len(nums)):
            if left_array[i] == right_array[i]:
                return i
            i += 1

        return -1


if __name__ == '__main__':
    solution = Solution()
    print(solution.pivotIndex([1, 7, 3, 6, 5, 6]))
