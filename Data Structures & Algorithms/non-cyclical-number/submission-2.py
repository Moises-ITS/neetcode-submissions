class Solution:
    def sum_squared(self, num:int) -> int:
        sum_squares = 0
        digit = 0
        while num:
            digit = num % 10
            sum_squares += math.pow(digit, 2)
            num = num // 10
        return int(sum_squares)

    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            if n in seen:
                return False
            else:
                seen.add(n)
            n = self.sum_squared(n)
            print(n)
        return True
