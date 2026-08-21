class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need={}
        for i in range(len(t)):
            need[t[i]]=need.get(t[i],0)+1
        have=0
        left=0
        window={}
        minlen=float("inf")

        for right in range(len(s)):
            window[s[right]]=window.get(s[right],0)+1

            if s[right] in need and window[s[right]]==need[s[right]]:
                have+=1
            
            while have==len(need):
                currlen=right-left+1
                if currlen<minlen:
                    minlen=currlen
                    start=left
                window[s[left]]-=1
                if s[left] in need and window[s[left]]<need[s[left]]:
                    have-=1
                left+=1
        if minlen==float("inf"):
            return ""
        return s[start:start+minlen]        