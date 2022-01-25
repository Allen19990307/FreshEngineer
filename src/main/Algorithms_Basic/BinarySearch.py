#使用python实现二分查找算法，logn的时间复杂程度
def BinarySearch(nums,target):
      length = len(nums)
      max = length - 1
      min = 0
      while min <= max:
         # // 在list中代表的是整数除法，而 / 代表的浮点除法
         mid =( min + max ) // 2
         if nums[mid] > target:
            max = mid - 1
         elif nums[mid] < target:
            min = mid + 1
         else:
            return mid
      return -1
if __name__ == '__main__':
    """Given an array of integers nums which is sorted in ascending order, 
       and an integer target, write a function to search target in nums. 
       If target exists, then return its index. Otherwise, return -1.
       You must write an algorithm with O(log n) runtime complexity.
        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/binary-search
"""
    nums = [1,2,3,4,5,6]
    target = 5
    search = BinarySearch(nums, target)
    print(search)