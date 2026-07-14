class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s={}
        dict_t={}
        for wrd in s:
            if wrd in dict_s:
                dict_s[wrd]+=1
            else:
                dict_s[wrd]=1
        for wrd in t:
            if wrd in dict_t:
                dict_t[wrd]+=1
            else:
                dict_t[wrd]=1
        if dict_s==dict_t:
            return True
        else: return False
        
        