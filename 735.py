from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        res =[]
        for i in range(len(asteroids)):
            if asteroids[i] > 0:
                res.append(asteroids[i])
            else:
                while len(res) > 0 and res[-1] > 0:
                    if abs(asteroids[i]) > abs(res[-1]):
                        res.pop()
                    elif abs(asteroids[i]) < abs(res[-1]):
                        break
                    else:
                        res.pop()
                        break
                else:
                    res.append(asteroids[i])
        return res

s = Solution()
print(s.asteroidCollision([5, 10, -5]))
print(s.asteroidCollision([8, -8]))
print(s.asteroidCollision([10, 2, -5]))
