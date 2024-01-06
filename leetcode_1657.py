from collections import Counter


class Solution:
    @staticmethod
    def closeStrings(word1: str, word2: str) -> bool:
        counter1 = Counter(word1)
        counter2 = Counter(word2)
        frequency_match = sorted(list(counter2.values())) == sorted(list(counter1.values()))
        have_all_the_characters = len(set(counter1.keys()).symmetric_difference(set(counter2.keys()))) == 0

        return frequency_match and have_all_the_characters


if __name__ == '__main__':
    solution = Solution()
    print(solution.closeStrings("a", 'aa'))
