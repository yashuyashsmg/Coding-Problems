# Recursive solution 
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<0:
            return False
          
        # After recursive steps => n//4 yields 1
        elif n==1:
            return True
          
        # Check for the condition
        return (n%4==0 and self.isPowerOfFour(n//4))
