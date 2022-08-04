class Solution:
    def isValid(self, s: str) -> bool:
        
        stack=[]
        dic={"}":"{","]":"[",")":"("}
        
        for i in s:
            if i in ["(","[","{"]:
                stack.append(i)
                
          
            else:
                
                if len(stack)==0:
                    return False
                
                x=stack.pop()
                if(dic[i]!=x):
                    return False
        
        if(len(stack)==0):
            return True
                
        