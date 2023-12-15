from typing import List


class Solution:
    @staticmethod
    def equalPairs(grid: List[List[int]]) -> int:
        count = 0
        columns_map = {}
        for row in grid:
            for index, column in enumerate(row):
                columns_map.setdefault(index, []).append(column)

        for row in grid:
            for i in range(len(row)):
                matched = True
                for j in range(len(row)):
                    if columns_map[i][j] != row[j]:
                        matched = False
                        break
                if matched:
                    count += 1
        return count


if __name__ == '__main__':
    solution = Solution()
    print(solution.equalPairs([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]))
