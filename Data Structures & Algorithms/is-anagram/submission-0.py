class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        charS = {}
        charT = {}

        for x in s:
            if x not in charS.keys():
                charS[x] = 1
            
            else:
                charS[x] = charS[x] + 1

        for y in t: 
            if y not in charT.keys():
                charT[y] = 1

            else:
                charT[y] = charT[y] + 1

        if charS == charT:
            return True
        
        else:
            return False


    
        