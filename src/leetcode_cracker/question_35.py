def print_question():
    print("""Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.""")
def print_solution():

    print("""
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        for i in range(len(nums)):
            if nums[i] == target:
                return i
            if nums[i] > target:
                return i
        return len(nums)

    """)
def solution_stats():
    print("""
        Time: Beats 6.61%
        Memory: Beats 26.92%
    """)
    

  
