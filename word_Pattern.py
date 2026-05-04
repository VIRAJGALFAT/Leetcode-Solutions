#https://leetcode.com/problems/word-pattern/description/

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        store = dict()
        s = s.split()
        if len(s) != len(pattern):
            return False
            
        for i in range(len(s)):
            if pattern[i] in store:
                if store[pattern[i]] != s[i]:
                    return False
            else:
                store[pattern[i]] = s[i]
        if len(store.values()) != len(set(store.values())):
            return False
       
        return True
