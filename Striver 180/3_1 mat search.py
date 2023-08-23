class Solution:
    def searchMatrix(self, mat: List[List[int]], key: int) -> bool:
        i=0
        j=len(mat[0])-1
        r=len(mat)
        while  i<r and j>=0:
            if mat[i][j]==key:
                return True
            elif mat[i][j]<key:
                i+=1
            else:
                j-=1
        return False