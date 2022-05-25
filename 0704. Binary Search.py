'''
iven an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:  
                                                                        # binary search, 用target 和list的中间值 作对比, 不断缩小范围
        left, right = 0, len(nums) - 1                                  # 设置左右 pointer
        while left <= right:  
            pivot = left + (right - left) // 2                          # 在这里 我们设置 中间值 为 pivot, 这样的算法 保证不会overflow
            if nums[pivot] == target:                                   # 如果pivot 等于 target return, 如果 大于小于,挪动相应的 bound
                return pivot
            if target < nums[pivot]:
                right = pivot - 1
            else:
                left = pivot + 1
        return -1
