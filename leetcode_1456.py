class Solution:
    @staticmethod
    def maxVowels(s: str, k: int) -> int:
        vowels = 'aeiou'
        # calculating number of vowels in the current window
        curr_count = 0
        for character in s[:k]:
            if character in vowels:
                curr_count += 1

        max_count = curr_count

        # initializing the start and tail indices of the window
        i = 0
        j = i + k
        while j < len(s):
            if s[j] in vowels:
                curr_count += 1
            if s[i] in vowels:
                curr_count -= 1

            i += 1
            j += 1
            max_count = max(max_count, curr_count)

        return max_count


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxVowels("leetcode", 3))
