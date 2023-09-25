from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        mx = 0
        ans = []
        for i in range(len(candies)):
            if candies[i] > mx:
                mx = candies[i]

        for i in range(len(candies)):
            if (candies[i] + extraCandies) >= mx:
                ans.append('true')
            else:
                ans.append('false')
        return ans

if __name__ == "__main__":
    s = Solution()
    extraCandies = 3
    candies = [2, 3, 5, 1, 3]
    ans = s.kidsWithCandies(candies, extraCandies)
    print(ans)
