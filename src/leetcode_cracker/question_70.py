def print_question():
    print("""
    You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
""")
def print_solution():

    print("""
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        sequence = [1, 2]

        
        return(self.climbStairs(n-1) + self.climbStairs(n-2))
    """)
def solution_stats():
    print("""
        Time: Beats 5.73%
        Memory: Beats 29.77%
    """)
    

  
