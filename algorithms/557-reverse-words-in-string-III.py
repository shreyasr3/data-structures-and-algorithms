class Solution:
    def reverseWords(self, s: str) -> str:
        str_list = s.split()
        return " ".join([sl[::-1] for sl in str_list])
        
     
## O(n)

class Solution:
    def reverseWords(self, s: str) -> str:
        right, left = 0, 0
        res = []
        
        while right < len(s):
            if s[right] == " ":
                res.append(s[left:right][::-1])
                left = right+1
        
            right += 1
        
        res.append(s[left:right][::-1])
        return " ".join(res)
       
    
