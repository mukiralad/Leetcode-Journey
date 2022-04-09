#User function Template for python3

class Solution:
    def segregate0and1(self, arr, n):
        # code here
        count0=0
        count1=0
        for i in range(len(arr)):
            if(arr[i]==0):
                count0+=1

            
        
        for i in range(0,count0):
            arr[i]=0
        
        for j in range(count0,n):
            arr[j]=1
            
            
                

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.segregate0and1(arr, n)
        print(*arr)
        tc -= 1

# } Driver Code Ends