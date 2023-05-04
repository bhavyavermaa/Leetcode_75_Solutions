class Solution:

    def dfs(self,i,j,n,m,grid):
        if(i<0 or j<0 or i==n or j==m or grid[i][j]=="0" ):return
        grid[i][j]="0"
        self.dfs(i,j+1,n,m,grid)
        self.dfs(i,j-1,n,m,grid)
        self.dfs(i+1,j,n,m,grid)
        self.dfs(i-1,j,n,m,grid)
        return

    def numIslands(self, grid: List[List[str]]) -> int:
        n=len(grid)
        m=len(grid[0])
        ans=0
        for i in range(n):
            for j in range(m):
                if(grid[i][j]=="0"):continue
                ans+=1
                self.dfs(i,j,n,m,grid)
        return ans