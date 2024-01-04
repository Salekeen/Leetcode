from typing import List


class Solution:
    @staticmethod
    def largestAltitude(gain: List[int]) -> int:
        prefix_array = [0]
        for i in range(len(gain)):
            prefix_array.append(gain[i] + prefix_array[-1])
            i += 1
        return max(prefix_array)


if __name__ == '__main__':
    solution = Solution()
    print(solution.largestAltitude([-4, -3, -2, -1, 4, 3, 2]))
