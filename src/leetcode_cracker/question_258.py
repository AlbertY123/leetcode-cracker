def print_question():
    print("""Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.""")
def print_solution():

    print("""
class Solution(object):
    def addDigits(self, num):
        listedn = list(map(int, str(num))) 
        while True:
            new = 0
            for i in range(len(listedn)):
                new += listedn[i]   
            if len(str(new)) < 2:
                return new
            listedn = list(map(int, str(new))) 
        # listedn = list(map(int, str(num)))
        # new = 0
        # for i in range(len(listedn)):
        #     new += listedn[i]
        
        # if len(str(num)) > 1:
        #     for i in range(len(listedn)):
        #         new += listedn[i]
        # else:
        #     answer = 0
        #     for i in range(len(listedn)):
        #         answer += listedn[i]
        #     return answer
        

    """)
def solution_stats():
    print("""
        Time: Beats 5.81%
        Memory: Beats 65.41%
    """)
    

  
