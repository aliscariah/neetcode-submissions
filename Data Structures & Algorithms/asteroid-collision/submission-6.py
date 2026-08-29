class Solution:
    def asteroidCollision(self, aster: List[int]) -> List[int]:

        stack=[]
        stack.append(aster[0])

        for num in range(1,len(aster)):
            if stack and stack[-1]<0:
                stack.append(aster[num])
            elif not stack:
                stack.append(aster[num])
            else:
                if aster[num]>0:
                    stack.append(aster[num])
                else:
                    if stack[-1]==(-1*aster[num]):
                        stack.pop()
                    else:
                        while stack and stack[-1]>0 and stack[-1]<(-1*aster[num]):
                            stack.pop()
                        if not stack or stack[-1]<0:
                            stack.append(aster[num])
                        elif stack[-1]==(-1*aster[num]):
                            stack.pop()
                        
        return stack