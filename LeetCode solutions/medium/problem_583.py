class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if (word1 == word2):
            return 0

        length1, length2 = len(word1), len(word2)

        dpLast, dpCurr = [0] * (length2 + 1), [0] * (length2 + 1)

        for i in word1:
            for j in range(length2):
                if i == word2[j]:
                    dpCurr[j+1] = dpLast[j] + 1
                else:
                    dpCurr[j+1] = max(dpCurr[j], dpLast[j+1])
            dpLast, dpCurr = dpCurr, dpLast
        return ((length1 + length2) - (2 * dpLast[length2]))
