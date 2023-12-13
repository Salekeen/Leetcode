from typing import List


class Solution:
    @staticmethod
    def findDifference(nums1: List[int], nums2: List[int]) -> List[List[int]]:
        return [list(set(nums1) - set(nums2)), list(set(nums2) - set(nums1))]


if __name__ == '__main__':
    s = Solution()
    print(s.findDifference(nums1=[1, 2, 3], nums2=[2, 4, 6]))
