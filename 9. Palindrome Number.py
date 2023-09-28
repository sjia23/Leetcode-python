class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        l = 0
        r = len(str(x)) - 1
        y = str(x)
        while r > l:
            if y[l] == y[r]:
                l = l + 1
                r = r - 1
            else:
                return False
        return True
