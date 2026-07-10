class Solution:
    def isPalindrome(self, x: int) -> bool:
        D = x
        rev = 0
        while x>0:
            l_d = x%10
            x=x//10
            rev = (rev*10) + l_d
        if rev==D:
            return True
        else:
            return False

        