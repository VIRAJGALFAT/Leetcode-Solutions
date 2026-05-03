#https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/


class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        store = {}
        for i in s:
            if i not in store:
                store[i] = 1
            else:
                store[i] += 1
        lst = []
        for j in store.values():
            lst.append(j)

        l = lst[0]
        ans = True
        for k in lst:
            if l == k:
                pass
            else:
                ans = False
        return ans

        
