def print_question():
    print("""
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.
    """)
def print_solution():

    print("""
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        newlist = []
        oldnum = 0
        for i in range(len(nums)):
            newlist.append(oldnum + nums[i])
            oldnum = oldnum + nums[i]
        return newlist
    """)
def solution_stats():
    print("""
        Time: Beats 35.31%
        Memory: Beats 62.14%
    """)
    

  
