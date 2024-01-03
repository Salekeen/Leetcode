class Solution:
    @staticmethod
    def gcdOfStrings(str1: str, str2: str) -> str:
        output_string = ""
        # let str1 represent the shorter str
        if len(str1) > len(str2):
            str1, str2 = str2, str1
        len_str_1 = len(str1)
        for i in range(len(str1), 0, -1):
            if len_str_1 % i == 0:
                multiplier_1 = len(str1) // i
                multiplier_2 = len(str2) // i
                if str1[:i] * multiplier_1 == str1 and str1[:i] * multiplier_2 == str2:
                    output_string += str1[:i]
                    break

        return output_string


if __name__ == '__main__':
    s = Solution()
    print(s.gcdOfStrings("ABCABC", "ABC"))
