def print_question():
    print("""A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
A self-dividing number is not allowed to contain the digit zero.

Given two integers left and right, return a list of all the self-dividing numbers in the range [left, right].

""")
def print_solution():

    print("""
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        returnvalue = []
        value = 0
        for i in range(right-left+2):
            value = i+left
            valuelist = [int(x) for a,x in enumerate(str(value))]
            correctvalues = 0
            for i in range(len(valuelist)):
                if valuelist[i] == 0:
                    pass
                elif value%valuelist[i] == 0:
                    correctvalues += 1
            if correctvalues == len(valuelist):
                returnvalue.append(value)
        return returnvalue

    """)
def solution_stats():
    print("""
        Time: Beats 5.68%
        Memory: Beats 96.55%
    """)
    

  
