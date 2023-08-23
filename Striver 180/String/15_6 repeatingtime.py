class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        multiple=len(b)//len(a)
        for i in range(multiple+3):
            if b in a*i:
                return i
        return -1