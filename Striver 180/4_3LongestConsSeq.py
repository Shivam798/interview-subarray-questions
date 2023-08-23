class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=set(nums)
        maxx=0
        for i in nums:
            if i-1 in nums:
                continue
            else:
                length=1
                while i+length in nums:
                    length+=1
                maxx=max(maxx,length)
        return maxx

            
