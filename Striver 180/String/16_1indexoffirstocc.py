class Solution:
    def strStr(self, h: str, n: str) -> int:
        new=h.replace(n,'A')
        if h==new:
            return -1
        else:
            return new.index('A')
        
class Solution:
    def strStr(self, h: str, n: str) -> int:
        l=len(n)
        for i in range(len(h)):
            if h[i:l+i]==n:
                return i
        return -1
            