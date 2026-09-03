class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        result = [0] * len(t)
        # if len(t) == 1:
        #     return result
        # for i in range(len(t)):
        #     for j in range(i+1, len(t)):
        #         if t[j] > t[i]:
        #             result[i] = j - i
        #             break
        stack=[]
        for i in range(len(t)):
            while stack and t[stack[-1]]<t[i]:
                prev=stack.pop()
                result[prev]=i-prev
            stack.append(i)
        return result
