def print_question():
    print("""Given two binary strings a and b, return their sum as a binary string.""")
def print_solution():

    print("""
class Solution(object):
    def addBinary(self, a, b):
        def binaryToDecimal(n):
            return int(n,2)
        decimalresult = binaryToDecimal(a) + binaryToDecimal(b)
        return format(decimalresult, 'b')
    """)
def solution_stats():
    print("""
        Time: Beats 5.30%
        Memory: Beats 82.52%
    """)
    

  
