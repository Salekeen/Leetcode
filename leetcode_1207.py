from typing import List


class Solution:
    @staticmethod
    def uniqueOccurrences(arr: List[int]) -> bool:
        occurance_map = {}
        for num in arr:
            occurance_map[num] = occurance_map.get(num, 0) + 1
        seen_values = set()
        has_duplicate = False
        for value in occurance_map.values():
            if value in seen_values:
                has_duplicate = True
                break
            seen_values.add(value)

        return False if has_duplicate else True


if __name__ == '__main__':
    s = Solution()
    print(s.uniqueOccurrences(arr=[-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]))
