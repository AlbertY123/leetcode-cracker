def print_question():
    print("""Given an integer n, return true if it is a power of four. Otherwise, return false.

An integer n is a power of four, if there exists an integer x such that n == 4x.""")
def print_solution():

    print("""
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 0:
            return False
        while n > 1:
            n = n/4
        if n == 1:
            return True
        else:
            return False
    """)
def solution_stats():
    print("""
        Time: Beats 94.11%
        Memory: Beats 89.11%
    """)
    

  
