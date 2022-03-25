class Solution:
    def isHappy(self, n: int) -> bool:
        while len(str(n)) > 1:
            total = 0
            for i in str(n):
                total+=int(i)**2
            n = total
        if n == 1 or n == 7:
            return True
        else:
            return False