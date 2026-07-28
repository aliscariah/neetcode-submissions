class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        l=len(s)
        n=l//2
        for i in range(0,n):
            temp=s[i]
            s[i]=s[l-1-i]
            s[l-1-i]=temp
        print(s)
        
        