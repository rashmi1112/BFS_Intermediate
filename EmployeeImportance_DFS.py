# TC: O(N) 
# SC: O(H) where H is the size of the recursive stack. 

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        if not employees or len(employees) == 0:
            return 0
        
        self.hmap = {}
        self.result = 0
        for i in range(len(employees)):
            self.hmap[employees[i].id] = employees[i]
        
        def dfs(id):
            emp = self.hmap.get(id)
            self.result += emp.importance
            for i in emp.subordinates:
                dfs(i)
            
        dfs(id)
        return self.result
