from typing import List


class Solution:
    @staticmethod
    def increasingTriplet(nums: List[int]) -> bool:
        # if len(nums)<=2 then dont consider anything
        if len(nums) < 3:
            return False

        # Finding Left Min array
        left_minimum = [nums[0]] * len(nums)
        for i in range(1, len(nums)):
            if nums[i] < left_minimum[i - 1]:
                left_minimum[i] = nums[i]
            else:
                left_minimum[i] = left_minimum[i - 1]

        # Finding Right MAX ARRAY
        right_maximum = [nums[-1]] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] > right_maximum[i + 1]:
                right_maximum[i] = nums[i]
            else:
                right_maximum[i] = right_maximum[i + 1]

        # Finding triplet
        triplet_exist = False
        for i in range(len(nums)):
            if left_minimum[i] < nums[i] < right_maximum[i]:
                triplet_exist = True
                break

        return triplet_exist


if __name__ == '__main__':
    solution = Solution()
    print(solution.increasingTriplet([20, 100, 10, 12, 5, 13]))
