from typing import List


class Solution:
    @staticmethod
    def productExceptSelf(nums: List[int]) -> List[int]:
        # Step 1: Calculate the prefix array
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(nums[i] * prefix[-1])
        # Step 2: Calculate the postfix array
        postfix = [nums[-1]]
        for i in range(len(nums) - 2, -1, -1):
            postfix.insert(0, nums[i] * postfix[0])

        # Step 3: Do multiplication
        result_list = []
        for i in range(len(nums)):
            pre = 1 if i == 0 else prefix[i - 1]
            post = 1 if i == len(nums) - 1 else postfix[i + 1]
            result_list.append(pre * post)

        return result_list


if __name__ == '__main__':
    s = Solution()
    print(s.productExceptSelf([3, 4]))
