from typing import List


class Solution:
    @staticmethod
    def compress(chars: List[str]) -> int:
        i = res = 0
        count = 1
        while i < len(chars):
            if i < len(chars) - 1 and chars[i] == chars[i + 1]:
                count += 1
            else:
                chars[res] = chars[i]
                res += 1
                if count > 1:
                    count_str = str(count)
                    for cs in count_str:
                        chars[res] = cs
                        res += 1
                count = 1
            i += 1
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.compress(["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]))
