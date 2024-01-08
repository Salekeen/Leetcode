from typing import List


class Solution:
    @staticmethod
    def asteroidCollision(asteroids: List[int]) -> List[int]:
        asteroid_stack = []
        for asteroid in asteroids:
            while asteroid_stack and asteroid_stack[-1] > 0 > asteroid:
                diff = asteroid_stack[-1] + asteroid
                if diff < 0:
                    asteroid_stack.pop()
                elif diff > 0:
                    asteroid = 0
                else:
                    asteroid_stack.pop()
                    asteroid = 0
            if asteroid:
                asteroid_stack.append(asteroid)
        return asteroid_stack


if __name__ == '__main__':
    solution = Solution()
    print(solution.asteroidCollision([10, 2, -5]))
