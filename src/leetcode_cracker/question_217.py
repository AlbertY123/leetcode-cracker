def print_question():
    print("""class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for i in range(len(nums)):
            if nums[i] in hashset:
                return True
            hashset.add(nums[i])
        return False
""")
def print_solution():

    print("""
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for i in range(len(nums)):
            if nums[i] in hashset:
                return True
            hashset.add(nums[i])
        return False

    """)
def solution_stats():
    print("""
        Time: Beats 99.94%
        Memory: Beats 99.57%
    """)
    

  
