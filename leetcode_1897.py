from typing import List
from collections import Counter


class Solution:
    @staticmethod
    def makeEqual(words: List[str]) -> bool:
        counter = Counter()
        for word in words:
            counter.update(word)
        words_len = len(words)
        # check for even distribution of characters
        for count in counter.values():
            if count % words_len != 0:
                return False

        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.makeEqual(
        ["caaaaa", "aaaaaaaaa", "a", "bbb", "bbbbbbbbb", "bbb", "cc", "cccccccccccc", "ccccccc", "ccccccc", "cc",
         "cccc", "c", "cccccccc", "c"]))
