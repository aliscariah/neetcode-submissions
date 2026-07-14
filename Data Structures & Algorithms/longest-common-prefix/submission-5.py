class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pos=strs[0]
        for i in range(0,len(pos)):
            for word in strs:
                if len(word)>i:
                    if pos[i]!=word[i]:
                        return pos[0:i]
                elif len(word)== 0:
                    return ""
                else:
                    return pos[0:i]
        return pos

                    



        