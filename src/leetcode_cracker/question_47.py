def print_question():
    print("""
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.
""")
def print_solution():

    print("""
import itertools
class Solution(object):
    def permuteUnique(self, nums):
        num = itertools.permutations(nums) 
        return list(OrderedDict.fromkeys(num)) 
    """)
def solution_stats():
    print("""
        Time: Beats 34.27%
        Memory: Beats 19.60%
    """)
    

  
