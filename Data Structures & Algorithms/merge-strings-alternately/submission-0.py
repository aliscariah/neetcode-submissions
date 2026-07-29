class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i=0
        j=0
        output=[]
        while i<len(word1) and j<len(word2):
            output.append(word1[i])
            output.append(word2[j])
            i+=1
            j+=1
        output.extend(word1[i:])   # grabs ALL remaining chars, not just one
        output.extend(word2[j:])   # only one of these will actually add anything
        return ''.join(output)    

        

        