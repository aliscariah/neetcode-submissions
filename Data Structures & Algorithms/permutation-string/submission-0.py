class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        left=0
        right=len(s1)
        s1_dict = {}
        for ch in s1:
            s1_dict[ch] = s1_dict.get(ch, 0) + 1
        
        while right<=len(s2):
            s2_dict={}
            for i in range(left, right):
                s2_dict[s2[i]] = s2_dict.get(s2[i], 0) + 1
            if s1_dict == s2_dict:
                return True
            
            left+=1
            right+=1
            
        return False





     


            

