class Solution:
#
    def longestKSubstr(self, s, k):
        mx = -1
        i, j = 0, 0
        dic = {}
        while j < len(s):
            if s[j] not in dic:
                dic[s[j]] = 1
            else:
                dic[s[j]] += 1

            if len(dic) < k:
                j += 1
            elif len(dic) == k:
                mx = max(mx, j - i + 1)
                j += 1
            elif len(dic) > k:
                while i <= j and len(dic) > k:
                    if s[i] in dic:
                        count = dic[s[i]]
                        count -= 1
                        if count == 0:
                            del dic[s[i]]
                        else:
                            dic[s[i]] = count
                    i += 1
                j += 1
        return mx