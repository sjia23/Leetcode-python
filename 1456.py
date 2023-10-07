class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = {'a', 'e', 'i', 'o', 'u'}

        cur, res = 0, 0
        for i in range(k):
            if s[i] in vowel: cur += 1
        res = cur
        for i in range(k, len(s)):
            if s[i] in vowel:
                cur += 1
            if s[i - k] in vowel:
                cur -= 1
            res = max(cur, res)
        return res
