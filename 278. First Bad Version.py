'''
You are a product manager and currently leading a team to develop a new product. Unfortunately, 
the latest version of your product fails the quality check. Since each version is developed based 
on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes 
all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a
function to find the first bad version. You should minimize the number of calls to the API.
'''
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n                                                    # 设置左右pointer
        while left < right:                     
            mid = left + (right - left) // 2                                  # 设置 pivot
            if isBadVersion(mid):                                             # 如果pivot 是bad version 重置, right bound, 
                right = mid
            else:                                                             # 如果不是, 重置left bound, 直到 left = right, 并且能确保, right一直为bad version
                left = mid + 1
        return left
