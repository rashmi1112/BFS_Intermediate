# TC: O(N) where N is the number of employees in the input
# SC: O(N) since we will be performing dfs for all the subordinates of an employee.

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        if not employees or len(employees) == 0:
            return 0
        
        queue = collections.deque()
        self.hmap = {}
        self.result = 0
        for i in range(len(employees)):
            self.hmap[employees[i].id] = employees[i]
        
        emp = self.hmap.get(id)
        queue.append(emp)
        while queue:
            curr_emp = queue.popleft()
            self.result += curr_emp.importance
            if curr_emp.subordinates:
                for subid in curr_emp.subordinates:
                    queue.append(self.hmap.get(subid))
        
        return self.result
