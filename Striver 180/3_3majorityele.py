class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]
    

from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d=Counter(nums)
        n=len(nums)
        for i,val in d.items():
            if val > (n//2):
                return i

# majority element 2            
from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d=Counter(nums)
        n=len(nums)
        n=n//3
        arr=[]
        for k,v in d.items():
            if v>n:
                arr.append(k)
        return arr 