class MinStack:

    def __init__(self):
        self.s1=[]
        self.m=[]
        

    def push(self, val: int) -> None:
        self.s1.append(val)
        if self.m:
                self.m.append(min(val,self.m[-1]))
        else: 
            self.m.append(val)

        

    def pop(self) -> None:
        if self.s1 :
            self.s1.pop()
        if self.m:
            self.m.pop()


        
        
    def top(self) -> int:
        if self.s1 :
            return self.s1[-1]

        

    def getMin(self) -> int:
        return self.m[-1]
        
        
