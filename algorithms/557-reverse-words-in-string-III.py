class Solution:
    def reverseWords(self, s: str) -> str:
        str_list = s.split()
        return " ".join([sl[::-1] for sl in str_list])
        
        
    
