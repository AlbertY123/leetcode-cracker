def print_question():
    print("""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 """)
def print_solution():

    print("""
class Solution:
    def twoSum(self, nums, target):
        hashMap = {nums[i]:i for i in range(len(nums))}
        for i in range(len(nums)):
            if target-nums[i] in hashMap and hashMap[target-nums[i]] != i:
                return i, hashMap[target-nums[i]]
    """)
def solution_stats():
    print("""
        Time: Beats: 71.96%
        Memory: Beats 15.65%
    """)
    

  
