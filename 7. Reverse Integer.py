'''
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
'''

class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            sign = -1
            x = -x
        else:
            sign = 1
        num_str = str(x)
        
        reverse_str = ''
        for i in num_str[::-1]:
            reverse_str = reverse_str + i
        
        reverse_num = int(reverse_str) * sign
        
        if (-2 **31)<reverse_num < (2 **31-1):
            return reverse_num
        else:
            return 0
