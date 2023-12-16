class Solution:
    @staticmethod
    def reverseVowels(s: str) -> str:
        s = list(s)
        i, j = 0, len(s) - 1
        found_vowel_i = False
        found_vowel_j = False
        while i <= j:
            if s[i] in 'aeiou':
                found_vowel_i = True
            else:
                i += 1

            if s[j] in 'aeiou':
                found_vowel_j = True
            else:
                j -= 1

            if found_vowel_i and found_vowel_j:
                s[i], s[j] = s[j], s[i]
                found_vowel_j, found_vowel_i = False, False
                i += 1
                j -= 1

        return ''.join(s)


if __name__ == '__main__':
    s1 = Solution()
    print(s1.reverseVowels("leetcode"))
