
# User function Template for python3

class Solution:
    
    #Function to reverse words in a given string.
    def reverseWords(self,S):
        # code here 
        
        x=S.split(".")
        
        ans=""
        
        for i in x[::-1]:
            ans=ans+i
            ans=ans+"."
        
        final=""
        for i in range(len(ans)-1):
            final+=ans[i]
        
        return final
        
        
            

#{ 
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = str(input())
        obj = Solution()
        print(obj.reverseWords(s))

# } Driver Code Ends