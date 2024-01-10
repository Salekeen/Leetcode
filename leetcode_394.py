class Solution:
    @staticmethod
    def decodeString(s: str) -> str:
        stack = []
        for character in s:
            if character != "]":
                stack.append(character)
            else:
                temp = ''
                while stack and stack[-1] != '[':
                    temp = stack.pop() + temp
                stack.pop()
                num = ''
                while stack and stack[-1].isnumeric():
                    num = stack.pop() + num

                stack.append(temp * int(num))

        return ''.join(stack)


if __name__ == '__main__':
    sol = Solution()
    print(sol.decodeString("2[abc]3[cd]ef"))
