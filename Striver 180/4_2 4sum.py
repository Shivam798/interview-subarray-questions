class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n=len(nums)
    
        res=set()
        for i in range(0,n-3):
            if i>0 and nums[i]==nums[i-1]:continue
            for j in range(i+1,n-2):
                if j>i+1 and nums[j]==nums[j-1]:continue
                k=j+1
                l=n-1
                while k<l:
                    summ=nums[i]+nums[j]+nums[k]+nums[l]
                    if summ==target:
                        temp=(nums[i],nums[j],nums[k],nums[l])
                        
                        res.add(temp)
                        while k<l and nums[k]==nums[k+1] :k+=1 
                        while k<l and nums[l]==nums[l-1] :l-=1 
                        k+=1
                        l-=1
                    elif summ<target:
                        k+=1
                    else:
                        l-=1
                
        return res
    
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n=len(nums)
    
        res=set()
        for i in range(0,n-3):
            for j in range(i+1,n-2):
                k=j+1
                l=n-1
                while k<l:
                    summ=nums[i]+nums[j]+nums[k]+nums[l]
                    if summ==target:
                        temp=(nums[i],nums[j],nums[k],nums[l])
                        
                        res.add(temp) 
                        k+=1
                        l-=1
                    elif summ<target:
                        k+=1
                    else:
                        l-=1
                
        return res