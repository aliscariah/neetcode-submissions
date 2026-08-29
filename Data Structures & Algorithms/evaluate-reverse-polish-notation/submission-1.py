class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack=[]
        op = { '+','-','*','/'}
        for num in tokens:
            if num not in op:
                stack.append(int(num))
            else:
                
                b=stack.pop()
                a=stack.pop()
                if num == '+':
                    val=a+b
                elif num == '-':
                    val=a-b
                elif num == '*':
                    val=a*b
                else:
                    val= a/b

                
                stack.append(int(val))
        return stack[-1]