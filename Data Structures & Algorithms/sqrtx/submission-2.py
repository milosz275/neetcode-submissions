class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        middle = (right - left) // 3 + left
        while left <= right:
            target = middle * middle
            if target == x:
                return middle
            elif target > x:
                right = middle - 1
            else:
                left = middle + 1
            middle = (right - left) // 2 + left
        return right