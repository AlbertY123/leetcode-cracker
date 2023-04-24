def print_question():
    print("""Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.
""")
def print_solution():

    print("""
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        while n > 1:
            n = n/2
        if n == 1:
            return True
        else:
            return False

    """)
def solution_stats():
    print("""
        Time: Beats 43.47%
        Memory: Beats 38.53%
    """)
    

  
