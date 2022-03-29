class Solution:
    def average(self, salary: List[int]) -> float:
        
        salary=sorted(salary)
        x=len(salary)
        y=max(salary)
        z=min(salary)
        
        salary.remove(y)
        salary.remove(z)
        
        
        
        d=sum(salary)/len(salary)
        
        return(d)
        
        
        