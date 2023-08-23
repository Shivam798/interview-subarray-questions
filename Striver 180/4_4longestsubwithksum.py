class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        summ=0
        d={0:1}
        ans=0
        for i in nums:
            summ+=i
            if summ-k in d:
                ans+=d[summ-k]
            if summ not in d:
                d[summ]=1
            else:
                d[summ]+=1
            
        return ans