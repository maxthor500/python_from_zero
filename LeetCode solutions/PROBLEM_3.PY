class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if not s:
            return 0

        countMap = 0
        index = 0
        letterMap = {}
        answer = 0
        while index < len(s):
            if (s[index] not in letterMap) or (countMap > letterMap[s[index]]):
                answer = max(answer, (index - countMap + 1))
                letterMap[s[index]] = index
            else:
                countMap = letterMap[s[index]]+1
                answer = max(answer, (index - countMap + 1))
                index -= 1
            index += 1
        return answer


ob1 = Solution()
print(ob1.lengthOfLongestSubstring("pwwkew"))
