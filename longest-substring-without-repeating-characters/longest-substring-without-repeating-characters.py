class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == " ": return 1
        res = []
        maxlen = 0
        for i in s:
            if i not in res:
                res.append(i)
                maxlen = max(maxlen,len(res))
            else:
                maxlen = max(maxlen,len(res))
                # find the last occurence
                last = len(res) - res[::-1].index(i) - 1
                res = res[last+1:]
                res.append(i)
                
        return maxlen