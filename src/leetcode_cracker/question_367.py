def print_question():
    print("""
Given a positive integer num, return true if num is a perfect square or false otherwise.

A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.

You must not use any built-in library function, such as sqrt.
""")
def print_solution():

    print("""
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        for i in range(num+1):
            if i*i == num:
                return True
            elif i*i > num:
                return False
        return False
    """)
def solution_stats():
    print("""
        Time: Beats 5.30%
        Memory: Beats 91.78%
    """)
    

  
