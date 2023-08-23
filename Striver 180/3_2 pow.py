class Solution:
    def myPow(self, x: float, n: int) -> float:
        def fun(base=x,expo=abs(n)):
            if expo==0:
                return 1
            elif expo%2==0:
                return fun(base*base,expo//2)
            else:
                return base*fun(base*base,(expo-1)//2)
        f=fun()
        return float(f) if n>=0 else 1/f 
    
class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x**n