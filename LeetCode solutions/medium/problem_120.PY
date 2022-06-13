class Solution:
    def minimumTotal(self, triangle):
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(i + 1):
                triangle[i][j] += min(triangle[i + 1][j],
                                      triangle[i + 1][j + 1])

        return triangle[0][0]


ob1 = Solution()
triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
print(ob1.minimumTotal(triangle))
