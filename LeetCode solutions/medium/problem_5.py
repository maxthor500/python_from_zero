def longestPalindrome(s):
    longestSubs = ""

    start = 0
    for i in range(len(s)):
        left, right = i, i

        while left >= 0 and right < len(s) and s[left] == s[right]:
            if (right - left + 1) > start:
                longestSubs = s[left:right+1]
                start = right - left + 1
            left -= 1
            right += 1

        left, right = i, i + 1

        while left >= 0 and right < len(s) and s[left] == s[right]:
            if (right - left + 1) > start:
                longestSubs = s[left:right+1]
                start = right - left + 1
            left -= 1
            right += 1
    return longestSubs



str = "babad"
print(longestPalindrome(str))


