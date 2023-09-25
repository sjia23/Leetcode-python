class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        u,d = 0,0
        while u < len(word1) and d < len(word2):
            res += word1[u]
            res += word2[d]
            u += 1
            d += 1
        while u < len(word1):
            res += word1[u]
            u += 1

        while d < len(word2):
            res += word2[d]
            d += 1
        return res
