class Solution:
    def isValid(self, s: str) -> bool:
        d= { '(':')','{':'}','[':']'}
        stack=[]
        for i in s:
            if i in d:
                stack.append(i)
            else:
                if stack and i == d[stack[-1]]:
                    stack.pop()
                else:
                    return False
        return len(stack)==0
        