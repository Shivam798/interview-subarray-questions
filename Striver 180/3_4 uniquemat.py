class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        

        def helper(i,j,m,n):
            if i==m-1 and j==n-1:
                return 1
            elif i>=m or j>=n:
                return 0
            elif dp[i][j]!=-1:
                return dp[i][j]
            else:
                dp[i][j]=helper(i+1,j,m,n) + helper(i,j+1,m,n)
            return dp[i][j]

        dp=[[-1]*n for _ in range(m)]
        f=helper(0,0,m,n)
        
        return f
    
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[1]*n for _ in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j]=dp[i-1][j]+dp[i][j-1]
        return dp[-1][-1]
    