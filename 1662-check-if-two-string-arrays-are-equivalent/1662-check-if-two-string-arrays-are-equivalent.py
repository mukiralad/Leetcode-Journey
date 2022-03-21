class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        
        s=""
        d=""
        
        for i in range(len(word1)):
          
                
                s=s+word1[i]
        
        for j in range(len(word2)):
          
                
                d=d+word2[j]
        
        
        
        if(s==d):
            return True
        else:
            return False
       
       
                
                
        