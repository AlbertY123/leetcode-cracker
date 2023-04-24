def print_question():
    print("""Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal 
substring
 consisting of non-space characters only.""")
def print_solution():

    print("""
class Solution(object):
    def lengthOfLastWord(self, s):

        word_list = re.findall(r'\w+', s)
        if len(word_list) >=1:
            return len(word_list[-1])
        else:
            return 0
    """)
def solution_stats():
    print("""
        Time: Beats 5.98%
        Memory: Beats 31.35%
    """)
    

  
