def print_question():
    print("""Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.""")
def print_solution():

    print("""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        #Store Numbers
        total = {}

        #For Every Number in nums list
        for n in nums:

            #If Number not in total, add it to total as 1
            if n not in total:
                total[n] = 1
            
            #Otherwise,
            else:
                #Increase it by one.
                total[n] += 1

            if total[n] > len(nums)/2:
                return n

    """)
def solution_stats():
    print("""
        Time: Beats 5.13%
        Memory: Beats 99.11%
    """)
    

  
