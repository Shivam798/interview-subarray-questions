class Solution:
    def reverseWords(self, s: str) -> str:
        listt=s.split()
        print(listt)
        st=""
        for i in listt[::-1]:
            st+=i+" "
        return st[:-1]