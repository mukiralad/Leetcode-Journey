class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        Dict={}
        
        for i in nums:
            if(i in Dict):
                Dict[i]+=1
            else:
                Dict[i]=1
        
        #print(Dict)
        
        #{1: 3, 2: 2, 3: 1}
        
        heap=[]
        for i in Dict:
            heappush(heap,(-Dict[i],i))
        
        print(heap)
        
        ans=[]
        for i in range(k):
            ans.append(heappop(heap)[1])
        
        return ans
        
            
            
        
        
            
            
            
    
        
    

            

        