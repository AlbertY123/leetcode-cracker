def print_question():
    print("""Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.""")
def print_solution():

    print("""
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        temp = []
        result = []

        def loop(openN, closeN):
            if openN == n == closeN:
                result.append("".join(temp))
                return
            
            if openN < n:
                temp.append("(")
                loop(openN + 1, closeN)
                temp.pop()

            if closeN < openN:
                temp.append(")")
                loop(openN, closeN +1)
                temp.pop()

        loop(0, 0)
        return result
    """)
def solution_stats():
    print("""
        Time: Beats 5.60%
        Memory: Beats 26.93%
    """)
    

  
