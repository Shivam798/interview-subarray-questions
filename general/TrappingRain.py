class Solution:
    def trap( bars: list[int]) -> int:
        if not bars or len(bars)<3:
            return 0
        left=0
        right=len(bars)-1
        maxl=bars[left]
        maxr=bars[right]
        water=0
        while left<right:
            maxl,maxr=max(bars[left],maxl),max(maxr,bars[right])
            if maxl<=maxr:
                water+=maxl-bars[left]
                left+=1
            else:
                water+=maxr-bars[right]
                right-=1
        return water
    def trap_space_n(bars):
        n=len(bars)
        maxl=[0]*n
        maxr=[0]*n
        maxl[0]=bars[0]
        maxr[-1]=bars[-1]
        water=0
        for i in range(1,n):
            maxl[i]=max(maxl[i-1],bars[i])
        for i in range(n-2,-1,-1):
            maxr[i]=max(bars[i],maxr[i+1])
        
        for i in range(n):
            water+=min(maxr[i],maxl[i])-bars[i]
        return water
    
obj=Solution
print(obj.trap_space_n([1,8,6,2,5,4,8,3,7]))