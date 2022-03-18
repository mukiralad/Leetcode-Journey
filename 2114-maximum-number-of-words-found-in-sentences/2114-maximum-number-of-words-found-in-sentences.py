class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        count=0
        d=[]
        for i in range(len(sentences)):
            x=(sentences[i].count(' '))
            d.append(x)
        return max(d)+1
            
                
            
        
       
           
        
        