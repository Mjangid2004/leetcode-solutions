class Solution(object):
    def reverse(self, x):
        # rev = 0
        # while x != 0:
        #     d = x % 10
        #     rev = rev * 10 + d
        #     x //= 10
        # return rev    

        sign = -1 if x < 0 else 1
        x_str = str(abs(x))
        rev = int(x_str[::-1]) * sign  
        
        if rev < -2**31 or rev > 2**31 - 1: 
            return 0
        return rev