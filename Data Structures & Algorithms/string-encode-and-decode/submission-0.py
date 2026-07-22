class Solution:

    def encode(self, strs: List[str]) -> str:
        sentence=""
        for wrd in strs:
            sentence+=str(len(wrd))+'#'+ wrd
        return sentence
   

    def decode(self, s: str) -> List[str]:
        i=0
        result=[]
        while i<len(s):
            j=s.find('#',i)
            l=int(s[i:j])
            word=s[j+1:j+l+1]
            result.append(word)
            i=j+l+1

        return result


