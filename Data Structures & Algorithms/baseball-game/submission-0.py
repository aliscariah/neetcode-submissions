class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        total=0
        for op in operations:
            if op == '+':
                a=stack[-1]
                b=stack[-2]
                t=a+b
                stack.append(t)
            elif op =="D":
                a=stack[-1]
                t=a*2
                stack.append(t)
            elif op == "C":
                a=stack.pop()
            else:
                stack.append(int(op))
        
        for st in stack:
            total+=st
        return total
   



        