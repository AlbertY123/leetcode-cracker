def print_question():
    print("""Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.""")
def print_solution():

    print("""
  class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        ##This code does not work with 0, 0, 1.
        ##Expected = 1, 0, 0   Recieved = 0, 1, 0


        # for i in range(len(nums)):
        #     if nums[i] == 0:
        #         nums.pop(i)
        #         nums.append(0)

        #In 1, 3, 12, 0, 0 Expected 1,3 , 12, 0, 0 Return 12, 3, 1, 0, 0
        # for i in range(len(nums)):
        #     if nums[i] != 0:
        #         value = nums.pop(i)
        #         nums.insert(0, value)

        insertpos = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                value = nums.pop(i)
                nums.insert(insertpos, value)
                insertpos += 1
    """)
def solution_stats():
    print("""
        Time: Beats 21.55%
        Memory: Beats 50.84%
    """)
    

  
