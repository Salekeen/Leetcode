class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        output_string = ""
        # let str1 represent the shorter str
        if len(str1) > len(str2):
            str1, str2 = str2, str1
        len_str_1 = len(str1)
        for i in range(len(str1), 0, -1):
            if i % len_str_1 == 0 and i % len(str2) == 0:
                pass


if __name__ == '__main__':
    s = Solution()
    print(s.gcdOfStrings("ABCABC", "ABC"))
