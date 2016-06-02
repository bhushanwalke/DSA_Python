def wordBreak(s, wordDict):
    """
    :type s: str
    :type wordDict: Set[str]
    :rtype: bool
    """
    n = len(s)
    if not s or n == 0:
        return False

    dp = [False] * (n+1)
    dp[0] = True

    for i in range(1, n+1):
        for j in range(i):
            if dp[j] and s[j:i] in wordDict:
                dp[i] = True
                break
    return dp[-1]


dict = ["leet", "code"]
s = "leetcode"

print wordBreak(s, dict)
