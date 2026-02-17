class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        s = set(nums)
        lst = sorted(s, reverse=True)
        
        if len(lst) >= 3:
            return lst[2]
        else:
            return lst[0]
