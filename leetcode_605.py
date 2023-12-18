from typing import List


class Solution:
    @staticmethod
    def canPlaceFlowers(flowerbed: List[int], n: int) -> bool:
        original_size = len(flowerbed)
        flowerbed.insert(0, 0)
        flowerbed.append(0)

        i = 1
        while i <= original_size and n > 0:
            if flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0 and flowerbed[i] != 1:
                flowerbed[i] = 1
                n -= 1
            i += 1

        if n == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    solution = Solution()
    print(solution.canPlaceFlowers([1, 0, 0, 0, 1, 0, 0], 2))
