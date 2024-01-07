class Solution:
    @staticmethod
    def removeStars(s: str) -> str:
        string_stack = []
        for char in s:
            string_stack.pop() if char == '*' else string_stack.append(char)
        return ''.join(string_stack)


if __name__ == '__main__':
    solution = Solution()
    print(solution.removeStars("erase*****"))
