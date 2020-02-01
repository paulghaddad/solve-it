class Solution:
    def reverse(self, x: int) -> int:
        reversed_int = 0

        el = abs(x)
        while (el):
            rdigit = el % 10
            x = int(el / 10)
            reversed_int = reversed_int * 10 + rdigit

        if reversed_int > 2**31:
            return 0

        return reversed_int
