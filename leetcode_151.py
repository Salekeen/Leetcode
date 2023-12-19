from typing import List


class Solution:
    @staticmethod
    def reverseWords(s: str) -> str:
        words: List[str] = s.split()
        words_stripped = [word.strip() for word in words]

        i, j = 0, len(words_stripped) - 1
        while i <= j:
            words_stripped[i], words_stripped[j] = words_stripped[j], words_stripped[i]
            i += 1
            j -= 1

        reversed_str: str = " ".join(words_stripped)
        return reversed_str


if __name__ == '__main__':
    solution = Solution()
    print(solution.reverseWords("  hello   world  "))
