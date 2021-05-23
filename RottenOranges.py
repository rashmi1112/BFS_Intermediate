# TC: O(M x N) where M is the rows of the matrix and N is the number of columns. 
# SC: O(M x N)

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0] or len(grid) == 0 or len(grid[0]) == 0:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        queue = collections.deque()
        fresh = time = 0
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i,j))
                if grid[i][j] == 1:
                    fresh += 1
        if fresh == 0:
            return 0
        
        while queue:
            for i in range(len(queue)):
                curr_x, curr_y = queue.popleft()
                dirs = [(0,1),(0,-1),(1,0),(-1,0)]
                for x, y in dirs:
                    new_x, new_y = curr_x + x, curr_y + y
                    if new_x >= 0 and new_y >= 0 and new_x < rows and new_y < cols and grid[new_x][new_y] == 1:
                        queue.append((new_x, new_y))
                        grid[new_x][new_y] = 2
                        fresh -= 1
            time += 1
        if fresh != 0:
            return -1 
        return time - 1   
                        
