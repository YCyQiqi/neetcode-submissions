class Solution:
    def isPalindrome(self, s: str) -> bool:
        newstr = ""
        for x in s:
            if x.isalnum() == True:
                newstr = newstr + x
     
        left = 0
        right = len(newstr) - 1
        while left <= right: 

            if newstr[left].lower() == newstr[right].lower():
                left += 1
                right -= 1
            else: 
                return False

                
        
        return True
            

        