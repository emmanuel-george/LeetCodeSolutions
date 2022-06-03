class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mx = 0
        dic = {}
        i, j = 0, 0
        while j < len(s):
            if s[j] not in dic:
                dic[s[j]] = 1
            else:
                dic[s[j]] += 1
            if len(dic) == j - i + 1:
                mx = max(mx, j - i + 1)
                j += 1
            elif len(dic) < j - i + 1:
                while i <= j and len(dic) < j - i + 1:
                    dic[s[i]] -= 1
                    if dic[s[i]] == 0:
                        del dic[s[i]]
                    i += 1
                j += 1
            elif len(dic) > j - i + 1:
                j += 1
        return mx


