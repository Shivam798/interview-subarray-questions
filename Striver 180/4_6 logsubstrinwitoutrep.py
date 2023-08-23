class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st=set()
        l=0
        maxx=0
        for i in range(len(s)):
            if s[i] not in st:
                st.add(s[i])
                maxx=max(maxx,i-l+1)
            else:
                while s[i] in st:
                    st.remove(s[l])
                    l+=1
                st.add(s[i])
        return maxx
       