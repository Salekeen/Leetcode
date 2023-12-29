class Solution:
    @staticmethod
    def isSubsequence(s: str, t: str) -> bool:
        i = j = 0
        while i < len(s):
            while j < len(t) and s[i] != t[j]:
                j += 1
            if j == len(t):
                break
            i += 1
            j += 1

        return True if i == len(s) else False


if __name__ == '__main__':
    sol = Solution()
    print(sol.isSubsequence("", ""))
