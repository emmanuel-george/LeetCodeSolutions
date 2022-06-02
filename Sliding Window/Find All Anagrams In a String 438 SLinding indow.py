def findAnagrams(self, s: str, p: str):
    count = 0
    count_words = {}

    # Count each occurences in anagram
    for word in p:
        if word not in count_words:
            count_words[word] = 1
        else:
            count_words[word] += 1

    i = j = 0
    ans = []
    while j < len(s):

        # calculations
        if s[j] in count_words:
            count_words[s[j]] -= 1
            if count_words[s[j]] == 0:
                count -= 1

        # check window size
        if j - i + 1 < len(p):
            j += 1

        # Fixed window size
        elif j - i + 1 == len(p):
            if count == 0:
                ans.append(i)
                print(str(i))
        # Delete s[i]
        # Reverse the calculations
        if s[i] in count_words:
            count_words[s[i]] += 1
            if count_words[s[i]] == 1:
                count += 1
        # Slide the window
        j += 1
        i += 1
    return ans


if __name__ == '__main__':
    p = 'abbc'
    s = "cbaebabacd"
    k = len(p)
    hmap = {}
    ans = []
    for i in range(len(p)):
        if p[i] not in hmap:
            hmap[p[i]] = 1
        else:
            count1 = hmap[p[i]]
            hmap[p[i]] = count1 + 1
    print(hmap)
    count = len(hmap)
    i = 0
    j = 0

    while j < len(s):
        if s[j] in hmap:
            c1 = hmap[s[j]]
            c1 -= 1
            hmap[s[j]] = c1
            if c1 == 0:
                count -= 1
        # Increment J until window size is matched
        if j - i + 1 < k:
            j += 1
        # Window size matched
        elif j - i + 1 == k:
            if count == 0:
                ans.append(j)
            # remove the calculation for i from count while sliding
            if hmap[s[i]] == 0:
                count += 1
            count2 = hmap[s[i]]
            count2 += 1
            hmap[s[i]] = count2
            i += 1
            j += 1
