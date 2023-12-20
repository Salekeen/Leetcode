class Solution:
    @staticmethod
    def isValid(s: str) -> bool:
        closeToOpen = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        # Lets create our stack
        stack = []

        for char in s:
            # found a closing bracket
            if char in closeToOpen.keys():
                if stack and closeToOpen[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return True if not stack else False


if __name__ == '__main__':
    sol = Solution()
    print(sol.isValid("{"))
